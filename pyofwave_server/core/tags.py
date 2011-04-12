"""
This file provides access to a simplified interface upon deltas and documents called "Tags".
"""
import delta, datasource

class Tag(object):
   """Simplified document interface."""
   def __init__(self, item):
      self._item = item
      self._delta = Delta()

   @property
   def _name(self): return self._item.name

   #itterable properties
   def __len__(self):
      pass

   def __getitem__(self, index):
       pass

   def __setitem__(self, index, value):
       pass

   #psuedo-properties
   def __getattr__(self, attr):
        pass

   def __setattr__(self, attr, value):
        pass

    def __delattr__(self, attr, value):
        pass

   #delta creation
   @property
   def _contentdelta(self):
      pass

   def sendDelta(self):
      """Sends a beta delta."""

class Text(object):
   """Represents textual changes. """

class Retain(object):
   """Represents unchanged content. """