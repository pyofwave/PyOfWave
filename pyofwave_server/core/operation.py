"""
Standard interface for connecting client protocols to the operation extensions. 
"""
from importlib import import_module
from ..operations import OperationError

def performOperation(ip, operation, kwargs):
    module, op = operation.split(".")
    opFunction = import_module('..operations.'+module, 'pyofwave_server.core')
##    try: 
    rep = getattr(opFunction, op)(ip, **kwargs)
##    except (AttributeError, TypeError): raise OperationError(404)
    return rep
