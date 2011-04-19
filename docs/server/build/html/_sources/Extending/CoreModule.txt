Using PyOfWave's Core module
****************************

pyofwave_server.core provides facilities that are shared, somehow, by all protocols and extensions. Specifics for extending this are provided by my :doc:'Authentication' , :doc:'DataStorage' , :doc:'Operations' , and :doc:'Protocols' .

core.auth
=========
Auth provides basic services for authentication and profiles in PyOfWave. To access a solid object, use :py:data:SETTINGS.AUTH . 

This object has the following methods.

.. py:method:: signin(ip, username, password)

   Logs a user in with specified username and password on specified IP 
   Address. Returns a boolean indicating success.

.. py:method:: setPassword(ip, oldpassword, password)

   If the user logged in on IP has an existing password of oldpassword, 
   changes their password to password. Returns a boolean indicating success.

.. py:method:: getUser(ip)

   Gets the user logged in on the specified IP address. Returns a 
   :py:class:User object.

.. py:method:: saveFolder(folder)

   Saves a :py:class:Folder object to wherever the service saves it's data, 
   providing the fid property has not changed.

.. py:method:: logout(ip)

   Cancels the user authentication on a IP. Returns a boolean indicating 
   success.

When calling the :py:meth:'getUser' method, you will get a :py:class:'User' object. This class is effectively a structure:

.. py:class:: User(name, doc, folder)

   Represents a user, and wraps whatever authentication service is used. 
   This represents the basic profile you'll need with Wave.

   .. py:attribute:: name

      The user's wave address with your domain name cut off as a string. 
      Strictly, it is allowed to be changed, but it will not change 
      anything.

   .. py:attribute:: doc

      A :py:class:Document object representing the user's profile. In PyOfWave, 
      this isn't expected to be anything, but gadgets will have expectations 
      and other servers. I discuss these required annotations in my 
      Federation Format standard (in repository docs/protocols/
      federationFormat.txt).

   .. py:attribute:: folder

      A :py:class:Folder which illustrates the user's organisation of waves. 
      You'll need to use search to get the waves inside these, though.

.. py:class:: Folder(fid, name, icon, search, children)

   Represents an \"inbox\" for the user to store their waves in. 

   .. py:attribute:: fid

      The ID specified by the :py:class:AuthService to identify the folder. 
      This should not be changed (or you cannot :meth:saveFolder it), and 
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
This module has exactly the same architecture of the core.auth module.