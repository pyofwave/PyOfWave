"""
The Wave Protocol

Loose XMPP wrapper around operations and their events. 
"""

import xmpp
from pyofwave.core import opdev, operation

class WaveProtocol(xmpp.ServerCore):
    
    def __init__(self, stream):
	self.events = None
        super(WaveProtocol, self).__init__(stream, jid="serverjid") # XXX: hardcoded JID

    def is_stanza(self, name):
        return super(WaveProtocol, self).is_stanza(name) or name in opdev._receive.keys()

    def handle_stanza(self, el):
        super(WaveProtocol, self).handle_stanza(el)
        operation.handleOperation(self.events, el)

    def info_query(self, elem):
        # Same as in xmpp.Core, slight change in handling
        if not self.authJID:
            return self.stream_error('not-authorized')

        kind = elem.get('type')
        if kind == 'error':
            log.exception('Unhandled stanza error %r.', xml.tostring(elem))
            return

        if kind == 'result':
            name = self.iq_ident(elem)
        else:
            child = xml.child(elem)
            if child is None:
                log.exception('No child element: %r.' % xml.tostring(elem))
                return self.stanza_error(
                    elem, 'modify', 'not-acceptable',
                    'GET or SET must have a child element.'
                )
            name = '{jabber:client}iq/%s' % child.tag

        ret = operation.handleOperation(self.events, elem) #TODO: Handle errors

        if ret != None: self.iq('result', ret)

    def on_stream_authorized(self, usr):
        self.events = operation.EventRegistry(usr, self.write)
        super(WaveProtocol, self).on_stream_authorized(usr)

if __name__ == '__main__':
    from pyofwave.conf import settings

    server = xmpp.TCPServer(xmpp.XMPPHandler(WaveProtocol)).bind(settings.DOMAIN, 5222)
    xmpp.start([server])
