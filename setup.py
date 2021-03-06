#!/usr/bin/env python
# vim: set sw=4 et:

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import glob


# Fix for TypeError: 'NoneType' object is not callable" error
# when running 'python setup.py test'
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='webarchiveplayer',
    version='1.0.1',
    url='https://github.com/ikreymer/webarchiveplayer',
    author='Ilya Kreymer',
    author_email='ikreymer@gmail.com',
    description='Simple Point-and-Click Web Archive Player Tool',
    long_description='',
    license='GPL',
    packages=find_packages(),
    provides=[
        'archiveplayer',
        'archiveplayer.archiveplayer'
        ],
    package_data={
        'archiveplayer': ['templates/*'],
        },
    install_requires=[
        'pywb>=0.7.7',
        'waitress',
       ],
    dependency_links=[
#        'git+https://github.com/ikreymer/pywb.git@develop#egg=pywb-0.7.6'
    ],
    entry_points="""
        [console_scripts]
        webarchiveplayer = archiveplayer.archiveplayer:main
    """,
    tests_require=[
        'pytest',
        'WebTest',
        'pytest-cov',
       ],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: System :: Archiving',
        'Topic :: Utilities',
    ])
