"""
Contains standard interfaces for dataSources. 
"""
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

   def searchDocuments(user, query):
      """Returns an iterable of all documents that match the query.
         This query  should be in the form found in the client protocol standard."""

   def setTags(doc, user, **tags):
      """Apply the tags to the document/user combination to be searched."""

   def applyDelta(doc, delta):
      """Apply delta to doc and save."""

   successor = interface.Attribute('DataSource')

class Document(object):
   """Stores a series of items representing start tags, end tags, and text. """
   def __init__(self, *items, **tags):
      """Initializes document as a collection of passed items. """
      self.items = [item for item in items]

      #transform properties
      self.cursor = -1
      self.annotations = {}

class Item(object):
   """Stores a name, type, and annotations."""
   def __init__(self, typeI, name, **annotations):
      self.type = typeI
      self.name = name
      self.annotations = annotations

   TYPE_START_TAG = 0
   TYPE_END_TAG = 1
   TYPE_TEXT = 2
