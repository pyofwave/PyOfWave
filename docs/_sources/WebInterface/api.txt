POW Web Client API
******************

This API provides the building blocks for the POW web client. These building blocks are organized into scripts that each do one thing:

* :file:`kvo.js` provides a "Key Value Coding" interface to cut down on coupling between model and view. 

* :file:`wquery.js` provides an interface upon the *Simple Data Protocol* and the *Events Protocol* to communicate with the server.

  .. note:: To develop, use :file:`wQuery-local.js` which bounces request 
      back as events to remove dependancy on the server for testing.

* :file:`events.js` provides callback implementations for when events are recieved.

* :file:`waveUIx.js` provides frequently reused "views" so as to encourage internal consistancy.

* :file:`waveUI.js` provides jQuery widgets, "Controllers", which collectively represent a Wave.

* :file:`elements.js` provides routines to handle inserting elements inside a "blip", a single message in a wave.

kvo.js
======

:file:`kvo.js` has one class, which wraps an object and calls a list of observers when that object changes.

.. js:class:: KVO

   :param obj: The object to wrap all properties are wrapped.

   .. js:function:: get(key)

      :param key: The property or index to access.
      Returns a property of the wrapped object.

      :returns: KVO object or :js:class:`Integer`/:js:class:`String`.

   .. js:function:: set(obj)

      :param obj: The value to set the wrapped object to.
      Sets the wrapped object to a different value and notifies observers. 
      All properties of :js:data:`obj` are wrapped by :js:class:`KVO` 
      objects as well.

   .. js:function:: change(obj)

      Exactly like set except changes only changed properties, calling 
      appropriate observers.

   .. js:function:: observe(cb)

      :param cb: The :js:class:`Function` to be called when a change 
      occurs.

      :returns: :js:class:`Integer` object to be passed to 
         :js:attr:`KVO.unobserve` to remove :js:data:`cb` from observers.

   .. js:function:: unobserve(id)

      :param id: The :js:class:`Integer` returned by :js:attr:`KVO.observe` 
         when registering the function you wish to be removed from 
         the :js:class:`Array` of observers.

      Removes a function from the :js:class:`Array` of observers.

wquery.js
=========

wQuery manages and interfaces 2 protocols, "Simple Data Protocol" and the "Event Protocol". 

Simple Data Protocol
--------------------

The Simple Data Protocol is as simple as one function:

.. js:function:: sendOperations(...)
   
   Takes paramators in the form ``(operation, {key:value arguments}, 
   function(data) {handling code})``, representing all the operations to be 
   performed.

   Sends a Simple Data Protocol to the server via HTTP and calls 
   appropriate callbacks with the response.

Events Protocol
---------------

This protocol also has a basic API. To handle a event, simply set a property of the event's name on eventHandlers to a function taking an object returned by the server::

   eventHandlers.EVENT = function(obj) {
      handling code
   }

In addition, there are 2 hashtables (objects) of :js:class:`KVO` objects:

.. js:data:: wavelets

   Hashtable pairing wavelet IDs to :js:class:`KVO` objects wrapping JSON 
   objects returned by the server representing a wavelet (a wave or private 
   reply).

.. js:data:: blips

   Hashtable pairing blip IDs to :js:class:`KVO` objects wrapping JSON 
   objects returned by the server representing messages in a wavelet.

waveUIx.js
==========

:file:`waveUIx.js` provides several views for use by the POW web client. It provides:

* **menus** displays a list of action temporarily until an option is selected. It won't like the system one because the browser does not provide access to it.

* **cantact cards** displays the details for a contact on Wave.

* **toolbar** displays a list of actions until hidden. It is not as temporary as the menu, and only displays for/in the wave area. They are built of several menu items:

   * An **option** is an action in the toolbar that does something.

   * A **check option** toggles on and off and performs an action on the 
      page.

   * A **dropdown option** provides a list of choices for a value, which it 
      applies to an action.

   * A **radio option** is like a *check option* except only one in a group 
      (identified by a name) can be checked.

   * A **slider** wraps a jQueryUI slider and places it inside the toolbar.

   * A **color option** shows a Farbtastic colour picker when clicked.

waveUI.js
=========

:file:`waveUI.js` provides a number of *jQuery* widgets using *JavaScriptMVC*\'s :js:attr:`$.Controller`. It provides the following widgets:

* WaveletView

* ParticipantsBar

* BlipsListView

* BlipView

* GadgetView

WaveletView
-----------

.. rubric:: Options
 
ParticipantsBar
---------------

.. rubric:: Options

BlipsListView
-------------

.. rubric:: Options

BlipView
--------

.. rubric:: Options

.. rubric:: Methods

GadgetView
----------

.. rubric:: Options

.. rubric:: Methods