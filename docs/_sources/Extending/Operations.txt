Protocol Operators
******************

An operator is a function called by a client request to minipulate the server. These operators can be called by either the Simple Data Protocol or the Wave Client Protocol. These operators should be implemented to those standards.

Basic Form
==========

Operators have several parts guiding it's form in the protocols:

- A XML tagname

- Attributes and children

- Return element

- Event condition (determines when it is sent to client)

These map to the following syntax in python (with `<` and `>` surrounding parts specific to your tag)::

   from ..core.opdev import OperationNS as Ops
   NS = Ops("<XML namespace>")

   @NS
   def <tagname>(usr, <expected children>, <attributes>):
      <action>
      return <return element>

   @NS("<xQuery conditional>")
   def _<tagname>(S, tag, delta):
      if <conditional>: return S(<event element content>)

As a shortcut, when PyOfWave receives an operation, it will distribute it as an event without checking the conditionals. You will not be able to block it. 

Instead the conditionals are to check if the same effective action has been applied. 

.. note:: Event conditions aren't checked at all yet, but they will be soon.

OperationNS.E
-------------

The :py:class:`OperationNS` has a property of :py:data:`E` of class :py:class:`lxml.builder.ElementMaker` setup with the specified namespace. 

If you don't know how to use this factory (it's the same as :py:data:`lxml.builder.E`), it allows you to create XML tags using the following syntax::

   NS.E.tag(*children, **attributes)

Events
------

If for whatever reason, events in a namespace requires the :py:class:`EventRegistry` object associated with the connection, pass `events=True` to the :py:class:`OperationNS` constructor. In this case, the events object would be passed in place of the username for all registered operations with that namespace. 