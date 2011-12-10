Installing PyOfWave on Your Server
**********************************

This file leads you through how to install PyOfWave on your server.

Setting Up the Server
=====================

.. note:: Since PyOfWave is still under heavy development, we
   	  recommend using virtualenv for testing.

#. Download a release of PyOfWave at https://github.com/pyofwave/PyOfWave/ or if
   you prefer to live on the bleeding edge, clone
   the repository::

     git clone https://github.com/pyofwave/PyOfWave

#. From inside the downloaded and uncompressed directory (you can skip
   this step if you want to use it locally)::

    cd pyofwave_server/
    python setup.py install

#. Create a file named :file:`settings.py` as described by :doc:`settings` and from its directory run::

    pyofwave

.. note:: If your :file:`settings.py` file is not in the current
   	  directory, you can export the :py:data:`PYOFWAVE_SETTINGS_MODULE` symbol.

Setting Up the Client
=====================

#. Ensure that the HTTP server you plan to use supports:

   * Serving raw files.

   * Supports Python CGI.

#. Customize :file:`pyofwave_client/index.html` and :file:`pofwave_client/pyofwave_client/pyofwave_client.html` to include your branding.

#. Place these files in your server's web directory.

#. Start your HTTP server.
