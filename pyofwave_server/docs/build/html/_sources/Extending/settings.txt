Settings in PyOfWave Server
***************************

This file documents all the values in :file:`SETTINGS.py`, :file:`PREFERENCES.py`, and :file:`__init__.py` you can customise.

SETTINGS.py
===========

It is *highly* recommended to set these settings, or PyOfWave may not function correct in your setup.

.. py:data:: DOMAIN

   This value represents your domain name. This is used by the protocols to 
   identify documents and users belonging to you. Should be a string.

.. py:data:: DELTA_OBSERVER_PROCESSES

   The number of processes to launch to handle changes in documents 
   "deltas". Should be a integer.

.. py:data:: DELTA_OBSERVER_TIMEOUT

   The number of tasks a process should run before it times out. Should be 
   a integer.

PREFERENCES.py
==============

If you wish to customize how data is handled in PyOfWave, use this file. If you need more details, please see :doc:`CoreModule`.

.. note:: This file is seperate to handle seperate dependancies (Python 
   yells if I have both settings using the objects and used by the objects 
   in the core server).

.. py:data:: STORAGE_OBJECT

   The main storage object used by all protocols and extensions.


__init__.py
===========

In this file, you setup any changes to the protocols you have in your runtime. Instructions for doing this can be found at :doc:`Protocols`.