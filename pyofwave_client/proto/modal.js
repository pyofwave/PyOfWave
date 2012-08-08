define(['../src/api/jquery-1.5.1.js', '../src/api/jqueryUI/jquery-ui-1.8.14.custom.js', '../src/api/farbtastic.js'], function($) {
	var $overlay = $('<div>').css({
				position: 'absolute', top: 0, left: 0, 
				width: window.innerWidth, height: window.innerHeight, 
				background: 'black', opacity: 0.1})

		$.fn.popover = function popover($el) {
			$el.hide()
			return function(evtOrEl) {
				$el.fadeIn().click(function(evt) {evt.stopPropagation()})
					.position({of: evtOrEl, offset: "0 10", collision: "fit",
						my: 'top', at: 'bottom'})
				$overlay.fadeIn()
					.one('click', function(e) {
						e.stopPropagation()
						$(this).add($el).fadeOut()
					})
			}
		}
		$(function() {
			$overlay.prependTo('body').hide()
		})
}
