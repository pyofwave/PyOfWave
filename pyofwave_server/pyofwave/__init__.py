"""
Starts PyOfWave Server.
"""
import logging

logger = logging.getLogger("pyofwave.server")

def start(settings_mod=None):
    # Setup the configuration using a configuration file
    from conf import setup_environ
    setup_environ(settings_mod)
    
    # TODO: Once we have XMPP/BOSH service, start them here. (Ideally, load all protocols from settings)

