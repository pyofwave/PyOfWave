"""
This file defines a simple observer system for responding to updates on waves.
"""
from multiprocessing import Pool
from .. import SETTINGS
import deltaop

class ImproperDelta(Exception):
    """If this is recieved, you should reload the delta."""
    
class Delta(object):
    """Represents a change to a XML-like document."""
    def __init__(self, *ops):
        self.ops = ops

    def applyToDoc(self, doc, mod=deltaop):
        """Use to apply changes described to a document doc."""
        from datasource import Document
        
        if isinstance(doc, Document): rep = Document()
        else: rep = doc
        
        doc.cursor = 0
        for op in self.ops: op.applyToDoc(mod, doc, rep)
        return rep

class Operation(object):
    """A single change in a delta. """
    def __init__(self, operation, *args):
        self.operation = operation
        self.args = args

    def applyToDoc(self, mod, doc, new):
        """Applies the particulor operation to a document new based on data in doc."""
        ##try:
        op = getattr(mod, self.operation)
        op(doc, new, *self.args)
        ##except (AttributeError, TypeError): raise ImproperDelta

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
        """Call to be called whenever a new delta is sent in through the DeltaObservable.
            You will be called in a seperate process than the main server, so as to avoid overhead in handling requests."""
        self.observers.append(observer)

    def removeObserver(self, observer):
        """Call to remove a function from being called by applyDelta."""
        self.observers.remove(observer)

#central objects
alphaDeltaObservable = DeltaObservable() #for operations in permanent memory
betaDeltaObservable = DeltaObservable()  #for operations before they arrive at permanent memory
