"""
PyOfWave Server client protocol
Manages the receival of operations using the official Wave Simple Data HTTP Protocol.
This format uses JSON and is centred around method calls.

A few additional operations are supported, for optimisations.
"""
from twisted.internet.protocol import Protocol, Factory

from pyofwave.core.operation import performOperation
from pyofwave.operations import OperationError

import dictOps
import logging

class ClientProtocol(Protocol):
    """Interface for clients to call operations on the server."""
    def connectionMade(self):
        logging.debug("Connection made with client")
        self._mname = ""
        self._mmethod = ""
        self._mkwargs = {}
        
    def dataReceived(self, data):
        """Parses into a method call."""
        logging.debug("Data %s received by client" % data)
        firstChar = data[0]
        if firstChar == "#":
            self.call()
            self._mname = data[1:]
        elif firstChar == "[":
            if self._mmethod: self.call()
            self._mmethod = data[1:]
        elif self._mmethod and ":" in data:
            key, value = data.split(":")
            key = key.strip()
            value = value.strip()
            
            self._mkwargs[key] = value #TODO change key to a nested dictionary path.
            print self._mkwargs
        else:
            self.sendError(self._mname, OperationError(500, method=self._mmethod, keys=str(self._mkwargs)))
    
    def connectionLost(self, reason):
        """Calls the final operation."""
        self.call()
        
    def call(self):
        """Calls the method specified from the parsed request."""
        err = None
        response = {}
        if self._mmethod: 
            try:
                response = performOperation(self.transport.getPeer(), self._mmethod, self._mkwargs)
                self.sendResponse(self._mname, "RESPONSE.response", response)
            except(OperationError, err):
                self.sendError(self._mname, err)
        self._mname = ""
        self._mmethod = ""
        self._mkwargs = {}
        
    def sendResponse(self, name, method, kwargs):
        """Writes a response back."""
        kwargs = dictOps.flatten(kwargs)
        if name: self.transport.write("#"+name)
        self.transport.write("["+method)
        
        for key in kwargs.keys():
            self.transport.write(key + ":" + kwargs[key])
            
    def sendError(self, name, error):
        """Writes an ERROR response back."""
        self.sendResponse(name, "ERROR."+str(error.code), error.status)

class ClientProtocolFactory(Factory):
    protocol = ClientProtocol

factory = ClientProtocolFactory()
