/* Simple JavaScript which imports javascripts during development, imports are replaced by the script by compress.py for production. 
 * Should not be used in production.
/* This script will be the only place we pamper to IE, and doesn't use jQuery since we'll import that. */
(function() {
  var request = null;
  var loaded = [];

  // create the request object.
  try {
    request = new XMLHttpRequest();
  } catch (trymicrosoft) {
    try {
      request = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (othermicrosoft) {
      request = new ActiveXObject("Microsoft.XMLHTTP");
    }
  }

  // import script
  window.import = function() {
    for (var script in arguments) {
      if (loaded.indexOf(script) <= 0) {
        request.open("GET", script, false);
        request.send();

        (window.execScript || function(data) {
          window["eval"].call(window, data);
        })(request.responseText);

        loaded.push(script);
      }
    }
  }
})();
