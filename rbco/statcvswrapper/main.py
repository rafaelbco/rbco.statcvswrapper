#!/usr/bin/python
"""Usage: statcvs_wrapper.py DIRECTORY"""

import sys
import os
import os.path
import subprocess
import shutil
from format import FormatadorCVSReport
from prdg.util import proc

OUT_DIRNAME = 'cvs_report'
LOG_FILENAME = 'cvs_log.txt'

DEFAULT_FORMATTER = FormatadorCVSReport()

def create_report(working_copy_path, jar_path):
    """
    Create a report.
    
    Return: path of the created report directory.
    """
    os.chdir(working_copy_path)
    
    temp_filename = LOG_FILENAME + '.tmp'
    proc.call_subprocess_to_file(['cvs', 'log'], temp_filename)
    proc.call_subprocess_to_file(['iconv', '-f latin1', '-t utf8', temp_filename], LOG_FILENAME)     
        
    if os.access(OUT_DIRNAME, os.F_OK):
        shutil.rmtree(OUT_DIRNAME)
    os.mkdir(OUT_DIRNAME)    
    
    subprocess.call([
        'java',
        '-jar',
        os.environ['STATCVS_JAR_PATH'], 
        '-output-dir', 
        OUT_DIRNAME,
        LOG_FILENAME, 
        '.'
    ])
    
    return os.path.join(working_copy_path, OUT_DIRNAME)
    
def format_report(report_path, formatter):     
    print >> sys.stderr, 'Formatando %s ...' % report_path                
    formatter.formatar(report_path)    
    
def show_report(report_path):    
    subprocess.call(['firefox', os.path.join(report_path, 'index.html')])
    
def process_arguments():
    if len(sys.argv) != 2:
        raise RuntimeError(__doc__)
    
    working_copy_path = sys.argv[1]    
    if not os.path.isdir(working_copy_path):
        raise RuntimeError('Argument should be a directory.')
        
    jar_path = os.environ.get('STATCVS_JAR_PATH')
    if not jar_path:
        raise RuntimeError('STATCVS_JAR_PATH environment variable not set.')
        
    
    return (working_copy_path, jar_path)         

def main(formatter=DEFAULT_FORMATTER):
    (working_copy_path, jar_path) = process_arguments()
        
    report_path = create_report(working_copy_path, jar_path)
    format_report(report_path, formatter)
    show_report(report_path)
    
    
    
    
