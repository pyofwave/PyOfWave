Testing PyOfWave
================


Running the tests
-----------------

We use trial_, the test runner of Twisted.

Since we depend on a configuration file (see :doc:`../Usage/settings`), you
need to run the tests either by using :file:`setup.py` or :file:`runtest.py`. These
scripts set a correct environment for you before running the test suite::

	python setup.py test

or::

	./runtest.py


Writing new tests
-----------------

Tests are written in a :file:`tests/` directory, located under your
package. Make sure the files start with the :file:`test_` prefix, such
as :file:`test_client.py`.

You can write two kinds of tests:
    #. Standard Unittests
    #. Twisted Asynchronous Unittests

Standard Unittests
..................

This is the most common type of tests. Use them when you don't need to
mimic the asynchronous behaviour of twisted or of a network.

Here's a sample test::

       import unittest
       
       from pyofwave.core import operation, opdev
       
       class TestOperations(unittest.TestCase):
           def testCreateOperation(self):
	           NS = opdev.OperationNS("pyofwave.info/test")
		   assert(NS is not None)

           def testAnotherOne(...):
                   ...


Trial tests
...........

Such tests are specific to Twisted and make use of trial_
features. Trials helps us writing unit tests without worrying about
asynchronous returns and weird network behaviours.
You can refer to this document to learn `how to write asynchronous tests`__.

Here's an example::

       from twisted.trial import unittest
       from twisted.test import proto_helpers

       from ..client import ClientProtocolFactory

       class TestClientProtocol(unittest.TestCase):
           def setUp(self):
	       factory = ClientProtocolFactory()
	       self.proto = factory.buildProtocol(('127.0.0.1', 0))
	       self.tr = proto_helpers.StringTransport()
	       self.proto.makeConnection(self.tr)

	   def testCall(self):
               self.proto.dataReceived("#aname\r\n")
	       self.proto.dataReceived("[tests.operation")



Adding settings to the test environment
.......................................

Before writing a test, you may need to add a few variables to the test
environment. The file is located at :py:mod:`pyofwave.conf.test_configuration.py`.



.. _trial: http://twistedmatrix.com/trac/wiki/TwistedTrial
__ http://twistedmatrix.com/documents/current/core/howto/testing.html
