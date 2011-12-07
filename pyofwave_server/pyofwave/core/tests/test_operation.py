import unittest
from lxml.builder import ElementMaker

from pyofwave.core import operation, opdev

E = ElementMaker(namespace="pyofwave.info/test")

class TestOperations(unittest.TestCase):
    def testCreateOperation(self):
        NS = opdev.OperationNS("pyofwave.info/test")

        @NS
        def op(event, arg, tag, text, action):
            self.assertEqual(event, None)
            self.assertEqual(arg, "Hello")
            self.assertEqual(tag.tag, "{pyofwave.info/test}tag")
            self.assertEqual(text, "World")
            self.assertEqual(action, "SayHello")
            return NS.E.response("success", status = "400")
    
        operation.performOperation(None,
                                   E.op("Hello",
                                        E.tag(),
                                        "World",
                                        action="SayHello"))

    def testPerformOperation(self):
        res = operation.performOperation(None,
                                   E.op("Hello",
                                        E.tag(),
                                        "World",
                                        action="SayHello"))
        
        self.assertEqual(res.text, "success")
        self.assertEqual(res.get("status"), "400")
#
class TestEvents(unittest.TestCase):
    def testOperationEvents(self):
        #Define a test context
        res = {"value": "FOO"}
        #Define a function used as event callback that will modify the context
        def misc(*args, **kwargs):
            res["value"] = "BAR"
        
        url = "wave://test@pyofwave.info/test"
        user="test@pyofwave.info"
        evts = operation.Events(user=user, 
                                callback=misc)
        
        self.assertEqual(evts.user, user)

        # Create an operation for it's event.
        NS = opdev.OperationNS("pyofwave.info/test")
        @NS
        def op(event, *args, **kwargs): pass

        # Test that event isn't triggered before register
        operation.performOperation(evts, E.op(href=url))
        self.assertEqual(res["value"],"FOO")

        # Trigger event
        evts.register(url, "{pyofwave.info/test}op")
        operation.performOperation(evts, E.op(href=url))
        self.assertEqual(res["value"], "BAR")

        # test different URL
        res["value"] = "FOOBAR"
        operation.performOperation(evts, E.op(href="pyofwave.info/Firefly"))
        self.assertEqual(res["value"], "FOOBAR")

        # Unregister one event
        res["value"] = "BARFOO"
        evts.unregister(url, "{pyofwave.info/test}op")
        operation.performOperation(evts, E.op(href=url))
        self.assertEqual(res["value"], "BARFOO")
        
        # Unregister all events
        evts.register(url, "{pyofwave.info/test}op1")
        evts.register(url, "{pyofwave.info/test}op2")
        evts.unregister(url, "*")
        

if __name__ == '__main__':
    unittest.main()
