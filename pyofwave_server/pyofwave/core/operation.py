"""
Standard interface for connecting client protocols to the operation extensions. 
"""
from cStringIO import StringIO

import lxml.etree, lxml.builder
from zope import interface

from delta import DeltaObserverPool as dop
import opdev, delta

from pyofwave.utils.command import CommandInterface
from .action import ACTION_REGISTRY

class OperationBase(object):
    """
    An operation is a transformation that alters an entity (blip,
    document, ...) and is made of one or more Actions.
    """
    interface.implements(CommandInterface)
    
    def do(self, aDocument):
        """
        Perform the operation using the scenario
        """
        cursor_position = 0 # Cursor index in the document

        # Apply transformations using actions
        for action in self.scenario():
            cursor_position = action.do(aDocument=aDocument,
                                        cursor_position=cursor_position)

        assert(aDocument.length == cursor_position)
        
    def scenario(self):
        """
        Yield here the flow of Actions required to perform this
        operation.
        """
        raise NotImplementedError

    def to_xml_etree(self):
        """
        Turns an operation to an XML etree
        """
        # XXX This namespace shouldn't be hardcoded
        E = lxml.builder.ElementMaker(namespace="pyofwave.info/2012/dtd/document.dtd")
        xml_etree = E.op()
        for action in self.scenario():
            xml_etree.append(action.to_xml_etree())

        return xml_etree

    def to_xml(self):
        """
        Turns an operation to an XML stream
        """
        return lxml.etree.tostring(self.to_xml_etree())


class XMLOperation(OperationBase):
    """
    An Operation that reads its Actions from a XML stream.
    """
    def __init__(self, xml):
        self.xml = xml
    
    def scenario(self):
        root = lxml.etree.fromstring(self.xml)
        
        # XXX This namespace shouldn't be hardcoded
        operation_tag = root.find(".//{pyofwave.info/2012/dtd/document.dtd}op")

        for element in operation_tag.iterchildren():
            # Lookup the action name (using: "{NS}NAME") from the
            # action registry and yield the corresponding Action(s)
            if element.tag in ACTION_REGISTRY:
                kwargs = dict(element.items())
                try:
                    yield ACTION_REGISTRY[element.tag](**kwargs)
                except Exception, e:
                    raise OperationError("Wrong usage of '%s': %s" % (element.tag, e))

            else:
                raise OperationError("Unknown Action: %s" % element.tag)

# Perform operation
def _getChildren(tag):
    rep = [tag.text, ]
    for child in tag:
        rep.append(child)
        rep.append(child.tail)
    return rep

def performOperation(event, operation):
    """
    Execute an operation.
    """
    rep = opdev._receive[operation.tag](event, *_getChildren(operation), **operation.attrib)

    EventRegisty.notify(operation)
    return rep

# Events
def get(obj, prop, default = {}):
    if not obj.get(prop): 
        obj[prop] = default
    return obj[prop]

_handlers = {}

class EventRegisty(object):
    """
    Keeps track of all the events a user registers to.
    """
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
    def notify(operation, src=None):
        if src == None: 
            src = operation.get("href", operation.get("src", ""))

        for handler in _handlers.get(src, {}).get(operation.tag, []):
            ## FIXME : apply_async fails because handler seems to not be pickable 
            #dop.apply_async(handler, [operation])
            # XXX : amha, for the moment, a synchronous call is enought
            handler(operation)

    @delta.alphaDeltaObservable.addObserver
    @staticmethod
    def applyDelta(doc, delta):
        """ Calculate and send events. """

## -- Exceptions -- #
class OperationError(Exception):
    pass
