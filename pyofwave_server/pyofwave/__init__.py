"""
Starts PyOfWave Server.
"""
import logging

logger = logging.getLogger("pyofwave.server")

def start(settings_mod=None):
    # Setup the configuration using a configuration file
    from conf import setup_environ
    setup_environ(settings_mod)
    
    # Setup Wave Protocol
    import xmpp
    from pyofwave.protocols import WaveProtocol
    server = xmpp.TCPServer(xmpp.XMPPHandler(WaveProtocol)).bind('127.0.0.1', 5222)
    xmpp.start([server])

