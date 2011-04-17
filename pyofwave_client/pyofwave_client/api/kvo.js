/*Small class which wraps dynamic objects to form loose coupling between model and view.*/

/*Wraps a value and adds "observers"*/
$.Class('KVO', {
   /*Initializes KVO with an object.*/
   init : function(obj) {
      this._observers = new Array();
      this._binds = {}
      this.set(obj);
   }
   /*Returns a property of this._obj*/
   get : function(key) {return this._obj[key];}
   /*Adds a function as a observer and returns an "ID"*/
   observe : function(cb) {return this._observers.push(cb);}
   /*Removes a function with an "ID".*/
   unobserve : function(id) {this._observers.remove(this._observers[id]);}
   /*Sets this to refer to a different value and notifies observers.*/
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
   /*Observer for all children of the represented value.*/
   _notify : function(obj) {
      //called when a property of obj changes, via observer system. """
      var key;
      for (var _key in this._obj) if (this.get(_key) === obj) {key = _key; break;}

      for (var o in this._observers) o(this, key, obj);
   }
}