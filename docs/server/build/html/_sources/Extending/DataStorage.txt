Data Storage Extensions
*****************************

If the existing data storage options don't suit you, you can easily add your own.

1. Preparing the Datasource
====================

The datasource needs to be set up to be able to store PyOfWave documents before you integrate it. To do this, setup your datasource to store under a name:

- A sequence of "items"

   - Each item must have some text; a type of either open, close, or text; and a map of annotations.

- A map of tags, for each user and global, to a sequence of values.

2. Implement the Adaptor
===================

Add a new Python file in datasource (doesn't really matter if you put it there) and code::

   from ..core import datasource
   from zope import interface

Implement the methods.

3. Integrate the Adaptor
=================

Open PREFERENCES.py and import your file. Then set one of the storage options (either CACHE_OBJECT and/or STORAGE_OBJECT) to an instance of your adaptor.