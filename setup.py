#!/usr/bin/env python

import io
from setuptools import setup

with io.open('README.md', encoding='utf-8') as handle:
    long_description = handle.read()

kwargs = {
    "name": "reshaper",
    "description": long_description.splitlines()[0],
    "long_description": long_description,
    "url": "https://github.com/sanand0/reshaper",
    "author": "S Anand",
    "author_email": "root.node@gmail.com",
    "version": "1.1.1",
    "py_modules": ["reshaper"],
    "install_requires": ["pandas", "scipy", "tqdm", "GDAL"],
    "entry_points": {
        "console_scripts": ["reshaper=reshaper:cmdline"]
    },
    "license": "MIT",
    "keywords": "reshaper",
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ]
}

setup(**kwargs)
