Integrating Your Own Authentication Scheme
****************************************************

If your are integrating PyOfWave into your own system, it may well be the case that you want to integrate it with your existing authentication system. This is easy to do, providing you can do the following:

- Access the scheme from Python in PyOfWave's runtime.

- Add new fields to the authentication service (a PyOfWave document link and a personal folder scheme).

1. Preparing the Auth Service
======================

Due to the differences between different schemes, there's not much to be said here, except to:

- Ensure access from PyOfWave's Python runtime.

- Add to extra fields to the authentication service, doc (A link to a PyOfWave "document") and a link to a folder structure.

   * This folder structure should have fields for an ID, name, icon, search query (folders are actually saved searches), and children (or parent appropriately).

2. Implementing the Adaptor
=====================

Now create a Python file somewhere inside :py:mod:`pyofwave_server`. It does not matter what this file is called or exactly where it is. Inside it, code::

   from core import datasource #may change depending on where you put the file
   from zope.interface import implements

Now implement all the methods to refer back to your authentication scheme. 

3. Integrate the Adaptor
=================

Now open :file:`PREFERENCES.py` and 

#. Import the file you just created.

#. Set AUTHENTICATION to an instance of your adaptor.

Congratulations! Now when you run the server, it should be using your existing authentication service.

That wasn't hard, was it.