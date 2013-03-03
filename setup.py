from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='rbco.statcvswrapper',
      version=version,
      description="Very simple package to make use of StatCVS easier.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='cvs',
      author='Rafael Oliveira',
      author_email='rafaelbco@gmail.com',
      url="",
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rbco'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'prdg.util>=0.0.7,<=0.0.99',
      ],
      entry_points={
          'console_scripts': [
              'statcvs_wrapper = rbco.statcvswrapper.main:main',
              'statcvs_format = rbco.statcvswrapper.format:main',              
          ],
      },
)
