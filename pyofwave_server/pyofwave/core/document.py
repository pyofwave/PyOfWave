import pyofwave.storage

class Document(object):
    """
    A document is piece of XML linked to an URI, that can be stored
    into a datastore and on which operations can be applied to
    transform it.
    """
    def __init__(self, uri, content="", aDataStore=None):
        self.uri = uri
        self.content = content
        self.datastore = aDataStore

    @classmethod
    def load(klass, uri, aDataStore=None):
        """
        Loads a document from a given datastore, or from the
        configured default one.
        """
        if not aDataStore:
            aDataStore = pyofwave.storage.datastore

        return aDataStore.get_document(uri)
        

    def save(self, aDataStore=None):
        """
        Persist a Document into the given DataStore, or the one where
        the document comes from.
        """
        if not aDataStore:
            if self.datastore:
                aDataStore = self.datastore
            else:
                # XXX: Use a real exception
                raise "This document is not linked to a datastore or none was specified"
            
        return aDataStore.save_document(self)
                
    @property
    def length(self):
        """
        The length of the xml content
        """
        return len(self.content)

    def __str__(self):
        return "%s: %s" % (self.uri, self.content)





