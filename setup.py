import os
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='DANE-server',
    version='0.1',
    author='Nanne van Noord',
    author_email='n.j.e.vannoord@uva.nl',
    url='https://github.com/CLARIAH/DANE-server',
    description="Back-end for the Distributed Annotation 'n' Enrichment (DANE) system",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],

    packages=find_packages(exclude=('test',)),

    install_requires=[
      'DANE',
      'Flask',
      'mysql-connector-python',
      'pika',
    ])