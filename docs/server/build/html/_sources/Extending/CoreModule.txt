Using PyOfWave's Core module
****************************

pyofwave_server.core provides facilities that are shared, somehow, by all protocols and extensions. Specifics for extending this are provided by my :doc:`Authentication`, :doc:`DataStorage`, :doc:`Operations`, and :doc:`Protocols`.

core.auth
=========
Auth provides basic services for authentication and profiles in PyOfWave. To access a solid object, use :py:data:`SETTINGS.AUTH`. 

This object has the following methods.

.. py:method:: signin(ip, username, password)

   Logs a user in with specified username and password on specified IP 
   Address. Returns a boolean indicating success.

.. py:method:: setPassword(ip, oldpassword, password)

   If the user logged in on IP has an existing password of oldpassword, 
   changes their password to password. Returns a boolean indicating success.

.. py:method:: getUser(ip)

   Gets the user logged in on the specified IP address. Returns a 
   :py:class:`User` object.

.. py:method:: saveFolder(folder)

   Saves a :py:class:`Folder` object to wherever the service saves it's data, 
   providing the fid property has not changed.

.. py:method:: logout(ip)

   Cancels the user authentication on a IP. Returns a boolean indicating 
   success.

When calling the :py:meth:`getUser` method, you will get a :py:class:`User` object. This class is effectively a structure:

.. py:class:: User(name, doc, folder)

   Represents a user, and wraps whatever authentication service is used. 
   This represents the basic profile you'll need with Wave.

   .. py:attribute:: name

      The user's wave address with your domain name cut off as a string. 
      Strictly, it is allowed to be changed, but it will not change 
      anything.

   .. py:attribute:: doc

      A :py:class:`Document` object representing the user's profile. In PyOfWave, 
      this isn't expected to be anything, but gadgets will have expectations 
      and other servers. I discuss these required annotations in my 
      Federation Format standard (in repository docs/protocols/
      federationFormat.txt).

   .. py:attribute:: folder

      A :py:class:`Folder` which illustrates the user's organisation of waves. 
      You'll need to use search to get the waves inside these, though.

.. py:class:: Folder(fid, name, icon, search, children)

   Represents an \"inbox\" for the user to store their waves in. 

   .. py:attribute:: fid

      The ID specified by the :py:class:AuthService to identify the folder. 
      This should not be changed (or you cannot :meth:`saveFolder` it), and 
      can be whatever the service wants it to be.

   .. py:attribute:: name

      The display name of the folder as a string.

   .. py:attribute:: icon

      The display icon of the folder as a string.

   .. py:attribute:: search

      The string to pass to :py:class:DataSource to get contained waves.

   .. py:attribute:: children

      A list of \"child\" Folder objects of the Folder.

core.datasource
===============
This module has exactly the same architecture of the core.auth module. The \"interface\" in this module is DataSource and it stores objects of :py:class:`Document` which contains a number of :py:class:`Item` objects. 

.. py:method:: newDocument(doc)

   Creates a new document in the DataSource. Returns the blank :py:class:Document object if successful. 

.. py:method:: getDocument(doc)

   Loads the document from the DataSource. Returns a :py:class:`Document` object. 

.. py:method:: getDocumentVersion(doc, start, end, limit)

   Loads the document at the specified times. Returns a iterable :py:class:`Delta` objects. 

.. py:method:: searchDocuments(user, search)

   Returns a list of wave documents that match the source. The tags that may be specified in the search are provided by :py:meth:`setTags`. 

.. py:method:: setTags(doc, user, **tags)

   Sets the tags for the documentation for use by search. 

Classes:

.. py:class:: Document(*items)

   Represents a single \"document\" in the DataSource. 

   .. py:attribute:: items

      A list of :py:class:`Item` objects that make up the document. 

   .. py:attribute:: cursor

      An integer representing the current location of the \"cursor\" in the document, used for delta processing. 

.. py:class:: Item(type, name, **annotations)

   Represents a single \"item\" that makes up a document in the DataSource. 

   .. py:attribute:: type

      Which type of item this is, as an integer. Values are specified by the class attributes. 

   .. py:attribute:: name

      The name or text of the item. 

   .. py:attribute:: annotations

      The mapping of the \"annotations\" attached to the tag. 

If this appears to be a bit imprecise, that's because you use this to store whatever data you need to, adhering to appropriate standards. 