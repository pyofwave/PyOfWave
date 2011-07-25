PyOfWave server and webclient (in development, pre-beta)
=======================
Wave is a combination of existing communication technologies (eMail, forums, wikis, and instant messaging) designed by Google. PyGoWave is one implementation of Wave programmed in Python.

Server
=====

The server provides protocols around some core functionality (authentication, profiles, "document" access, and sending and recieving "deltas"). These protocols are documented in docs/protocols. 

The client and server acts as 2 different programs. The server is a customizable application while the client is some CGI and "static" web files. 

When launched, PyOfWave appears to do nothing, but don't worry, it sets up API and shortly Internet access to them. 

Dependancies
--------------------

+ Python 2.7+ -  http://python.org/ (older versions can be used with installation of importlib)

+ Twisted (requires zope.interface)  - http://twistedmatrix.com/

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

Tasks are currently being rostered off of the roster.rst file. 