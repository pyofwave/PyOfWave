"""
This file provides default settings you can customize through a
user-defined 'settings.py'
"""
## URL settings
DOMAIN = ""

## Multiprocess settings
from multiprocessing import cpu_count
DELTA_OBSERVER_PROCESSES = cpu_count()
DELTA_OBSERVER_TIMEOUT = None

## BACKING STORES (DATA SOURCES)
DATASOURCE_STORAGE = 'pyofwave.storage.backends.files'

FILESTORAGE_PATH = "waves/"
FILESTORAGE_CHECKDOMAIN = True

## LOGGING
LOGGING_CONFIG = 'logging.config.dictConfig'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            },
        },
    'loggers': {
        'pyofwave.server': {
            'handlers': ['console_debug'],
            'level': 'DEBUG',
            'propagate': False,
            },
        },
    'formatters': {
        'verbose': {
            #TODO : display logger name
            'format': '%(asctime)s - %(levelname)s - %(message)s',
            },
        },
    }
