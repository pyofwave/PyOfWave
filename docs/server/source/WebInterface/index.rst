For Web Developers
******************

.. toctree::
   :maxdepth: 2

   design
   api

Overview
========

The client is built using `JavaScriptMVC <http://javascriptmvc.com/>`_ and `jQuery <http://jquery.com/>`_ . 

It is also built upon strict organization:

* :file:`pyofwave_client/pyofwave_client.html` stores the final user experience along with the files in the same directory.

* :file:`api/` stores all dependancies.

* :file:`pyofwave_client/api/` stores the building blocks upon which :file:`pyofwave_client.html` is built.

* :file:`gadget/` stores the gadget iframe environment. 