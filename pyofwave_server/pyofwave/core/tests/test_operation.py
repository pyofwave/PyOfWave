import unittest
from lxml.builder import ElementMaker

from pyofwave.core import operation, opdev

class TestOperations(unittest.TestCase):
    def testCreateOperation(self):
        NS = opdev.OperationNS("pyofwave.info/test")

        @NS
        def op(event, arg, tag, text, action):
            self.assertEqual(arg, "test")
            self.assertEqual(tag.tag, "{pyofwave.info/test}tag")
            self.assertEqual(text, "hello")
            self.assertEqual(action, "test")
            return NS.E.response("success", status = "400")

    def testPerformOperation(self):
        E = ElementMaker(namespace="pyofwave.info/test")
        res = operation.performOperation(None, 
            E.op("test", E.tag(), "hello", action="test"))
        self.assertEqual(res.text, "success")
        self.assertEqual(res.get("status"), "400")

if __name__ == '__main__':
    unittest.main()
