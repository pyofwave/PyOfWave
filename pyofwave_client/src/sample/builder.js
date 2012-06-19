/* Sample data builder for PyOfWave client
* 
* Enforces a XML structure to sample data used for development.
* This is done to make it easier to switch to a XMPP BOSH 
* interface which was chosen for serverside simplicity.
*/
define(['../../api/knockout-2.1.0'], function(ko) {
	return function() {
		var args = Array.slice(arguments),
			name = args.shift(),
			attrs = args.shift(),
			obj = {$:name};

		// attrs
		for (var key in attrs)
			obj[key] = ko.observable(attrs[key]);

		// tagname children
		for (var i=0; i < args.length; i++) if (args[i]) {
			var child = args[i];
			var prop = '_' + child.$;

			if (! (prop in obj) ) obj[prop] = ko.observableArray();
			obj[prop].push(child);
		}

		// children
		obj._ = ko.observableArray(args);

		return obj;
	}
});
