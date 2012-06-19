define(['sample/contacts', '../api/knockout-2.1.0', '../api/jquery-1.5.1', '../api/splitter'], function(contacts, ko) {
	var groups = contacts._;

	var mapped = {
		'groups' : groups,
		'contacts' : ko.observable(groups()[0]),
		'contact' : ko.observable(),

		addGroup : function() {
			this.groups.push({
				name: ko.observable("Untitled"), _: ko.observableArray()
			});
		},
		addContact : function() {
			this.contacts()._.push({foaf_name : ko.observable("Some One"),
				foaf_mbox : ko.observable("account@provider.com"),
				foaf_depiction : ko.observable("avatars/unknown.png")
			})
		}
	};

	/* UI */
	$(function() {
	ko.applyBindings(mapped);

	// Main vertical splitter, anchored to the browser window
	$("#content").splitter({
		type: "v",
		sizeLeft: 200, 
		anchorToWindow: true,
		accessKey: "L"
	});
	// Second vertical splitter, nested in the right pane of the main one.
	$("#people").splitter({
		type: "v",
		sizeLeft: 200,
		accessKey: "R"
	});
	});

	/* custom bindings */
	ko.bindingHandlers.edit = {
		init: function(element, valueAccessor) {
			function handler() {
				function close() {
					$(input).replaceWith(element);
					accessor($(input).val());
				}

				var input = $('<input>').val(accessor()).keydown(function(e) {
					if (e.which == 13) close();
				}).click(function(e) {
					e.stopPropagation();
				}).width($(element).width() - 10);

				$(input).insertBefore(this); $(this).detach();
				$(document).click(close);
			}

			var accessor = valueAccessor();
			$(element).dblclick(handler);
		}
	}
});
