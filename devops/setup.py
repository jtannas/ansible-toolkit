#!/usr/bin/env python3

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='joels-devops',
    version='0.0.1',
    description='Ansible based Devops',
    long_description=read('README.md'),
    author='Joel Tannas',
    author_email='jtannas@gmail.com',
    url='https://github.com/jtannas',
    packages=[
        'roles',
    ],
    install_requires=[
        'ansible',
    ],
)
