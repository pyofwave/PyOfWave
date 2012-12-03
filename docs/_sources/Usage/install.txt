Installing PyOfWave on Your Server
**********************************

This file leads you through how to install PyOfWave on your server.

Setting Up the Server
=====================

#. Download PyOfWave at https://github.com/pyofwave/PyOfWave/ .

#. From inside the downloaded and uncompressed directory::

    python setup.py install

#. Create a file named :file:`settings.py` as described by :doc:`settings` and from it's directory run::

    pyofwave

.. note:: Should we add a argument of the file to import?

Setting Up the Client
=====================

#. Ensure that the HTTP server you plan to use supports:

   * Serving raw files.

   * Supports Python CGI.

#. Customize :file:`pyofwave_client/index.html` and :file:`pofwave_client/pyofwave_client/pyofwave_client.html` to include your branding.

#. Place these files in your server's web directory.

#. Start your HTTP server.