#!/usr/bin/env python

from setuptools import setup

setup(
    name='HavocFrontend',
    packages=['havocfrontend'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
