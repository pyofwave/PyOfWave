"""
This file provides settings which you will need to provide for your system.
"""
# Logging
import logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

#URL settings
DOMAIN = ""

#Multiprocess settings
from multiprocessing import cpu_count
DELTA_OBSERVER_PROCESSES = cpu_count()
DELTA_OBSERVER_TIMEOUT = None


