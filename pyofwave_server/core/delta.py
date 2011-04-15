"""
This file defines a simple observer system for responding to updates on waves.
"""
from multiprocessing import Pool
from .. import SETTINGS

class ImproperDelta(Exception):
    """If this is recieved, you should reload the delta."""
    
class Delta(object):
    """Represents a change to a XML-like document."""
    def __init__(self, *ops):
        self.ops = ops

    def applyToDoc(self, doc):
        """Use to apply changes described to a document."""
        from datasource import Document
        
        rep = Document()
        doc.cursor = 0
        for op in self.ops: ops.apply(doc, rep)
        return rep

class Operation(object):
    """A single change in a delta. """
    def __init__(self, operation, *args):
        import deltaop

        try: self.operation = getattr(deltaop, operation)
        except (AttributeError): raise ImproperDelta
        self.args = args

    def applyToDoc(doc, new):
        try: self.operation(doc, new, *self.args)
        except (ArgumentError): raise ImproperDelta

class Message(object):
    """A message version. """
    def __init__(self, message, version):
        self.message = message
        self.version = version

DeltaObserverPool = Pool(SETTINGS.DELTA_OBSERVER_PROCESSES,
                         None, None, SETTINGS.DELTA_OBSERVER_TIMEOUT)
class DeltaObservable(object):
    """The subject in the observer pattern."""
    def __init__(self):
        self.observers = []
        
    def applyDelta(self, doc, delta):
        """Notifiers observers. """
        for observer in self.observers: DeltaObserverPool.apply_async(observer, (doc, delta))

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

#central objects
alphaDeltaObservable = DeltaObservable() #for operations in permanent memory
betaDeltaObservable = DeltaObservable()  #for operations before they arrive at permanent memory
