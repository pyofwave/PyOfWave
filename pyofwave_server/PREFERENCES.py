"""
This file contains preferences and sets up objects for easily
setting up the PyGoWave for your server system.
"""
#datasource settings
from storage import files
## from protocols import federation

STORAGE_OBJECT = files.FileStorage("waves/", True)
CACHE_OBJECT = files.FileStorage("temp/", False)
## FEDERATION_OBJECT = federation.DataModel()

#setup datasource
from core import delta

STORAGE_OBJECT.successor = CACHE_OBJECT
## CACHE_OBJECT.successor = FEDERATION_OBJECT
delta.betaDeltaObservable.addObserver(STORAGE_OBJECT)
delta.betaDeltaObservable.addObserver(CACHE_OBJECT)
## delta.betaDeltaObservable.addObserver(FEDERATION_OBJECT)

#protocol settings
