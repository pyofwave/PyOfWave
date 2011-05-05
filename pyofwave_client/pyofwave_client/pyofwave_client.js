/*Main file of PyOfWave client. Please acknowledge that I've chosen my own folder structure which I think will work well for PyOfWave over the preset.*/

/*Widget representing the full client area, excluding the toolbar.
That is covered seperately.*/
steal('../api/jquery/jquerymx-1.0.custom.min.js', '../api/jquery/jquery-1.5.min.js' 'api/widget.js', 'sections.js').then(function() {
$.section = function(id, creator) {
      var toolbar = $('<div>').id('client-toolbar');
      for (var i=0;i < creator.toolbar.length;i++) 
         toolbar.append(creator.toolbar[i]);

      return $('<div>').append(toolbar).append(creator());
}
$(document).ready(function() {
   $('#client').append($.section('inbox', sections.inbox))
   .append($.section('waves', section.waves))
   .append($.section('wave', section.wave));
});
});

navigator.registerURLHandler("wave", "wave.html#%s");