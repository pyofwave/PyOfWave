Data Import Planning
====================

For the development on POW client to be real development that can be hooked up to the XMPP PyOfWave Server (which would have to be done via BOSH), we must look forward to how we'll get this data. 

For a library to implement BOSH, I've seen nothing smaller or nicer than Strophe.js, and UI-wise Knockout.js is the first MVC (or as it says MVVM) library I found which gives me the flexibility I want (and again is quite small). These are nice libraries, but the problem is connecting the two as Strophe (as a matter of it's field) reports DOM elements while Knockout.js requires heavy use of ko.Observable objects to work properly. The reasonable thing to do is to connect the two. 

As for how this would look, it would be convenient if a utility method would take an element to send to the server (Strophe.js objects) and return a ko.Observable (Knockout.js object). Using Strophe builders would allow easy element configuration while the Observable would tie nicely into the scene and provide a very smooth mechanism for updates. Behind the scenes, this utility would:

1. Register "event" with Strophe.js and the server.
2. Send the IQ
3. Translate all responses for the object into ko.Observable objects
4. Sends changes back.

In psuedocoding the templates (which will slowly be smoothed over into working templates), I found that it would be useful for the utility to return an inner function which assigns arguments to specified attributes. From here, these resulting "stanzas" will usually assign to one destination, so instead of returning a Observable, the utility should take one to update. 

The main question is: what should the adapted objects look like?
----------------------------------------------------------------

Ofcourse, they shouldn't clone the DOM APIs, that would be hard work with little reward, what we need is an easy way to get attributes and children by tagname, all with namespacing. 

On a first draft, I tried playing with the idea of just using properties on the object, with underscore instead of colons for namespaces and underscores donoting children. However, using namespaces turns out tedius and I wonder if there are easier to implement interfaces. So I'm thinking of using a function based interface instead with a setting for default namespace. This would take a simple query string and return an observable. 
