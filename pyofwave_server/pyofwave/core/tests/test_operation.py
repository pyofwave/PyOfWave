import unittest
from lxml.builder import ElementMaker

from pyofwave.core import operation, opdev

E = ElementMaker(namespace="pyofwave.info/test")

class TestOperations(unittest.TestCase):
    def testCreateOperation(self):
        NS = opdev.OperationNS("pyofwave.info/test")

        @NS
        def op(event, arg, tag, text, action):
            self.assertEqual(event, "AnEventToTrigger")
            self.assertEqual(arg, "Hello")
            self.assertEqual(tag.tag, "{pyofwave.info/test}tag")
            self.assertEqual(text, "World")
            self.assertEqual(action, "SayHello")
            return NS.E.response("success", status = "400")

    def testPerformOperation(self):
        res = operation.performOperation("AnEventToTrigger",
                                         E.op("Hello",
                                              E.tag(),
                                              "World",
                                              action="SayHello"))
        
        self.assertEqual(res.text, "success")
        self.assertEqual(res.get("status"), "400")
#
class TestEventRegisty(unittest.TestCase):
    def testEventRegisty(self):
        #Define a test context
        res = {"value": "FOO"}
        #Define a function used as event callback that will modify the context
        def misc(*args, **kwargs):
            res["value"] = "BAR"
        
        url = "wave://test@pyofwave.info/test"
        user="test@pyofwave.info"
        event_registry = operation.EventRegisty(user=user, 
                                                callback=misc)
        
        self.assertEqual(event_registry.user, user)

        # Create an operation for it's event.
        NS = opdev.OperationNS("pyofwave.info/test")
        @NS
        def op(event, *args, **kwargs): pass

        # Test that event isn't triggered before register
        operation.performOperation("AnEventToTrigger", E.op(href=url))
        self.assertEqual(res["value"],"FOO")

        # Trigger event
        event_registry.register(url, "{pyofwave.info/test}op")
        operation.performOperation("AnEventToTrigger", E.op(href=url))
        self.assertEqual(res["value"], "BAR")

        # test different URL
        res["value"] = "FOOBAR"
        operation.performOperation("AnEventToTrigger", E.op(href="pyofwave.info/Firefly"))
        self.assertEqual(res["value"], "FOOBAR")

        # Unregister one event
        res["value"] = "BARFOO"
        event_registry.unregister(url, "{pyofwave.info/test}op")
        operation.performOperation("AnEventToTrigger", E.op(href=url))
        self.assertEqual(res["value"], "BARFOO")
        
        # Unregister all events
        event_registry.register(url, "{pyofwave.info/test}op1")
        event_registry.register(url, "{pyofwave.info/test}op2")
        event_registry.unregister(url, "*")
        

if __name__ == '__main__':
    unittest.main()
