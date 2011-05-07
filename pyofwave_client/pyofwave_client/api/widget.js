/* Widget.js

A file created to simplify the "controllers" used in this application.
*/

steal('../../api/jquery/jquerymx-1.0.custom.min.js').then(function() {

$.WvWidget = function(name, view, observers, events, methods) {
   $.extend(methods, events);
   if (methods.init) methods._init_ = methods.init;
   $.extend(methods, {
      init : function(el, options) {
         $(el).html(view, options);

         //register observers
         this.observers = observers;
         this.options = new KVO(options);
         this.binds = {};

         for (var key in this.observers) {
            var obj = this.options;
            $.foreach(key.split('.'), function(attr) {
               obj = obj.get(attr);
            });
            this.binds[key] = obj.set(this.observers[key]);
         });
      },
      destroy : function() {
         this.super();
         for (var key in this.binds) {
            var obj = this.options;
            $.foreach(key.split('.', function(attr) {
               obj = obj.get(attr);
            });
            obj.unobserve(this.binds[key]);
         }
      }
      option : function(key, val) {
         var obj = this.options;
         $.foreach(key.split('.'), function(attr) {
            obj = obj.get(attr);
         });

         if (val != undefined) obj.set(val);
         return obj;
      }
   });

   $.Controller(name, methods);
}

});