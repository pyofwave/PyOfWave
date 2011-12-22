"""
Manage cursor location and blip body editing.
"""
MODULE_NS = "pyofwave.info/2012/dtd/document.dtd"

from lxml.builder import ElementMaker

from pyofwave.core.action import ActionBase
from pyofwave.core.action import action_register

E = ElementMaker(namespace=MODULE_NS)

@action_register
class Retain(ActionBase):
    """
    Move the cursor forward
    """
    NAMESPACE = MODULE_NS
    NAME = 'retain'
    
    def __init__(self, amount):
        self.amount = int(amount)

    def do(self, aDocument, cursor_position):
        future_cursor_position = cursor_position + self.amount
        assert(aDocument.length >= future_cursor_position)
        return future_cursor_position

    def to_xml_etree(self):
        return E.retain(amount=str(self.amount))

@action_register
class InsertCharacters(ActionBase):
    """
    Insert characters at the current cursor position
    """
    NAMESPACE = MODULE_NS
    NAME = 'insertCharacters'
    
    def __init__(self, characters):
        self.characters = characters

    def do(self, aDocument, cursor_position):
        # XXX: There may be room for speed improvment here
        aDocument.content = aDocument.content[:cursor_position] + self.characters + aDocument.content[cursor_position:]
        return cursor_position + len(self.characters)

    def to_xml_etree(self):
        return E.insertCharacters(characters=self.characters)
