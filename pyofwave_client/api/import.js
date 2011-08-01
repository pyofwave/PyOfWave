/* Simple JavaScript which imports javascripts during development, imports are replaced by the script by compress.py for production. */
function import() {
  for (var i; i < arguments.length; i++) {var m = arguments[i];
    var request = new XMLHTTPRequest();
    request.open("get", m, false);
    request.send();
    new Function(request.responseText)()

    import.loaded.push(m);
  }
}
import.loaded = new Array();