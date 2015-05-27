#!/usr/bin/python

from distutils.core import setup
setup(name='python-cfworker',
      version='1.2',
      py_modules=['cfworker'],
      install_requires=[
        "Flask",
      ],
      )
