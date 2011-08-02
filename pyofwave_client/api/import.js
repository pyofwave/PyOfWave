/* Simple JavaScript which imports javascripts during development, imports are replaced by the script by compress.py for production. 
 * Should not be used in production, internet delay may (probably will) cause bugs. */
function import() {
  for (var i; i < arguments.length; i++) {var m = arguments[i];
    document.write("<script type='text/javascript' src='"+ m +"'></scr"+"ipt>");
  }
  // waste some time in waiting
  for (var i; i < 500; i++) {}
  // alert("Waiting for scripts to load. . ."); // uncomment if import problems are experienced
}
