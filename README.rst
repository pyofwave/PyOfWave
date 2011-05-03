PyOfWave server and webclient
=======================
Wave is a combination of existing communication technologies (eMail, forums, wikis, and instant messaging) designed by Google. PyGoWave is one implementation of Wave programmed in Python.

Server
=====

The server provides protocols around some core functionality (authentication, profiles, "document" access, and sending and recieving "deltas"). These protocols are documented in docs/protocols. 

The client and server acts as 2 different programs. The server is a customizable application while the client is some CGI and "static" web files. 

Dependancies
--------------------

+ Python 2.7+ -  http://python.org/

+ Twisted (requires zope.interface)  - http://twistedmatrix.com/

+ python-xmpp-server (requires Tornado - http://tornadoweb.org/)  - https://github.com/thisismedium/python-xmpp-server/

+ CouchDB - http://couchdb.apache.org/ or any Relational Database System (Optional, recommended for production)


Client
====

The client provides a dynamic web based interface to PyOfWave_server, using the Wave Simple Data Protocol. It is designed to be embedded in the frame of your site and delivers great customizability and ease.  

It is written using the JavaScriptMVC library and jQuery, both of which are included in this project.

Used jQuery Plugins
------------------------------

- jQuery UI slider

- JavaScriptMVC (http://javascriptmvc.com/)

- farbtastic (https://github.com/mattfarina/farbtastic/)

- editabletext (https://github.com/alcinnz/editableText/)

- treeview (http://bassistance.de/jquery-plugins/jquery-plugin-treeview/)

- JSON plugin encoder (derived for easy access, http://www.ramirezcobos.com/2009/12/30/json-jquery-plugin/)

P. S. 
====

I, alcinnz, will roster off extension tasks for the server next week (my time), with Mozilla Drumbeat promotion. Please message me what you'd like to do (the list will come online shortly).