from zope import interface

from pyofwave.utils.command import CommandInterface

ACTION_REGISTRY = dict() # Temp place to store actions

def action_register(anActionClass):
    """
    Decorator to register a given class to the action registry
    """
    registry_entry_name = '{%s}%s' % (anActionClass.NAMESPACE, anActionClass.NAME)
    
    if registry_entry_name in ACTION_REGISTRY:
        # XXX: Refine exception
        raise Exception("%s already registered by %s" % (registry_entry_name, ACTION_REGISTRY[registry_entry_name]))
    
    ACTION_REGISTRY[registry_entry_name] = anActionClass

    return anActionClass

class ActionBase(object):
    """
    Base Action for any Action that can be compouned to build an
    Operation
    """
    interface.implements(CommandInterface)

    NAMESPACE = 'OVERRIDE_ME_NS'
    NAME = 'OVERRIDE_ME_NAME'
    
    def do(self, aDocument, cursor_position):
        """
        Perform the action on the given Document, at the given
        position.
        """
        raise NotImplementedError

    def to_xml_etree(self):
        """
        Turns an operation to an XML etree representation
        """
        raise NotImplementedError



