PyGoWave re-Relaunch
=================
Hello,
Since p2k does not seem to be interested in continuing this project, and I think that Wave deserves to rise from the grave (O.K., Apache is working on this too, but shouldn't there be multiple servers?), I will attempt to take ownership of this project and make use of the down time to make some slight changes to both the Wave standard and PyGoWave (although I will follow those standards for the most part). Any help would be greatly appreciated, and i should get back onto development as soon as I've setup a testbud. My revised plans follow (based on p2k's plan). 


The plans
=========

Backend
-------

* Provide a Django service for those that can't use the live-client (I like to use accessible practices). 
* Orbited will be kept as Comet-Framework for the Web Client
* The data models will be completely redesigned to fit the Federation Protocol
  requirements; all data will be XML documents
* There will also be an Erlang port of the RPC server as before (I may not provide)
* For persistency, plain XML files and SQL databases will be supported


Protocols
---------

* There will be means to convert operations and snapshots of waves for use with
  several protocols via a modular approach
* The old PyGoWave protocol will be replaced by the official Wave Data Protocol
  with a small extension to allow subscribing to events and for receiving
  letter-by-letter updates (this will be called "PyGoWave Simple Data Protocol")
* The official Wave Robot Protocol will be fully supported at a later point
* For clients other than the Web Client, there will be a bigger extension to the
  Wave Data Protocol which allows the reception of XML-operations (called
  "PyGoWave Extended Data Protocol")
* Non-browser clients will also have a lighter weight protocol for operations based on conf files. 
* I'll allow contributors to create their own clients, but avoid creating my own. 
* The simple API features Wave/Wavelet/Blip models only and uses the PyGoWave
  Simple Data Protocol. 
* Gadgets will have a greatly simplified SDK to ease non-browser clients (removing most browser APIs & languages
  and adding KVO and "super methods" to JS for simple SDK). 


Frontend / Web Client
---------------------

* I will implement the client in JavaScriptMVC because p2k's choice of Sproutcore didn't suit. 
* The standard protocols will be used in the client in order to ensure full access to other clients. 
* The new frontend tries to mimic the behavior of the redesigned Wave web
  frontend as good as possible (or even better), with a example I'll upload soon. 

If you are unsure what Wave is, or want to pitch it to your freinds, please read doc/ADVERTORIAL. I would also encourage developers to read it whether or not they understand what it is, as it contains important guidelines for you.