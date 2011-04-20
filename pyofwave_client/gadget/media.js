/*Loads various types of files for the gadget, as well as the gadget and API themselves.*/
function load(url, type) {
   load.loaders[type.split("/")[0]](url, load.loaders[type])
}
load.loaders = {}
load.loaders.text = function(url, loader) {
    $.get(url, "", loader);
}

load.loaders["text/javascript"] = function(script) {
    function processString(string, pattern, callback) {
      //Seperate content between curly brackets (they complicate regex)
      
      //Retrieve from cache if possible
      //Generate main regex
      //Generate parameter regex pairs
      //Add to cache
      
      //If curly brackets in pattern, replace one level of curly brackets.
      
      //Match regex
      //Extract parameters
      //Call callback.
   }  //TODO: Implement
   function process(pattern, callback) {
      script = processString(script, pattern, callback);
   }

   //Replace = with set method.
   script.replace( /\w*=\w*/, ".set(");
   process(";(.+);", function(text) {
      var unmatched = text.match("(").length - text.match(")").length;
      return ";"+text+(")" * unmatched)+";";
   });
   
   //retrieve all shared method names
   var shared = sharedMethods.keys();
   process("sharedMethod.(\w+)\w*=\w*function\((.*)\)\w*{(.*)}",
     function(method, args, code) {
       shared.push(method);
       return "sharedMethods."+method+"=function("+args+"){" +
         "if(this."+method+"!=undefined) return this."+method+"("+args+");"
         +code+"}"
    });
    
    //correct calls to sharedMethods
    var methRegex = shared.join("|");
    process(";\w*(.+).(["+methRegex+"])\((.*)\)", function(obj, method, args) {
      return ";sharedMethods."+method+".apply("+obj+",["+args+"])";
    });
   
   return self;
}
var sharedMethods = {}
sharedMethods.keys = function() {
   if (this.keys != undefined) this.keys();  //Don't overwrite children.
   
   var keys = ["keys",];
   for (var key in this) keys.push(key);
   return keys;
}