import unittest

from pyofwave.action.document import Retain, InsertCharacters
from pyofwave.core.document import Document
from pyofwave.core.operation import OperationBase

class TestDocumentActions(unittest.TestCase):
    def testRetain(self):
        class TestOperation(OperationBase):
            def scenario(self):
                yield Retain(1)
                yield Retain(2)
                yield Retain(2)

        doc = Document(uri='nowhere', content='Hello')

        op = TestOperation()
        op.do(doc)

        self.assertEqual(doc.content, "Hello")

    def testInsertCharacter(self):
        class TestOperation(OperationBase):
            def scenario(self):
                yield Retain(2)
                yield InsertCharacters('go')
                yield Retain(3)

        doc = Document(uri='nowhere', content='Hello')

        op = TestOperation()
        op.do(doc)

        self.assertEqual(doc.content, "Hegollo")






