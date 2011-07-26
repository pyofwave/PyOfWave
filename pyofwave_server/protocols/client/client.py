"""
PyOfWave Server client protocol
Manages the receival of operations using the official Wave Simple Data HTTP Protocol.
This format uses JSON and is centred around method calls.

A few additional operations are supported, for optimisations.
"""
from twisted.internet.protocol import Protocol, Factory
from ...core.operation import performOperation

class ClientProtocol(Protocol):
    """Interface for clients to call operations on the server."""
    def connectionMade(self):
        self._mname = ""
        self._mmethod = ""
        self._mkwargs = {}
        
    def dataReceived(self, data):
        """Parses into a method call."""
        firstChar = data[0]
        if firstChar == "#":
            self.call()
            self._mname = data[1:]
        elif firstChar == "[":
            if self._mkwargs: self.call()
            self._mmethod = data[1:]
        elif self._mmethod and ":" in data:
            key, value = data.split(":")
            key = key.strip()
            value = value.strip()
            
            self._mkwargs[key] = value #TODO change key to a nested dictionary path.
            print self._mkwargs
        else:
            pass #TODO send error.500 response
    
    def connectionLost(self, reason):
        """Calls the final operation."""
        self.call()
        
    def call(self):
        """Calls the method specified from the parsed request."""
        if self._mmethod: 
            performOperation(self.transport.getPeer(), self._mmethod, self._mkwargs)
        self._mname = ""
        self._mmethod = ""
        self._mkwargs = {}
        
factory = Factory()
factory.protocol = ClientProtocol