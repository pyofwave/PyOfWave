import unittest, stream

from pyofwave.protocols import WaveProtocol

class test_WaveProtocol(unittest):
    def setUp(self):
        from pyofwave.core.opdev import OperationNS as OpNS

        # Create operation
        NS = OpNS("http://pyofwave.info/test")

        @NS
        def op(*args, **kwargs):
            return NS.E.response(args, kwargs)

        # Create server
        import xmpp

        server = xmpp.TCPServer(xmpp.XMPPHandler(WaveProtocol)).bind(settings.DOMAIN, 5222)
        xmpp.start([server])
