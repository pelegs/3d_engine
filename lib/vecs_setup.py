#!/usr/bin/env python3

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('vecs.pyx', annotate=True),
)
