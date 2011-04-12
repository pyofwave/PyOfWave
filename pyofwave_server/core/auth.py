"""
Notifies all observers and authentication schemes when a user logs in and out and allows checking for
authentication.
"""
from zope import interface

class AuthService(interface.Interface):
   def signin(ip, username, password):
      """Signs a user in. """

   def getUser(ip):
      """Gets user profile. """

   def logout(ip):
      """Logs a user out. """

class User(object):
   def __init__(self, username, password, doc, folder):
      self.name = username
      self.password = password
      self.doc = doc
      self.folder = folder

class Folder(object):
   def __init__(self, name, icon, search, children):
      self.name = name
      self.icon = icon
      self.search = search
      self.children = children