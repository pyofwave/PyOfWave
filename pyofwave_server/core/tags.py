"""
This file provides access to a simplified interface upon deltas and documents called "Tags".
"""
import delta, datasource

annotationOffsets = {
   "updateAttributes" : 1,
   "elementStart" : 1,
   "annotationsBoundary" : 1
}
blankArgs = {
   'retain' : (0,),
   'updateAttributes' : ({}, {}),
   'replaceAttributes' : ({},),
   'charactors' : ('',),
   'elementStart' : ('', {}),
   'elementEnd' : (),
   'deleteCharactors' : (0,),
   'deleteElementStart' : ('', {}),
   'deleteElementEnd' : (),
   'annotationsBoundary' : ((), {})
}

class Tag(object):
   """Simplified document interface."""
   def __init__(self, doc, item, op = "elementStart"):
      #correct parameters
      if isinstance(doc, Tag): doc = doc._doc

      if op == "elementStart": self._closeTag = 'elementEnd'
      else: self._closeTag = False
      
      if isinstance(item, str):
         self._delta = delta.Operation("elementStart", item, {})
         op = ''
         
         item = datasource.Item(datasource.Item.TYPE_START_TAG, item)
      
      self._doc = doc
      self._item = item
      if op: self._delta = delta.Operation(op, *blankArgs[op])
      self._content = []      

   @property
   def _name(self): 
      """Returns the tag name/text of the tag, readonly."""
      return self._item.name

   #itterable properties
   def __len__(self):
      """Returns the number of direct children of the tag."""
      return len(self._content)

   def __getitem__(self, index):
      """Returns the child at specified index."""
      # support mapping incase attributes can't be used.
      if isinstance(index, str): return self.__getattr__(index)

      
      return self._content[index]

   def __setitem__(self, index, value):
      """Inserts (not replaces, use del for that) an object at index.
         Accepts Tag-like objects and strings.
         TODO: Correct processing to yield proper deltas."""
      # support mapping incase attributes can't be used
      if isinstance(index, str): return self.__setattr__(index, value)

      
      if isinstance(value, str): value = Text(value)
      self._content.insert(index, value)

   def __delitem__(self, index):
      """Removes an added child tag."""
      self._content[index]._delete()

   def append(self, item):
      self._content.append(item)

   #psuedo-properties
   def __getattr__(self, attr):
      """Returns the appropriate annotation value."""
      return self._item.annotations[attr]

   def __setattr__(self, attr, value):
      """Edits delta to set the appropriate annotation. 
         :warning: This does note apply it until you call :ref:sendDelta. """
      #ensure I can still set private properties
      if attr[0] == "_":
         object.__setattr__(self, attr, value)
         return
      
      #edit delta to set the attr
      index = self._delta.operation
      if index == "retain":
         self._delta = delta.Operation("updateAttributes", self._item.annotations)
         index = "updateAttributes"
      offset = annotationOffsets[index]
      self._delta.args[offset][attr] = value

   def __delattr__(self, attr):
      """Edits delta to remove an annotation.
         .. warning:: This does not apply it until you call :py:meth:`sendDelta`."""
      opName = self._delta.operation
      #handle new tags appropriately
      if opName == "elementStart":
         del self._delta.args[1][attr]
         return
         
      #ensure delta is is a annotationsBoundary
      if opName != "annotationBoundary":
         #backup information
         annotations = self._delta.args[annotationOffset[opName]]

         #combine with existing annotations
         keys = set().union(set(annotations.keys()), set(self._item.annotations.keys()))

         ann = {}
         for key in keys: ann[key] = (self._item.annotations[key], annotations[key]) 

         self._delta = delta.Operation("annotationsBoundary", [], ann)
      #edit delta to delete the attr
      self._delta.args[0].append(attr)

   #delta creation
   def _contentdelta(self, deltas):
      """Generates the list of operations for :ref:sendDelta."""
      deltas.append(self._delta)
      for child in self._content: child._contentdelta(deltas)
      if self._closeTag:
         deltas.append(delta.Operation(self._closeTag))

   def _delete(self):
      """Sets this tag to be deleted by outputted delta."""
      self._delta = delta.Operation("deleteElementStart", self._name, self._item.annotations)
      self._closeTag = "deleteElementEnd"

      for child in self._content:
         child._delete()

   def __str__(self):
      rep = "\n<%s>" % self._name
      for child in self:
         rep += "\n" + str(child)
      rep += "\n</END>"
      return rep

class Text(object):
   """Represents textual changes. """
   def __init__(self, text, op = "charactors"):
      self.__delta = delta.Operation(op, text)
      self.__text = text

   def _contentdelta(self, deltas):
      deltas.append(self.__delta)

   def _delete(self):
      self.__delta = delta.Operation("deleteCharactors", len(self.__text))

   def __str__(self):
      return str(self.__text) + "\t(Tag object)"
   
#utitlity functions
def TagDoc(doc):
   """Returns a list of Tags representing the doc.
      Adds a method sendDelta to send the delta."""

   class xList(list):
      def sendDelta(self):
         """Sends a beta delta based on the changes to this object and it's children."""
         #create delta
         ops = []

         for tag in self: tag._contentdelta(ops)

         #collapse retains
         fops = []
         curop = None
         for op in ops:
            if curop and op.operation == curop.operation == "retain":
               curop.args[0] += 1
            elif op.operation == "retain":
               op.args[0] = 1
               fops.append(op)
               curop = op
            else:
               curop = op
               fops.append(op)
            
         deltaO = delta.Delta(*fops)
         
         delta.betaDeltaObservable.applyDelta(self._doc, deltaO)
         return deltaO
      
   # generation variables
   i = 0
   rep = xList()

   while i < len(doc.items):
      tag, i = TagItem(doc, i)
      i += 1 # otherwise i is on an end item.
      rep.append(tag)

   rep._doc = doc
   return rep

def TagItem(doc, index):
   """Returns a Tag from the Item at index of the parent's document,
   and the index of it's end."""
   if doc.items[index].type == datasource.Item.TYPE_TEXT:
      return Text(doc.items[index].name, 'retain'), index
   
   parentTag = Tag(doc, doc.items[index], "retain")

   index += 1
   while doc.items[index].type != datasource.Item.TYPE_END_TAG:
         tag, index = TagItem(doc, index)
         parentTag._content.append(tag)
         index += 1

   return parentTag, index 
                          
def TagDelta(delta):
   """Returns a list of Tags representing the delta."""
   import tagop
   from datasource import Item

   class xList(list):
      def __init__(self):
         self.parents = [self,]
         
      def addTag(self, *args, **kwargs):
         parent = self.parents[-1]
         child = Tag(None, Item(*args, **kwargs))
         parent.append(child)

         if args[0] == 0:
            self.parents.append(child)
         elif args[0] == 1:
            self.parents.pop()
   
   return delta.applyToDoc(xList(), tagop)
