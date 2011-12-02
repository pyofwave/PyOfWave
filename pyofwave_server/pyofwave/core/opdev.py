"""
Underlaying API for creating operations.
"""
from lxml.builder import ElementMaker

_receive = {}
_shouldSend = {}

class OperationNS(object):
	""" Plugin interface for operations."""
	def __init__(self, namespace):
		self.namespace = namespace
		self.E = ElementMaker(namespace = namespace)

	def receive(self, callback):
		"""Register callback to be called for 
			"{%s}%s" % self.namespace, callback.__name__."""
		return self._register(_receive, callback.__name__, callback)
		
	def shouldSend(self, xQuery):
		"""Determines if a delta translates to this event (tag). """
		S = None
		cb = None
		def inner(fn):
			name = fn.__name__
			S = getattr(self.E, name)
			cb = fn

			self._register(_shouldSend, name, callback)
			return inner

		def callback(doc, delta):
			""" Checks xQuery then cb. """

		return inner

	def __call__(self, arg):
		if callable(arg): return self.receive(arg)
		else: return self.shouldSend(arg)

	def _register(self, dikt, name, value):
		dikt["{"+self.namespace+"}"+name] = value
