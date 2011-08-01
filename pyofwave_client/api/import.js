/* Simple JavaScript which imports javascripts during development, imports are replaced by the script by compress.py for production. 
 * Should not be used in production, internet delay may (probably will) cause bugs. */
function import() {
  for (var i; i < arguments.length; i++) {var m = arguments[i];
    $('head').append($('<script>').attr('type', 'text/javascript').attr('src', m));
  }
}
