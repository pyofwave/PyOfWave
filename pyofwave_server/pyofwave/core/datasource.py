"""
Contains standard interfaces for dataSources. 
"""
from zope import interface

class DataSource(interface.Interface):
    """
    Standard interface for a dataSource. 
    """
    def newDocument(doc):
        """
        generate a new document.
        """
        raise NotImplementedError

    def getDocument(doc):
        """
        returns the specified document.
        """
        raise NotImplementedError

    def getDocumentVersion(doc, start, end, limit):
        """
        Returns the delta for the specified versions. 
        """
        raise NotImplementedError

    def searchDocuments(user, query):
        """
        Returns an iterable of all documents that match the query.
        This query should be in the form found in the client protocol
        standard.
        """
        raise NotImplementedError

    def setTags(doc, user, **tags):
        """
        Apply the tags to the document/user combination to be searched.
        """
        raise NotImplementedError

    def applyDelta(doc, delta):
        """
        Apply delta to doc and save.
        """
        raise NotImplementedError

