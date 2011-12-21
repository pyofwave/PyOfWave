import unittest
from lxml.builder import ElementMaker

from pyofwave.core import operation, opdev
from pyofwave.core.action import Retain, InsertCharacters


from pyofwave.core.document import Document
from pyofwave.core.operation import OperationBase

ns = "pyofwave.info/test"

class TestActions(unittest.TestCase):
    def testInsertCharacters(self):
        class TestOperation(OperationBase):
            def scenario(self):
                yield Retain(2)
                yield InsertCharacters('go')
                yield Retain(3)

        doc = Document(uri='nowhere', content='Hello')

        op = TestOperation()
        op.do(doc)

        self.assertEqual(doc.content, "Hegollo")

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.E = ElementMaker(namespace=ns)

    def testCreateOperation(self):
        NS = opdev.OperationNS(ns, events=True)

        @NS
        def op(event, arg, tag, text, action):
            self.assertEqual(event, "AnEventToTrigger")
            self.assertEqual(arg, "Hello")
            self.assertEqual(tag.tag, "{%s}tag" % ns)
            self.assertEqual(text, "World")
            self.assertEqual(action, "SayHello")
            return NS.E.response("success", status="400")

    def testCreateOperationFromXML(self):
        class TestXMLOperation(OperationBase):
            def __init__(self, xml):
                self.xml = xml
                
            def scenario(self):
                import lxml.etree
                from cStringIO import StringIO

                xml_file = StringIO(self.xml)

                for event, element in lxml.etree.iterparse(xml_file):
                    #if eleemprint("%5s, %4s, %s" % (event, element.tag, element.text))
                    if element.tag in ("select", "text"):
                        action = {"select": Retain,
                                  "text": InsertCharacters}[element.tag]

                        yield action(element.items())

        # Write some xml
        xml = self.E.op(self.E.select(href="about:blank",
                                      range="10",
                                      version="2"),
                        self.E.text("go"),
                        )


        doc = Document(uri='nowhere', content='Hello')

        import lxml.etree
        op = TestXMLOperation(lxml.etree.tostring(xml))
        op.do(doc)

        self.assertEqual(doc.content, "Hegollo")


        # print lxml.etree.tostring(xml)

    def testPerformOperation(self):
        res = operation.performOperation("AnEventToTrigger",
                                         self.E.op("Hello",
                                                   self.E.tag(),
                                                   "World",
                                                   action="SayHello")
                                         )
        
        self.assertEqual(res.text, "success")
        self.assertEqual(res.get("status"), "400")



        
        
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
