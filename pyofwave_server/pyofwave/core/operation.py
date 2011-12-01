"""
Standard interface for connecting client protocols to the operation extensions. 
"""
## import delta
import opdev, delta
from lxml.builder import ElementMaker

# Load operations
def _loadModules(path):
    import os, runpy
    path = os.path.join(os.path.dirname(__file__), path)
    rep = []

    listing = os.listdir(path)
    for mod in listing:
        if ".py" in mod and ".pyc" not in mod:
            rep.append(runpy.run_path(os.path.join(path, mod), {
                "Operation" : opdev.Operation,
                "E" : lambda ns: ElementMaker(namespace = ns),
                "delta" : delta}))
    return rep

def _classesBySuper(mod, supr):
    import inspect
    
    rep = {}
    for key, val in mod.items():
        if inspect.isclass(val) and issubclass(val, supr):
            rep[key] = val
    return rep

def _loadOperations():
    mods = _loadModules("../operations/")
    rep = {}
    
    for mod in mods:
        ns = mod["NS"]
        ops = _classesBySuper(mod, opdev.Operation)

        for key in ops.keys():
            rep["{"+ns+"}"+key] = ops[key]

    return rep

_ops = _loadOperations()

# Perform operation
def performOperation(events, tag):
    """ Execute a operation."""
    return _ops[tag.tag].r(events, *list(tag), **tag.attrib)

# Events
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
    @staticmethod
    def applyDelta(doc, delta):
        """ Calculate and send events. """
