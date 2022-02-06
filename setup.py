#!/usr/bin/env python

from distutils.core import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='Review Assigner',
      version='1.0',
      description='A small library built to randomly assign class reviews to each other',
      author='Michael Cerny Green',
      author_email='mcgreentn@gmail.com',
      install_requires=required,
)