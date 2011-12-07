"""
Standard interface for connecting client protocols to the operation extensions. 
"""
## import delta
import opdev

# Perform operation
def _getChildren(tag):
    rep = [tag.text, ]
    for child in tag:
        rep.append(child)
        rep.append(child.tail)
    return rep

def performOperation(events, operation):
    """ Execute a operation."""
    rep = opdev._receive[operation.tag](events, *_getChildren(operation), **operation.attrib)

    Events.trigger(operation)
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

    def _handlers(self, url, operation):
        # XXX : Why is it a list that is associated to an operation ?
        # XXX : Is it possible to assign several callback to an operation ?
        return get(get(_handlers, url), operation, [])

    def register(self, url, operation):
        # XXX: All registered operations will have the save callback 
        self._handlers(url, operation).append(self._callback)

    def unregister(self, url, operation="*"):
        url_handlers = get(_handlers, url)
        if operation == "*": 
            for operation in url_handlers.keys():
                operation_callback = self._handlers(url, operation)
                if self._callback in operation_callback:
                    operation_callback.remove(self._callback)
        else: 
            self._handlers(url, operation).remove(self._callback)
    
    @staticmethod
    def trigger(operation, src = None):
        if src == None: 
            src = operation.get("href", operation.get("src", ""))

        for callback in _handlers.get(src, {}).get(operation.tag, []):
            callback(operation)

##    @delta.alphaDeltaObservable.addObserver
##    @staticmethod
##    def applyDelta(doc, delta):
##        """ Calculate and send events. """
