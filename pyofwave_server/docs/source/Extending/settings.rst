Settings in PyOfWave Server
***************************

.. note:: Shouldn't we move part of this to the :doc:`For Wave Providers` section ?

This file documents all the values in :file:`settings.py`  and
:file:`protocols/__init__.py` you can customise.

settings.py
===========

It is *highly* recommended to set these settings, or PyOfWave may not function correct in your setup.

General settings
----------------

.. py:data:: DOMAIN

   Default: '' (Empty string)

   This value represents your domain name. This is used by the protocols to 
   identify documents and users belonging to you. Should be a string.

.. py:data:: DELTA_OBSERVER_PROCESSES

   Default: Your CPU count

   The number of processes to launch to handle changes in documents 
   "deltas". Should be a integer.

.. py:data:: DELTA_OBSERVER_TIMEOUT

   Default: :py:data:`None`

   The number of tasks a process should run before it times out. Should be 
   a integer.

Backing stores
--------------

If you wish to customize how data is handled in PyOfWave, use these variables. If you need more details, please see :doc:`CoreModule`.

.. py:data:: DATASOURCE_STORAGE

   Default: 'storage.files.FileStorage'

   The main storage object used by all protocols and extensions. Use a
   dotted path that points to the module.



protocols/__init__.py
=====================

.. note:: These settings have to be moved out of the package to allow
    	  user reconfiguration

In this file, you setup any changes to the protocols you have in your runtime. Instructions for doing this can be found at :doc:`Protocols`.
