PyOfWave server and webclient (in development, pre-beta)
=======================
Wave is a combination of existing communication technologies (eMail, forums, wikis, and instant messaging) designed by Google. PyGoWave is one implementation of Wave programmed in Python.

Server
=====

The server provides protocols around some core functionality (authentication, profiles, "document" access, and sending and recieving "deltas"). These protocols are documented in docs/protocols. 

The client and server acts as 2 different programs. The server is a customizable application while the client is some CGI and "static" web files. 

When launched, PyOfWave appears to do nothing, but don't worry, it sets up API and shortly Internet access to them. Eventually, it'll become a deamon and include a setup and settings utility.

Dependancies
--------------------

+ Python 2.7+ -  http://python.org/ (older versions can be used with installation of importlib)

+ Python XMPP Server (requires Tornado, includes Twisted adaptor) - https://github.com/thisismedium/python-xmpp-server

+ Twisted Projects (requires zope.interface, for integration to existing protocols)  - http://twistedmatrix.com/

+ CouchDB - http://couchdb.apache.org/ or any Relational Database System (Optional, recommended for production)


Client
====

The client provides a dynamic web based interface to PyOfWave_server, using websockets on the client protocol or a backup protocol. It is designed to be embedded in the frame of your site and delivers great customizability and ease.  

It is written using Agility.js and jQuery, both of which are included in this project.

Used jQuery Plugins
------------------------------

- jQuery UI (http://jqueryui.com/)

- MVClets(https://github.com/pyofwave/MVClets/)

- farbtastic (https://github.com/mattfarina/farbtastic/)

- jsTree (http://www.jstree.com/)

Other dependancies
-----------------------------

- Strophe.js (https://github.com/metajack/strophejs)

- RepoTheWeb (https://github.com/mozilla/repotheweb) - For registerProtocolHandler support.

- CoffeeScript (https://github.com/jashkenas/coffee-script) - Purely for development.

P. S. 
====

Shortly, I will be rebuilding PyOfWave to use one XMPP based protocol for both web and offline clients and Federation. Client dependancies have been considered and changed to support a XMPP BOSH protocol.
The roster is old as of now. 