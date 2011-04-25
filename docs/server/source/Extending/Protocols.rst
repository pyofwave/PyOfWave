Adding New Protocols to the PyOfWave Server
*******************************************

Protocols are programmed in PyOfWave using `Twisted <http://twistedmatrix.com/trac>`_. Integration is provided by :py:mod:`core` as documented in :doc:`CoreModule`. Saying that, there's a few organizational things we do to keep things tidy.

#. Place your protocol in it's own folder inside protocols.

#. Tie it into the system in :file:`__index__.py`.