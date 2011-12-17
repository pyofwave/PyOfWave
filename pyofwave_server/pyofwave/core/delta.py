"""
This file defines a simple observer system for responding to updates on waves.
"""
from multiprocessing import Pool

from pyofwave.conf import settings

def applyDelta(doc, delta):
    """Extend doc with delta."""
    # apply delta:d
    d = delta.get("{pyofwave.info/delta}d")
    if d == "delete":
        doc.getParent().remove(doc)
        return True
    elif d == "replace":
        doc.clear()

    # find element
    if doc.tag != delta.tag:
        doc = doc.find("./"+delta.tag)
    if not doc: return False

    # apply elements
    attrs = delta.attrib[:]
    del attrs["{pyofwave.info/delta}d"]
    for attr, val in attrs.items():
        doc.set(attr, val)
    
    # apply children
    for child in delta:
        if (not doc) or (not applyDelta(doc, child)):
            doc.append(child)

    return True

DeltaObserverPool = Pool(settings.DELTA_OBSERVER_PROCESSES,
                         None, settings.DELTA_OBSERVER_TIMEOUT)
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
