Protocol Operators
******************

An operator is a function called by a client request to minipulate the server. These operators can be called by either the Simple Data Protocol or the Wave Client Protocol. These operators should be implemented to those standards.

Basic Form
==========

Operators have several parts guiding it's form in the protocols:

- A namespace

- A name

- Arguments

- Return value map

These map to the following syntax in python (with the namespace being the file your in):

   def :strong:`name` (ip, :strong:`arguments comma seperated`):
      **routine**

      return {
         **return map**
         }

If you want to minipulate the wave, it is reccomended that you use :py:mod:`core.auth`.