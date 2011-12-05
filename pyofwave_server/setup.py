#!/usr/bin/env python
from setuptools import setup
from setuptools.command.test import test

class POWTestRunner(test):
    """
    Custom test runner that setup a fake env before starting
    """
    def run(self, *args, **kwargs):
        if self.distribution.install_requires:
            self.distribution.fetch_build_eggs(self.distribution.install_requires)
        if self.distribution.tests_require:
            self.distribution.fetch_build_eggs(self.distribution.tests_require)

        from runtests import runtests
        runtests(self.distribution.test_suite)

setup(name='PyOfWave',
      version='0.1',
      description='Open Source Wave server in Python',
      author=u'Alcinnz',
      author_email='alcinnz@github.com',
      url='https://github.com/pyofwave/PyOfWave',
      license='Mozilla Public License Version 2.0, Release Candidate 1',

      packages=['pyofwave',
                'pyofwave.protocols',
                'pyofwave.core',
                'pyofwave.operations',
                'pyofwave.storage'],

      cmdclass = {'test': POWTestRunner},
      tests_require = 'setuptools_trial',
      test_suite = 'pyofwave',

      scripts = ['bin/pyofwave_server']
      )
