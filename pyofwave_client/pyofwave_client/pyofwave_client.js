/*Main file of PyOfWave client. Please acknowledge that I've chosen my own folder structure which I think will work well for PyOfWave over the preset.*/

/*Widget representing the full client area, excluding the toolbar.
That is covered seperately.*/
steal('../api/jquery/jquerymx-1.0.custom.min.js', '../api/jquery/jquery-1.5.min.js').then(function() {
$.Controller('client', {
   
});
$(document).ready(function() {
   $('#client').client().toolbar();
});
});