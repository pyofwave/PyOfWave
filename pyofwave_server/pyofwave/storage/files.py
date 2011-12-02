"""
Provides a storage class which uses .wave & .ver files to save data.
Not recommended for production use.  
"""
import cPickle

from pyofwave.conf import settings
from pyofwave.core import delta

class FileStorage(object):
   """
   A simple backing store using files to store waves
   """
   def __init__(self, path=None, checkDomain=None):
      self.path = path or settings.FILESTORAGE_PATH
      self.checkDomain = checkDomain or settings.FILESTORAGE_CHECKDOMAIN
      
   def applyDelta(self, doc, delta):
      doc = self.filename(doc)
      if not doc: return
      
      # update .wave file
      wavelet = delta.update(self.getDocument(doc)) # apply the delta
      f = open(doc+".wave", "w") # overwrite
      pickle.dump(wavelet, f)
      f.close()
      
      # append onto .ver file
      f = open(doc+".ver", "a") # append at end of file.
      pickle.dump(delta, f)
      f.close()

   def newDocument(self, doc):
      doc = self.filename(doc, "newDocument", doc)
      if type(doc) != "String": return

      # create the files.
      open(doc+".wave", "w").close()
      open(doc+".ver", "w").close()

   def getDocument(self, doc):
      doc = self.filename(doc, "getDocument", doc)
      if type(doc) != "String": return doc

      # unpickle current 
      f = open(doc+".wave", "r")
      rep = cpickle.load(f)
      f.close()
      return rep

   def getDocumentVersion(self, doc, start, end, limit):
      doc = self.filename(doc, "getDocumentVersion", doc, start, end, limit)
      if type(doc) != "String": return doc
      if (end-start > limit): end = start + limit # ensure the limit is met.

      # load data
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
         # if not in this domain, call the sucessor.
         if doc[0] != SETTINGS.DOMAIN and not chckDomain: 
            if call: return getatter(self.successor, call)(*args)
            return None
         return path+doc[1]
      
      return doc
