"""
Standard interface for connecting client protocols to the operation extensions. 
"""
## import delta
import opdev, delta

# Perform operation
def _getChildren(tag):
	rep = [tag.text,]
	for child in tag:
		rep.append(child)
		rep.append(child.tail)
	return rep

def performOperation(events, tag):
    """ Execute a operation."""
    return opdev._receive[tag.tag](events, *_getChildren(tag), **tag.attrib)

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
