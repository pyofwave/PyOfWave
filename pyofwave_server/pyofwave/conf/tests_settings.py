"""
A configuration file for running test cases
"""
import os, tempfile

from pyofwave.conf.global_settings import *

DOMAIN = "pyofwave.info"

LOGGING['handlers'] = {
        'tmpfile_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(tempfile.gettempdir(), 'pyofwave-testlog'),
            'formatter': 'verbose',
            }
        }

LOGGING['loggers']['pyofwave.server']['handlers'] = ['tmpfile_handler']

