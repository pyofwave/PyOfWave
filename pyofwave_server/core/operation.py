"""
Standard interface for connecting client protocols to the operation extensions. 
"""
from importlib import import_module

def performOperation(operation, kwargs):
   module, op = operation.split(".")
   opFunction = import_module('..operations.'+module, 'pygowave_server.core')
   try: opFunction = getattr(opFunction, op)
   except (AttributeError, evt): print evt
   return opFunction(**kwargs)
