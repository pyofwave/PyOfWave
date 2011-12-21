class Document(object):
    """
    A document is piece of XML linked to an URI, that can be stored
    into a datastore and on which operations can be applied to
    transform it.
    """
    def __init__(self, uri, content=""):
        self.uri = uri
        self.content = content

    @property
    def length(self):
        return len(self.content)

    def __str__(self):
        return "%s: %s" % (self.uri, self.content)





