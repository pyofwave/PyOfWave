import unittest

from lxml.builder import ElementMaker
import lxml.etree

from pyofwave.action.document import Retain, InsertCharacters
from pyofwave.core import operation, opdev
from pyofwave.core.document import Document
from pyofwave.core.operation import OperationBase, XMLOperation

ns = "pyofwave.info/2012/dtd/document.dtd"

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.E = ElementMaker(namespace=ns)

    def testPerformXMLOperation(self):
        # Write an operation in XML, inserting "go" at position 2
        xml = self.E.op(self.E.retain(amount="2"),
                        self.E.insertCharacters(characters="go"),
                        self.E.retain(amount="3")
                        )

        doc = Document(uri='nowhere', content='Hello')

        op = XMLOperation(lxml.etree.tostring(xml))
        op.do(doc)

        self.assertEqual(doc.content, "Hegollo")

        # Compare we can restitute the same XML from the Operation
        self.assertEqual(op.to_xml(), lxml.etree.tostring(xml))

    def testPerformOperation(self):
        class TestOperation(OperationBase):
            def scenario(self):
                yield Retain(2)
                yield InsertCharacters('go')
                yield Retain(3)

        doc = Document(uri='nowhere', content='Hello')

        op = TestOperation()
        op.do(doc)

        self.assertEqual(doc.content, "Hegollo")
        
        
class TestEventRegisty(unittest.TestCase):
    def setUp(self):
        self.E = ElementMaker(namespace=ns)

    def testEventRegisty(self):
        # Define a test context
        res = {"value": "FOO"}
        # Define a function used as event callback that will modify the context
        def misc(*args, **kwargs):
            res["value"] = "BAR"
        
        url = "wave://test@pyofwave.info/test"
        user="test@pyofwave.info"
        event_registry = operation.EventRegisty(user=user, 
                                                callback=misc)
        
        self.assertEqual(event_registry.user, user)

        # Create an operation for it's event.
        NS = opdev.OperationNS(ns)
        @NS
        def op(event, *args, **kwargs): pass

        # Test that event isn't triggered before register
        operation.performOperation(event_registry, self.E.op(href=url))
        self.assertEqual(res["value"],"FOO")

        # Trigger event
        event_registry.register(url, "{%s}op" % ns)
        operation.performOperation(event_registry, self.E.op(href=url))
        self.assertEqual(res["value"], "BAR")

        # test different URL
        res["value"] = "FOOBAR"
        operation.performOperation(event_registry, self.E.op(href="pyofwave.info/Firefly"))
        self.assertEqual(res["value"], "FOOBAR")

        # Unregister one event
        res["value"] = "BARFOO"
        event_registry.unregister(url, "{%s}op" % ns)
        operation.performOperation(event_registry, self.E.op(href=url))
        self.assertEqual(res["value"], "BARFOO")
        
        # Unregister all events
        event_registry.register(url, "{%s}op1" % ns)
        event_registry.register(url, "{%s}op2" % ns)
        event_registry.unregister(url, "*")
        

if __name__ == '__main__':
    unittest.main()
