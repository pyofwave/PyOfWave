"""
Central resource for all HTTP protocols.
"""
from twisted.web.resource import Resource
from twisted.web.server import Site
root = Resource()

sys = Resource()
root.putChild("sys", sys)
client = Resource()
root.putChild("client", client)
auth = Resource()
root.putChild("auth", auth)

factory = Site(root)
