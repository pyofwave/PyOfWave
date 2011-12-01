"""
Underlaying API for creating operations.
"""
from types import FunctionType

def _MetaClassFactory(function):
    class MetaClass(type):
        def __new__(meta, classname, bases, classDict):
            newClassDict = {}
            for attributeName, attribute in classDict.items():
                if type(attribute) == FunctionType:
                    attribute = function(attribute)

                newClassDict[attributeName] = attribute
            return  type.__new__(meta, classname, bases, newClassDict)
    return MetaClass

_OpMeta = _MetaClassFactory(classmethod)

class Operation(object):
    """Superclass for all operations, serves for identification, AOP via _OpMeta, and hooks. """
    ## __metaclass__ = _OpMeta

    def r(*args):
        pass

    def s(*args):
        pass

    q = ""
    
