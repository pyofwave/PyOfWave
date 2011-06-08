"""
Central resource for all HTTP protocols.
"""

root = Resource()

sys = Resource()
root.put("sys", sys)
client = Resource()
root.put("client", client)
auth = Resource()
root.put("auth", auth)

factory = Site(root)
