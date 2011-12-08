"""
Standard interface for connecting client protocols to the operation extensions. 
"""
from delta import DeltaObserverPool as dop
import opdev, delta

# Perform operation
def _getChildren(tag):
    rep = [tag.text, ]
    for child in tag:
        rep.append(child)
        rep.append(child.tail)
    return rep

def performOperation(events, op):
    """ Execute a operation."""
    rep = opdev._receive[op.tag](events, *_getChildren(op), **op.attrib)

    Events.trigger(op)
    return rep

# Events
def get(obj, prop, default = {}):
    if not obj.get(prop): obj[prop] = default
    return obj[prop]

_handlers = {}

class Events(object):
    """Keeps track of all the events a user registers to."""
    def __init__(self, user, callback):
        self.user = user
        self._callback = callback

    def _handlers(self, url, op):
        return get(get(_handlers, url), op, [])

    def register(self, url, op):
        self._handlers(url, op).append(self._callback)

    def unregister(self, url, op = "*"):
        if op == "*": 
            for evt in get(_handlers, url).values():
                evt.remove(handler)
        else: self._handlers(url, op).remove(self._callback)

    @staticmethod
    def trigger(op, src = None):
        if src == None: src = op.get("href", op.get("src", ""))

        for handler in _handlers.get(src, {}).get(op.tag, []):
            dop.apply_async(handler, (tag))

    @delta.alphaDeltaObservable.addObserver
    @staticmethod
    def applyDelta(doc, delta):
        """ Calculate and send events. """
