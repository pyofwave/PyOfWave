#!/usr/bin/env python

import sys

from twisted.trial.runner import TrialRunner, TestLoader
from twisted.trial.reporter import TreeReporter

from pyofwave.conf import settings
 
# If nothing has been configure, setup an environement before running
# the tests
if not settings.configured:
    from pyofwave.conf import setup_environ
    import pyofwave.conf.tests_settings
    setup_environ(pyofwave.conf.tests_settings,
                  'pyofwave.conf.tests_settings')
 
def runtests(root_dir='pyofwave'):
    runner = TrialRunner(TreeReporter)
    loader = TestLoader()
    failures = runner.run(loader.loadByName(root_dir, recurse=True))
    sys.exit(failures)
 
if __name__ == '__main__':
    if len(sys.argv) == 2:
        dir=sys.argv[1]
    else:
        dir='pyofwave'
    runtests(root_dir=dir)





