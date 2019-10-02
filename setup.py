#!/usr/bin/env python

import os

from setuptools import setup, find_packages


def path(fname=''):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), fname))


def readfile(fname):
    with open(path(fname)) as f:
        return f.read()


setup(
    name="theremin",
    version="0.1",
    author="Fabio Manganiello",
    author_email="info@fabiomanganiello.com",
    description="A theremin synth emulator controllable through a Leap Motion",
    license="MIT",
    python_requires='>= 3.5',
    keywords="music synth theremin pyo leap_motion",
    url="https://github.com/BlackLight/theremin",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'theremin=theremin:main',
        ],
    },
    long_description=readfile('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
    ],
    install_requires=[
        'pyo',
        # Also requires Leap.py from the Leap Motion SDK installation
        # see https://developer-archive.leapmotion.com/documentation/python/index.html
    ],
    extras_require={
    },
)
