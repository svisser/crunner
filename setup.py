# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


requires = [
    'mock==1.0.1',
    'watchdog==0.7.1',
]


setup(
    name="crunner",
    packages=['crunner'],
    version="0.2.0",
    description="Continues test runner.",
    author="Pawel Chomicki",
    author_email="pawel.chomicki@gmail.com",
    install_requires=requires,
    url="https://github.com/pchomik/crunner",
    scripts=['script/crun']
)