Protocol Operators
******************

.. note:: Not yet implemented.

An operator is a function called by a client request to minipulate the server. These operators can be called by either the Simple Data Protocol or the Wave Client Protocol. These operators should be implemented to those standards.

Basic Form
==========

Operators have several parts guiding it's form in the protocols:

- A XML tagname

- Attributes and children

- Return element

- Event condition (determines when it is sent to client)

These map to the following syntax in python (with the namespace being the file your in):

   from ..core import opdev
   from lxml import etree as xml

   NS = " :strong:`XML namespace` "

   class :strong:`local tagname` (opdev.Operation):
      """ :strong:`description` """

      def s(events, :strong:`expected children`, :strong:`attributes`):
         :strong:`action`

         return :strong:`return element`

      def r(tag, delta):
         if :strong:`conditional`: return :strong:`event element`

      q = " :strong:`xQuery conditional` "

As a shortcut, when PyOfWave receives an operation, it will distribute it as an event without checking the conditionals. You will not be able to block it. 

Instead the conditionals are to check if the same effective action has been applied. 