#!/usr/bin/env python

from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='dyatel',
    version='0.0.4',
    author='Vyacheslav Anzhiganov',
    author_email='vanzhiganov@ya.ru',
    url='',
    long_description=long_description,
    scripts=[
        'dyatel.py',
    ],
    install_requires=[
        'requests',
        'pyyaml',
    ]
)
