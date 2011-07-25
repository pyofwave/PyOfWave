from twisted.internet import reactor
import protocols

reactor.listenTCP(9283, protocols.client.factory)
reactor.run()