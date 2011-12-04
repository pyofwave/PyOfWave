#!/usr/bin/env python
from setuptools import setup

setup(name='PyOfWave',
      version='0.1',
      description='Open Source Wave server in Python',
      author=u'alcinnz (Adrian Cochrane)',
      author_email='alcinnz@eml.cc',
      url='https://github.com/pyofwave/PyOfWave',
      license='Mozilla Public License Version 2.0, Release Candidate 1',

      packages=['pyofwave',
                'pyofwave.protocols',
                'pyofwave.core',
                'pyofwave.operations',
                'pyofwave.storage'],

      test_suite = 'pyofwave',
      test_require = ['setuptools-trial'],

      scripts = ['bin/pyofwave_server']
      )
