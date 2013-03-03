#!/usr/bin/python2.5
#coding=utf8
from urllib2 import urlopen
import re
import sys
import os
import os.path

TAG_CODIFICACAO_LATIN1 = '<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"/>'
TAG_CODIFICACAO_UTF8 = '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>'

def escrever_arquivo(caminho, conteudo):
    f = open(caminho, 'w')    
    f.write(conteudo)
    f.close()

def ler_arquivo(caminho, open=open):
    return open(caminho, 'r').read()
    
def consertar_codificacao(pagina):
    return pagina.replace(TAG_CODIFICACAO_LATIN1, TAG_CODIFICACAO_UTF8)             

FORMATACOES_DEFAULT = [consertar_codificacao]
                  
class FormatadorCVSReport(object):

    formatacoes = FORMATACOES_DEFAULT
    
    def __init__(self, formatacoes=None):    
        if not (formatacoes is None):
            self.formatacoes = formatacoes
    
    def formatar(self, caminho_diretorio):
        for f in os.listdir(caminho_diretorio):
            if not f.endswith('.html'):
                continue
                
            print 'Formatando %s ...' % f            
            caminho = os.path.join(caminho_diretorio, f)
            pagina = ler_arquivo(caminho)
            
            for f in self.formatacoes:
                pagina = f(pagina)                
            
            escrever_arquivo(caminho, pagina)
        
def main():        
    diretorio = sys.argv[1]   

    print >> sys.stderr, 'Formatando %s ...' % diretorio 
           
    formatador = FormatadorCVSReport()
    formatador.formatar(diretorio)

print 'Concluído.'
