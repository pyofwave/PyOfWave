from ..operation import performOperation
from lxml.builder import ElementMaker

E = ElementMaker(namespace="pyofwave.info/test")
print performOperation(None, E.op("test", action="test"))
