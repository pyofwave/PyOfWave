/*Handlers to display element objects. TODO: rename to elements.js*/
EL_TYPES = {
   attachment : function(el) {
      return $('<iframe>').attr('src', el.url);
   },
   gadget : function(el) {
      return $('<iframe>').gadget(el.url, el.state);
   },
   control : function(el) {
      return $('<p>').append("control.html", el);
   }
}