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

def performOperation(events, tag):
    """ Execute a operation."""
    rep = opdev._receive[tag.tag](events, *_getChildren(tag), **tag.attrib)

    Events.trigger(tag)
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

    def _handlers(self, url, event):
        return get(get(_handlers, url), event, [])

    def register(self, url, event):
        self._handlers(url, event).append(self._callback)

    def unregister(self, url, event= "*"):
        if event == "*": 
            for evt in get(_handlers, url).values():
                evt.remove(handler)
        else: self._handlers(url, event).remove(self._callback)

    @staticmethod
    def trigger(tag, src = None):
        if src == None: src = tag.get("href", tag.get("src", ""))

        for handler in _handlers.get(src, {}).get(tag.tag, []):
            dop.apply_async(handler, (tag))

    @delta.alphaDeltaObservable.addObserver
    @staticmethod
    def applyDelta(doc, delta):
        """ Calculate and send events. """
