"""
Standard interface for connecting client protocols to the operation extensions. 
"""
from importlib import import_module
import delta

# TODO: load all operations, implement.

def performOperation(events, tag):
    """ Execute a operation."""

class Events(object):
    """Keeps track of all the events a user registers to."""
    def __init__(self, user, callback):
        self.user = user
        self._sendEvent= callback
        self._events = {}

    def register(self, url, event):
        if not self._events.get(url): self._events[url] = []
        self._events[url].append(event)

    def unregister(self, url, event= "*"):
        if event == "*": del self._events[url]
        else: self._events[url].remove(event)

    @delta.alphaDeltaObservable.addObserver
    @static
    def applyDelta(doc, delta):
        """ Calculate and send events. """
