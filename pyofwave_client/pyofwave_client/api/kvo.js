/*Small class which wraps dynamic objects to form loose coupling between model and view.*/

$.Class('KVO', {
   init : function(obj) {
      this._observers = new Array();
      this._binds = {}
      this.set(obj);
   }
   get : function(key) {return this._obj[key];}
   observe : function(cb) {return this._observers.push(cb);}
   unobserve : function(id) {this._observers.remove(this._observers[id]);}
   set : function(obj) {
      for (var id in this._binds) this.get(this._binds[id]).unobserve(id); //unbinds this from previous value

      //set new oject, and properly wrap properties. 
      this._obj = {};
      for (var key in obj) {
         if (!["String", "Integer"].contains(typeof obj[key]) || obj[key].class != "KVO") {
            this._obj[key] = new KVO(obj[key]);
            bind = this._obj[key].observe(this.callback(this._notify));
            this._binds[bind] = key;
         }
         else this._obj[key] = obj[key];
      }

      for (var o in observers) o(this);  //notify observers. 
   }
   _notify : function(obj) {
      //called when a property of obj changes, via observer system. """
      var key;
      for (var _key in this._obj) if (this.get(_key) === obj) {key = _key; break;}

      for (var o in this._observers) o(this, key, obj);
   }
}