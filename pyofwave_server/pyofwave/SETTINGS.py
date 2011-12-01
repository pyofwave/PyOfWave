"""
This file provides settings which you will need to provide for your system.
"""
#URL settings
DOMAIN = ""

#Multiprocess settings
from multiprocessing import cpu_count
DELTA_OBSERVER_PROCESSES = cpu_count()
DELTA_OBSERVER_TIMEOUT = None
