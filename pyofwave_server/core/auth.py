"""
Notifies all observers and authentication schemes when a user logs in and out and allows checking for
authentication.
"""
from zope import interface

class AuthService(interface.Interface):
   def signin(ip, username, password, alias=""):
      """Signs a user in. """

   def setPassword(ip, oldpassword, password):
      """Changes the logged in user's passord."""

   def getUser(ip):
      """Gets user profile. """

   def saveFolder(folder):
      """Saves changes to the folder."""

   def deleteFolder(folder):
      """Deletes a folder."""

   def logout(ip):
      """Logs a user out. """

class User(object):
   def __init__(self, username, doc, folder):
      self.name = username
      self.doc = doc
      self.folder = folder

class Folder(object):
   def __init__(self, fid, name, icon, search, children):
      self.fid = fid
      self.name = name
      self.icon = icon
      self.search = search
      self.children = children
