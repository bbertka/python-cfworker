#!/usr/bin/python

from distutils.core import setup
setup(name='python-cfworker',
      version='1.4.0',
      py_modules=['cfworker'],
      install_requires=[
        "Flask",
      ],
      download_url = 'https://pypi.python.org/pypi/python-cfworker',
      author = 'Ben Bertka',
      author_email = 'bbertka@gmail.com',
      maintainer = 'Ben Bertka',
      maintainer_email = 'bbertka@gmail.com',
      url = 'https://github.com/bbertka/python-cfworker',
      summary = 'CFWorker: A Module to simplify Worker App deployment',
      license = 'Apache',
      description = 'This module makes it easier to deploy Python workers by wrapping Flask and multiprocess functionality into a single module. When instanced, your app will be serving http via Flask, as well as performing work.',
      keywords = ['cloudfoundry', 'flask', 'worker', 'python'],
      classifiers = [],
)
