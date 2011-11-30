"""
Underlaying API for creating operations.
"""
NS = "" # required in this directory, here so scripts can import

def _MetaClassFactory(function):
    class MetaClass(type):
        def __new__(meta, classname, bases, classDict):
            for attributeName, attribute in classDict.items():
                if type(attribute) == FunctionType:
                    attribute = function(attribute)

                newClassDict[attributeName] = attribute
            return  type.__new__(meta, classname, bases, classDict)
    return MetaClass

_OpMeta = _MetaClassFactory(classmethod)

class Operation(object):
    """Superclass for all operations, serves for identification, AOP via _OpMeta, and hooks. """
    __meta__ = _OpMeta

    def r(*args):
        pass

    def s(*args):
        pass

    q = ""
    
