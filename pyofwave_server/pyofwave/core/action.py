from zope import interface

from pyofwave.utils.command import CommandInterface

class ActionBase(object):
    interface.implements(CommandInterface)
    
    def do(self, aDocument, cursor_position):
        raise NotImplementedError

class Retain(ActionBase):
    def __init__(self, amount):
        self.amount = amount

    def do(self, aDocument, cursor_position):
        future_cursor_position = cursor_position + self.amount
        assert(aDocument.length >= future_cursor_position)
        return future_cursor_position
        
class InsertCharacters(ActionBase):
    def __init__(self, characters):
        self.characters = characters

    def do(self, aDocument, cursor_position):
        # XXX: There may be room for speed improvment here
        aDocument.content = aDocument.content[:cursor_position] + self.characters + aDocument.content[cursor_position:]
        return cursor_position + len(self.characters)
        
class Annotate(object):
    def do(self):
        raise NotImplementedError



