"""The Wave Protocol

Loose XMPP wrapper around operations and their events. 
"""

import xmpp
from pyofwave.core import opdev, operation

class WaveProtocol(xmpp.ServerCore):

    def __init__(self, addr, stream):
        super(WaveProtocol, self).__init__(addr, stream)

    def is_stanza(self, name):
        supr = super(WaveProtocol, self).is_stanza(name) or name in opdev._receive.keys()

    def handle_stanza(self, el):
        super(WaveProtocol, self).handle_stanza(el)
        operation.handleOperation(None, el)

if __name__ == '__main__':
    server = xmpp.TCPServer(xmpp.XMPPHandler(WaveProtocol)).bind('127.0.0.1', 5222)
    xmpp.start([server])
