"""The Wave Protocol

Loose XMPP wrapper around operations and their events. 
"""

import xmpp

class WaveProtocol(xmpp.ServerCore):

    def __init__(self, addr, stream):
        super(Pong, self).__init__(addr, stream)

    def is_stanza(self, name):
        return super(Pong, self).is_stanza(name)

    def handle_open_stream(self, attrs):
        return super(Pong, self).is_stanza(attrs)

    def handle_stanza(self, ping):
        super(Pong, self).handle_stanza(ping)

    def handle_close_stream(self):
        super(Pong, self).handle_close_stream()

    def close(self):
        super(Pong, self).close()

if __name__ == '__main__':
    server = xmpp.TCPServer(xmpp.XMPPHandler(WaveProtocol)).bind('127.0.0.1', 9000)
    xmpp.start([server])
