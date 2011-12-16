Settings in PyOfWave Server
***************************

This file documents all the values in :file:`settings.py`  and
:file:`protocols/__init__.py` you can customise.

General settings
================

.. py:data:: DOMAIN

   *Required* (pyofwave.info for testing)

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
==============

If you wish to customize how data is handled in PyOfWave, use these variables. If you need more details, please see :doc:`../Extending/CoreModule`.

.. py:data:: DATASOURCE_STORAGE

   Default: 'storage.files.FileStorage'

   The main storage object used by all protocols and extensions. Use a
   dotted path that points to the module.



protocols/__init__.py
=====================

.. note:: These settings have to be moved out of the package to allow
    	  user reconfiguration.

          Perhaps add a :py:data:`ADDONS` setting. 

In this file, you setup any changes to the protocols you have in your runtime. Instructions for doing this can be found at :doc:`../Extending/Protocols`.
