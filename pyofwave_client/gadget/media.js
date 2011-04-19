/*Loads various types of files for the gadget, as well as the gadget and API themselves.*/

/*Load a resource at URL with a MIME type of type.*/
function load(url, type) {
   load.loaders[type.split("/")[0]](url, load.loaders[type])
}
load.loaders = {}
/*The plain text loader.*/
load.loaders.text = function(url, loader) {
    $.get(url, "", loader);
}

/*The JavaScript generator.
  TODO: Figure out how to write this tidily, perhaps by Python or a hint from CoffeeScript.*/
load.loaders["text/javascript"] = function(text) {
    function replaceRegex(pattern, params, callback) {
      //find pattern in text
      //find params
      //replace matched string with return of callback
   }
   function insertAfter(text, after, text) {
      //find charactor
      //insert after it.
   }

   var sharedMethods = sharedMethods.keys();
   replaceRegex(/^;\w*sharedMethods\.\n+\w*=\w*function(.*) {.*}$/, [/^\.\n$/, /^(.*)$/], function(text, method, args) {
      sharedMethods.push(method.substr(1,method.length);
      //do not overwrite existing.
      text = insertAfter(text, "{", "if (this"+method+") this"+method+args+";//PRESERVE");
      return text;
   });
   replaceRegex(/^;.+=[.|\{.*\}|(.*)|'.*'|".*"]+;$/, [], function(text) {
      //replace = with .set()
   });
   for (var i=0; i < sharedMethods.length; i++) {
      method = sharedMethods[i];
      replaceRegex("."+method, [/;.*;/, /^\\\\PRESERVE$/], function(text, preserve) {
         if (preserve) return text;
         //split by method
         //place call at beginning and call "sharedMethods."method".call(" obj", " args")"
      });
   }

    eval(text);
    return self;
}

/*Create shared methods for use by JavaScript interpretor.*/
var sharedMethods = {}
/*Get all keys of an object.*/
sharedMethods.keys = function() {
   var keys = ["keys",];
   for (var key in this) keys.push key;
   return keys;
}