PyOfWave server and webclient
=======================
Wave is a combination of existing communication technologies (eMail, forums, wikis, and instant messaging) designed by Google. PyGoWave is one implementation of Wave programmed in Python.

Server
=====

The server provides protocols around some core functionality (authentication, profiles, "document" access, and sending and recieving "deltas"). These protocols are documented in docs/protocols. 

Dependancies
--------------------

+ Python 2.7+ -  http://python.org/

+ Twisted (requires zope.interface)  - http://twistedmatrix.com/

+ python-xmpp-server (requires tornado - http://tornadoweb.org/)  - https://github.com/thisismedium/python-xmpp-server/

+ CouchDB - http://couchdb.apache.org/ or any Relational Database System (Optional, recommended for production)


Client
====

The client provides a dynamic web based interface to PyOfWave_server, using the Wave Simple Data Protocol. It is designed to be embedded in the frame of your site and delivers great customizability and ease.  

It is written using the JavaScriptMVC library and jQuery (as well as a port of Django's templating), both of which are included in this project.

Used jQuery Plugins
------------------------------
- JavaScriptMVC (http://javascriptmvc.org/)

- farbtastic

- editabletext (slightly altered for lower level use, with added cursor location, http://niichavo.wordpress.com/2009/01/06/contenteditable-div-cursor-position/)

- treeview

- JSON plugin encoder (derived for easy access)