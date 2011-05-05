/* Widget.js

A file created to simplify the "controllers" used in this application.
*/

steal('../../api/jquery/jquerymx-1.0.custom.min.js').then(function() {

$.WvWidget = function(name, view, observers, events, methods) {
   //TODO: Add super methods.
   var superMethods = {
      destroy : function() {
         var data = $(this).data('widget-'+name);
         for (var i = 0; i < data._binds; i++) {
            var bind = data._binds[i];
            bind[1].unobserve(bind[0]);
         }

         $.removeData($(this).text(''), 'widget-'+name);
      }
      option : function(key, value) {
         if (value != undefined) {
            var data = new KVO($(this).data('widget-'+name));
            var obj = data;
            var keys = key.split('.');

            for (var i=0; i < keys.length; i++) obj = obj.get(keys[i]);
            obj.set(value);

            data = data._obj;
            $(this).html(view, data).data('widget-'+name, data);
         }
         else {
           var obj = new KVO($(this).data('widget-'+name));
           var keys = key.split('.');

           for (var i=0; i<keys.length; i++) obj = obj.get(keys[i]);
           return obj;
         }
      }
   }

   $[name] = function() {
      var method = arguments.pop();
      if (typeof method === 'String') {
         return methods[method].apply(this, arguments);
      }
      else {
         $(this).html(view, method);
         
         //add observers
         method._binds = [];
         for (var key in observers) {
            var obj = new KVO(method);
            var keys = key.split('.');
            
            for (var i=0; i < keys.length; i++) {
               obj = obj.get(keys[i]);
            }

            var bind = obj.observe(function() {
               observers[key].apply(this, arguments);
            }));
            method._binds.push([bind, obj]);
         }

         //add events
         var eventRE = /^(.*) (\w*)$/
         for (var event in events) {
            var evt = eventRE.exec(event);

            $(this, evt[0]).live(evt[1], events[event]);
         }
         
         $(this).data('widget-'+name, method);
         methods.init.apply(this, method);
         return this;
      }
   }

}

});