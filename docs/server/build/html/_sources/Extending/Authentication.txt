Integrating Your Own Authentication Scheme
****************************************************

.. note:: Not yet implemented.

If your are integrating PyOfWave into your own system, it may well be the case that you want to integrate it with your existing authentication system. This is easy to do, providing you can do the following:

- Access the scheme from Python in PyOfWave's runtime.

Authentication is performed by Python SASL underneath Python XMPP Server. To change the authentication scheme for PyOfWave, you should change it within Python SASL. 

A tutorial will eventually be provided. 