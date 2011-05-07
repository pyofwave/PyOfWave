/*Main file of PyOfWave client. Please acknowledge that I've chosen my own folder structure which I think will work well for PyOfWave over the preset.*/

/*Specific details for the sections are in sections.js.*/
steal('../api/jquery/jquerymx-1.0.custom.min.js', '../api/jquery/jquery-1.5.min.js' 'api/widget.js', 'sections.js').then(function() {
$.fn.section = function(id, creator) {
      var toolbar = $('<div>').id('client-toolbar');
      for (var i=0;i < creator.toolbar.length;i++) 
         toolbar.append(creator.toolbar[i]);

      $(this).append($('<div>').append(toolbar).append(creator()).id(id));
}
$.Controller('Splitter', {
   init : function() {
      this.down = false;
   },
   mousedown : function() {
      this.down = true;
   },
   mouseup : function() {
      this.down = false;
   },
   mousemove : function(evt) {
      if (this.down) {
         var prev = $(this.element).prev();
         $(prev).style('width', event.mousex - $(prev).position().left);
         // With float, other side should change too.
      }
   }
});

$(document).ready(function() {
   $('#client').section('inbox', sections.inbox)
   .section('waves', section.waves))
   .append($('<div>').Splitter({dir : "v"}))
   .section('wave', section.wave));
});
});

navigator.registerURLHandler("wave", "wave.html#%s");