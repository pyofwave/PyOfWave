import socket

from twisted.trial import unittest
from twisted.test import proto_helpers

from ..client import ClientProtocolFactory

class TestClientProtocol(unittest.TestCase):
    def setUp(self):
        factory = ClientProtocolFactory()
        self.proto = factory.buildProtocol(('127.0.0.1', 0))
        self.tr = proto_helpers.StringTransport()
        self.proto.makeConnection(self.tr)

    def testCall(self):
        self.proto.dataReceived("#aname\r\n")
        self.proto.dataReceived("[tests.operation")
        self.proto.dataReceived("foo : bar")


    def testResponse(self):
        self.proto.dataReceived("#name1")
        self.proto.dataReceived("[tests.result")
        self.proto.dataReceived("foo:bar")
        self.proto.dataReceived("bar:foo")
        

        self.proto.dataReceived("#aname2")
        self.proto.dataReceived("[tests.nonexistant")
        self.proto.dataReceived("#name3")
        self.proto.dataReceived("[tests.error")
        


