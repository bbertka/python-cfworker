#!/usr/bin/python

from distutils.core import setup
setup(name='python-cfworker',
      version='1.1',
      py_modules=['cfworker'],
      install_requires=[
        "Flask",
      ],
      )
