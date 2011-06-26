/*Handlers to display element objects. TODO: rename to elements.js*/

/*Mapping of Element types to handler functions.*/
EL_TYPES = {
   /*An attached file.*/
   "attachment" : function(el) {
      return $('<iframe>').attr('src', el.url);
   },
   /*A collaborative "gadget"*/
   "gadget" : function(el) {
      return $('<iframe>').gadget(el.url, el.state);
   },
   /*A form control.*/
   "control" : function(el) {
      return $('<p>').append("control.ejs", el);
   }
}