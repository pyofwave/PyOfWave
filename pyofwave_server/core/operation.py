"""
Standard interface for connecting client protocols to the operation extensions. 
"""
## import delta
import opdev

# Load operations
def loadModules(path)
    import os, runpy
    rep = []

    listing = os.listdir(path)
    for mod in listing:
        rep.append(runpy.run_path(mod))

    return rep

def classesBySuper(mod, supr):
    rep = {}
    for key in mod.keys():
        if issubclass(mod[key], supr):
            rep[key] = mod[key]
    return rep

def loadOperations():
    mods = loadModules("../operations/")
    for mod in mods:
        ns = mod["NS"]
        ops = classesBySuper(mod, opdev.Operation)
        # compile list

_ops = loadOperations()

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
