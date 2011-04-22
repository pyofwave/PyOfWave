Using PyOfWave's Core module
****************************

pyofwave_server.core provides facilities that are shared, in various methods, by all protocols and extensions. Specifics for extending this are provided by :doc:`Authentication`, :doc:`DataStorage`, :doc:`Operations`, and :doc:`Protocols`.

core.auth
=========

.. uml::
   interface AuthService
   object PREFERENCES.AUTH

   zope.interface.Interface ..|> AuthService
   AuthService --* "many" User
   User --* Folder
   Folder --* "many" Folder
   PREFERENCES.AUTH <|.. AuthService

   AuthService : boolean signin(int ip, string username, string password)
   AuthService : boolean setPassword(int ip, string oldpassword, string password)
   AuthService : User getUser(int ip)
   AuthService : boolean saveFolder(Folder folder)
   AuthService : boolean deleteFolder(Folder folder)
   AuthService : boolean logout(int ip)

   User : string name
   User : Document doc
   User : Folder folder

   Folder : fid
   Folder : string name
   Folder : string icon
   Folder : string search
   Folder : Folder[] children

Auth provides basic services for authentication and profiles in PyOfWave. To access a solid object, use :py:data:`PREFERENCES.AUTH`. 

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

   .. note:: This method is provided here to ease integration of 
      authentication schemes.

.. py:method:: deleteFolder(folder)

   Deletes a :py:class:`Folder` object from wherever the service saves it's 
   data.

   .. note:: This method is provided here to ease integration of 
      authentication schemes.

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

      The ID specified by the :py:class:`AuthService` to identify the folder. 
      This should not be changed (or you cannot :meth:`saveFolder` it), and 
      can be whatever the service wants it to be.

   .. py:attribute:: name

      The display name of the folder as a string.

   .. py:attribute:: icon

      The display icon of the folder as a string.

   .. py:attribute:: search

      The string to pass to :py:class:`DataSource` to get contained waves.

   .. py:attribute:: children

      A list of \"child\" Folder objects of the Folder.

core.datasource
===============

.. uml::
   interface DataSource
   object PREFERENCES.STORAGE_OBJECT
   object PREFERENCES.CACHE_OBJECT
   object PREFERENCES.FEDERATION_OBJECT

   zope.interface.Interface ..|> DataSource
   DataSource --* Document
   Document --* "many" Item

   DataSource <|.. PREFERENCES.STORAGE_OBJECT
   DataSource <|.. PREFERENCES.CACHE_OBJECT
   DataSource <|.. PREFERENCES.FEDERATION_OBJECT
   PREFERENCES.STORAGE_OBJECT --* PREFERENCES.CACHE_OBJECT
   PREFERENCES.CACHE_OBJECT --* PREFERENCES.FEDERATION_OBJECT
   PREFERENCES.FEDERATION_OBJECT --* PREFERENCES.CACHE_OBJECT

   DataSource : newDocument(string doc)
   DataSource : getDocument(string doc)
   DataSource : getDocumentVersion(string doc, int start, int end, int limit)
   DataSource : searchDocuments(string user, string search)
   DataSource : setTags(string doc, string user, string[] **tags)

   Document : Item[] items
   Document : int cursor

   Item : type
   Item : name
   Item : annotations

This module has exactly the same architecture of the core.auth module. The \"interface\" in this module is DataSource, the object is :py:data:`PREFERENCES.STORAGE_OBJECT` and it stores objects of :py:class:`Document` which contains a number of :py:class:`Item` objects. 

.. py:method:: newDocument(doc)

   Creates a new document in the DataSource. Returns the 
   blank :py:class:`Document` object if successful. 

.. py:method:: getDocument(doc)

   Loads the document from the DataSource. Returns a :py:class:`Document` object. 

.. py:method:: getDocumentVersion(doc, start, end, limit)

   Loads the document at the specified times. Returns a iterable :py:class:`Delta` 
   objects. 

.. py:method:: searchDocuments(user, search)

   Returns a list of wave documents that match the source. The tags that may be 
   specified in the search are provided by :py:meth:`setTags`. 

.. py:method:: setTags(doc, user, **tags)

   Sets the tags for the documentation for use by search. 

Classes:

.. py:class:: Document(*items)

   Represents a single \"document\" in the DataSource. 

   .. py:attribute:: items

      A list of :py:class:`Item` objects that make up the document. 

   .. py:attribute:: cursor

      An integer representing the current location of the \"cursor\" in the 
      document, used for delta processing. 

.. py:class:: Item(type, name, **annotations)

   Represents a single \"item\" that makes up a document in the DataSource. 

   .. py:attribute:: type

      Which type of item this is, as an integer. Values are specified by the class 
      attributes. 

   .. py:attribute:: name

      The name or text of the item as a string. 

   .. py:attribute:: annotations

      The mapping of the \"annotations\" attached to the tag. 

   .. py:data:: TYPE_START_TAG

      Setting :py:attr:`type` to this represents that it's a start tag, which is 
      closed by a following :py:data:`TYPE_END_TAG`.

   .. py:data:: TYPE_END_TAG

      Setting :py:attr:`type` to this represents that it closes the 
      previous :py:class:`Item` object with type :py:data:`TYPE_START_TAG`.

   .. py:data:: TYPE_TEXT

      Setting :py:attr:`type` to this indicates that it represents the single 
      charactor :py:attr:`name`, and does not need a closing item.

If this appears to be a bit imprecise, that's because you use this to store whatever data you need to, adhering to appropriate standards. 

core.delta
==========

.. uml::
   object AlphaDeltaObservable
   object BetaDeltaObservable

   DeltaObservable ..|> AlphaDeltaObservable
   DeltaObservable ..|> BetaDeltaObservable
   
   Delta --* Operation
   class Message

   DeltaObservable : applyDelta(Document doc, Delta delta)
   DeltaObservable : addObserver(callable observer)
   DeltaObservable : removeObserver(callable observer)

   Delta : Operation[] ops
   Delta : ApplyToDoc(Document doc, Module mod = deltaop)

   Operation : string operation
   Operation : list args
   Operation : applyToDoc(Document doc, Document new)

   Message : string message
   Message : int version

:py:mod:`core.delta`, this time, uses the architecture of a classic observer pattern. This module is used to distribute changes to documents, \"deltas\", generated by the Federation and other protocols. These deltas can be in either \"alpha\" or \"beta\" state (after and before being commited to storage). In addition to just being passed around, they can also be applied to a document (which should only be done if you're creating a new datasource, :doc:`DataStorage`).

Any one has the ability to distribute deltas on a :py:class:`DeltaObservable`, but you should only do it on :py:data:`BetaDeltaObservable` leaving :py:class:`DataSource` objects to distribute on :py:data:`AlphaDeltaObservable`, so as that the distributed :py:class:`Delta` objects distributed there are truly in alpha state.

DeltaObservable
---------------

:py:class:`DeltaObservable` distributes :py:class:`Delta` objects throughout all extensions. 

.. autoclass:: pyofwave_server.core.delta.DeltaObservable


There's two instances of this class you'll use to distribute :py:class:`Delta` objects:

.. py:data:: AlphaDeltaObservable

   :py:class:`DataSource` objects pushes deltas through this 
   :py:class:`DeltaObservable`, which indicates that all :py:class:`Delta` 
   objects from this object has been commited to storage.

.. py:data:: BetaDeltaObservable

   :py:class:`DataSource` objects are observers of this object, which means 
   that by sending :py:class:`Delta` objects on this object, you are 
   commiting them to memory.

Deltas, Operations, and Messages
--------------------------------

.. autoclass:: pyofwave_server.core.delta.Delta

.. autoclass:: pyofwave_server.core.delta.Operation

.. autoclass:: pyofwave_server.core.delta.Message

:py:class:`Operation` wraps calls to functions in :py:mod:`deltaop`, which map to the standard Federation operations:

.. automodule:: pyofwave_server.core.deltaop

core.operation
==============

:py:mod:`core.operation` has only one function, which imports a function from pyofwave_server.operations and executes it with given arguments. 

.. py:function:: performOperation(ip, operation, kwargs)

   Executes the operation operation and provides it ip and kwargs. It will either 
   raise a :py:exc:`OperationError` providing a status dictionary and code (as in 
   HTTP Error codes), or return a mapping.

Instructions for adding operations are in :doc:`Operations`.

core.tags
=========

This module allows provides an alternate way to examine :py:class:`Document` and :py:class:`Delta` objects and create :py:class:`Delta` objects than by hand. The Tag class this module provides allows you to work with Documents simalor to how you work with XML with eTree. It lets you think of each tagname as a different object.

Annotation are now properties and children are accessed like the :py:class:`Tag` object was a :py:class:`List`. With this new ease, there's a few things to keep in mind:

1. Property changes don't take effect until you call :py:meth:`sendDelta`.

2. When you assign a value to an index, it is inserted there and the previous value will be after it. ''del'' it if you want to delete it.

   .. note:: This is to avoid problems in deltas.

3. Simalor to point 1, when you ''del'' an index, it is replaced with an object representing a deleted item. Call :py:meth:`sendDelta` to send changes.

Importing Objects to Tags
-------------------------

This module provides 3 functions which "import" objects to :py:class:`Tag` objects: :py:func:`TagDoc`, :py:func:`TagItem`, & :py:func:`TagDelta`.

.. automodule:: pyofwave_server.core.tags