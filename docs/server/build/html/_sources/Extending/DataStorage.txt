Data Storage Extensions
*****************************

If the existing data storage options don't suit you, you can easily add your own.

1. Preparing the Datasource
====================

The datasource needs to be set up to be able to store PyOfWave documents before you integrate it. To do this, setup your datasource to store under a name:

- A sequence of "items"

   - Each item must have some text; a type of either open, close, or text; 
   and a map of annotations.

- A map of tags, for each user and global, to a sequence of values.

2. Implement the Adaptor
===================

Add a new Python file in datasource (doesn't really matter if you put it there) and code::

   from ..core import datasource
   from zope.interface import implements

   class MyDataStorage(object):
      implements(datasource.Datasource)

      def newDocument(self, doc):
         """Create a new Document in datastorage."""

      def getDocument(self, doc):
         """Retrieve document named doc (which includes the domain) and 
            return as a Document object."""

      def getDocumentVersion(self, doc, start, end, limit):
         """Retrieve specified deltas for the document and 
            return as Delta objects."""

      def searchDocuments(self, user, search):
         """Retrieve a list of document names which match the tags 
            provided by setTags."""

      def setTags(self, doc, user, **tags):
         """Set the tags to the document/user pair to be searched upon."""

      def applyDelta(self, doc, delta):
         """Save the delta to the user."""

Implement the methods. If it is irrelevant for this object, call the same method (apart from applyDelta) on ``self.successor``.

3. Integrate the Adaptor
=================

Open :file:`PREFERENCES.py` and import your file. Then set one of the storage options (either :py:data:`CACHE_OBJECT` and/or :py:data:`STORAGE_OBJECT`) to an instance of your adaptor.

Also ensure that the applyDelta method is set to observe betaDeltaObservable, ``betaDeltaObservable.addObserver(STORAGE_OBJECT.applyDelta)`` and that it has a value for the successor property.