"""
Central resource for all HTTP protocols.
"""
from twisted.web.resource import Resource
from twisted.web.server import Site
import logging

root = Resource()

sys = Resource()
root.putChild("sys", sys)
client = Resource()
root.putChild("client", client)
auth = Resource()
root.putChild("auth", auth)

logging.debug("Create HTTP Site with sys, client and auth resources")
factory = Site(root)
