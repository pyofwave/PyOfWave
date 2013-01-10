"""
Contains standard interfaces for dataSources. 
"""
from zope import interface

class DataSource(interface.Interface):
    """
    Standard interface for a dataSource. 
    """
    def searchDocuments(user, url=None, xpath=None, range_=None, depth=-1, version=None, restore=False):
        """
        Returns an iterable of all documents that match the query.
        This query should be in the form found in the client protocol
        standard.
        """
        raise NotImplementedError

    def applyDelta(doc, delta):
        """
        Apply delta to doc and save.
        """
        raise NotImplementedError

		def getPermission(user, xml, ptype):
				"""
				Retrieve the permission *ptype* for user *user* and element *xml*.
				"""
				raise NotImplementedError
