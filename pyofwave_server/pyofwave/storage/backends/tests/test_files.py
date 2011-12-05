import unittest
import tempfile, os

from pyofwave.storage.backends.files import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage(path=os.path.join(tempfile.gettempdir(), 'pyofwave-fs-test'),
                                   checkDomain=True)

    def testNewDocument(self):
        assert(False)

    def testGetDocument(self):
        assert(False)

    def testGetDocumentVersion(self):
        assert(False)

    def testFilename(self):
        assert(False)
    
    def testApplyDelta(self):
        assert(False)



