PyOfWave server and webclient
=======================
Wave is a combination of existing communication technologies (eMail, forums, wikis, and instant messaging) designed by Google. PyGoWave is one implementation of Wave programmed in Python.

## Server

The server provides protocols around some core functionality (authentication, profiles, "document" access, and sending and recieving "deltas"). These protocols are documented in docs/protocols. 

### Dependancies
+ Python 2.7+  @*python.org*

+ Twisted (requires zope.interface)  @*twistedmatrix.com*

+ python-xmpp-server (requires tornado @*tornadoweb.org*)  @*https://github.com/thisismedium/python-xmpp-server/*


## Client