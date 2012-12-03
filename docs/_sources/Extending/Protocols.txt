Adding New Protocols to the PyOfWave Server
*******************************************

.. note:: Not fully implemented.

Protocols are programmed in PyOfWave using `Twisted <http://twistedmatrix.com/trac>`_. Integration is provided by :py:mod:`core` as documented in :doc:`CoreModule`. Saying that, there's a few organizational things we do to keep things tidy.

#. Place your protocol in it's own folder inside protocols.

#. Tie it into the system in :file:`__index__.py`.

Use :py:mod:`Tornado` 's reactor module in place of :py:mod:`Twisted` 's, as to avoid networking clashes between the modules. :py:mod:`Tornado` is used because py:mod:`Python XMPP Server` (which we use for the main protocol) uses it. 