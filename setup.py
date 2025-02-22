#!/usr/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages

NAME = "slip"
import slip
VERSION = slip.__version__ # << to change in __init__.py


setup(
    name = NAME,
    version = VERSION,
    packages = find_packages(exclude=['contrib', 'docs', 'tests']),
    author = "Laurent Perrinet INT - CNRS",
    author_email = "Laurent.Perrinet@univ-amu.fr",
    description = "SLIP: a Simple Library for Image Processing",
    long_description=open("README.md", 'r').read(),
    license = "GPLv2",
    install_requires=['numpy', 'NeuroTools'],
    extras_require={
                'html' : [
                         'vispy',
                         'matplotlib'
                         'jupyter>=1.0']
    },
    keywords = ('computational neuroscience', 'simulation', 'analysis', 'visualization', 'biologically-inspired', 'computer vision'),
    url = 'https://github.com/junchen1992/' + NAME, # use the URL to the github repo
    download_url = 'https://github.com/junchen1992/' + NAME + '/tarball/' + VERSION,
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: POSIX',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Utilities',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                  ],
     )
