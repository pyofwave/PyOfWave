"""
This file contains preferences and sets up objects for easily
setting up the PyGoWave for your server system.
"""
#datasource settings
from pyofwave.storage import files

STORAGE_OBJECT = files.FileStorage("waves/", True)
