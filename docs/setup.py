#!/usr/bin/env python3
"""Python Packgage installation file

Install via
    $ pip install -e .

Install with extra via
    $ pip install -e .[extra_key1, extra_key2]

"""
import os
from setuptools import setup


def read(fname):
    """Shorthand function to read in a file"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='portfolio-docs',
    version='0.0.1',
    description='Ansible based Devops',
    long_description=read('README.md'),
    author='Joel Tannas',
    author_email='jtannas@gmail.com',
    url='https://github.com/jtannas',
    install_requires=['sphinx', ],
    extras_require={'dev': [
        'sphinx-autobuild',
        'sphinx_rtd_theme',
    ], },
)
