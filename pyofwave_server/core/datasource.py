"""
Contains standard interfaces for dataSources. 
"""
from .. import SETTINGS
import delta
from zope import interface

class DataSource(interface.Interface):
   """Standard interface for a dataSource. """
   def newDocument(doc):
      """generate a new document."""

   def getDocument(doc):
      """returns the specified document."""

   def getDocumentVersion(doc, start, end, limit):
      """Returns the delta for the specified versions. """
   successor = interface.Attribute('DataSource')

class Document(object):
   """Stores a series of items representing start tags, end tags, and text. """
   def __init__(self, participants, *items):
      """Initializes document as a collection of passed items. """
      self.items = [item for item in items]
      self.participants = participants

      #transform properties
      self.cursor = -1
      self.annotations = {}

class Item(object):
   """Stores a name, type, and annotations."""
   def __init__(self, typeI, name, **annotations):
      self.type = typeI
      self.name = name
      self.annotations = annotations
      self.end = None

   TYPE_START_TAG = 0
   TYPE_END_TAG = 1
   TYPE_TEXT = 2
