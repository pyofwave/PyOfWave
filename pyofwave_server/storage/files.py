"""
Provides a storage class which uses .wave & .ver files to save data.
Not recommended for production use.  
"""
from ..core import delta
import cPickle

class FileStorage(object):
   def __init__(self, path, checkDomain):
      self.path = path
      self.checkDomain = checkDomain
      
   def applyDelta(self, doc, delta):
      doc = self.filename(doc)
      if not doc: return
      #update .wave file
      wavelet = delta.update(self.getDocument(doc))
      f = open(doc+".wave", "w")
      pickle.dump(wavelet, f)
      f.close()
      #append onto .ver file
      f = open(doc+".ver", "a")
      pickle.dump(delta, f)
      f.close()

   def newDocument(self, doc):
      doc = self.filename(doc, "newDocument", doc)
      if type(doc) != "String": return
      open(doc+".wave", "w").close()
      open(doc+".ver", "w").close()

   def getDocument(self, doc):
      doc = self.filename(doc, "getDocument", doc)
      if type(doc) != "String": return doc
      f = open(doc+".wave", "r")
      rep = cpickle.load(f)
      f.close()
      return rep

   def getDocumentVersion(self, doc, start, end, limit):
      doc = self.filename(doc, "getDocumentVersion", doc, start, end, limit)
      if type(doc) != "String": return doc
      if (end-start > limit): end = start + limit

      #load data
      f = open(doc+".ver", "r")
      res = []
      i = 0
      while delta or i >= end:
         delta = cpickle.load(f)
         res.append(delta)
      return res[start:end]

   def filename(self, doc, call = None, *args):
      if "!" in doc:
         doc = doc.split("!")
         if doc[0] != SETTINGS.DOMAIN and not chckDomain: 
            if call: return getatter(self.successor, call)(*args)
            return None
         return path+doc[1]
      return doc
