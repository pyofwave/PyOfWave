"""
This file provides access to a simplified interface upon deltas and documents called "Tags".
"""
import delta, datasource

class Tag(object):
   """Simplified document interface."""
   def __init__(self, doc, item):
      #provide default values if parameters not passed.
      #Use a retain delta.
      self._doc = doc
      self._item = item
      self._delta = delta.deltaop()

      self._content = []
      #retrieve all direct children of item from doc as tags

   @property
   def _name(self): return self._item.name

   #itterable properties
   def __len__(self):
      return len(self._content)

   def __getitem__(self, index):
       return self._content[i]

   def __setitem__(self, index, value):
       #if value is a string, change it into a Text object
       self.content[i] = value

   #psuedo-properties
   def __getattr__(self, attr):
        return self._item.annotations[attr]

   def __setattr__(self, attr, value):
        #edit delta to set the attr
        pass

    def __delattr__(self, attr, value):
        #ensure delta is is a deltaBoundary
        #edit delta to delete the attr
        pass

   #delta creation
   def _contentdelta(self, deltas):
      deltas.append(self._delta)
      for child in self._content: child._contentdelta(deltas)

   def sendDelta(self):
      """Sends a beta delta."""
      #create delta
      delta.betaDeltaObservable.applyDelta(self._doc, delta)

class Text(object):
   """Represents textual changes. """
   def __init__(self, text):
      #create insertain delta
      pass

   def _contentdelta(self, deltas):
      deltas.appand(self.__delta)