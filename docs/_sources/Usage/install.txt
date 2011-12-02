Installing PyOfWave on Your Server
**********************************

This file leads you through how to install PyOfWave on your server.

Setting Up the Server
=====================

#. Download PyOfWave at https://github.com/alcinnz/pyofwave/ .

#. Customize your settings/preferences as discussed in :doc:`settings`.

   At least open SETTINGS.py and set those values.

#. Execute :file:`pyofwave_server_launch`.

Setting Up the Client
=====================

#. Ensure that the HTTP server you plan to use supports:

   * Serving raw files.

   * Supports Python CGI.

      .. note:: This is note necessary if you have already integrated an authentication scheme that provides authentication and registration.

#. Customize :file:`pyofwave_client/index.html` and :file:`pofwave_client/pyofwave_client/pyofwave_client.html` to include your branding.

#. Place these files in your server's web directory.

#. Start your HTTP server.