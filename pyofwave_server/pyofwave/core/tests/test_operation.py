import unittest

from lxml.builder import ElementMaker

from pyofwave.core.operation import performOperation

class TestOperations(unittest.TestCase):
    def testPerformOperation(self):
        E = ElementMaker(namespace="pyofwave.info/test")
        print performOperation(None, E.op("test", action="test"))
