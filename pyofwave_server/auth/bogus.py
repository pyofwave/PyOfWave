"""
Bogus Authentication
"""
from ..core import auth, datasource as ds
from zope import interface

class BogusAuth(object):
    interface.implements(auth.AuthService)

    def signin(ip, username, password, alias=''):
        return True

    def setPassword(ip, oldpassword, password):
        return True

    def getUser(ip):
        return auth.User("jsmith@pyofwave.net",
                         ds.Document(ds.Item(ds.Item.TYPE_TEXT, " ",
                                             name = "John Smith",
                                             note = "The trickster, the riddler, the keeper of balance, he of many faces who finds light in death and who fears no evil; he who walks through doors. Brisingr by Christopher Poalini on Doctor Who",
                                             avatar = "http://example.com/blank.png")),
                         auth.Folder(0, "All Waves", "wave.png", "", (
                             auth.Folder(1, "Unread", "inbox.png", "unread", ()),
                             auth.Folder(2, "Chats", "bubble.png", "chat", ())
                             ))
                         )

    def deleteFolder(folder):
        return False #unsupported

    def logout(ip):
        return False #unsupported
