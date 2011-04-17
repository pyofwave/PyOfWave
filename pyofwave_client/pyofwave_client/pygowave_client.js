/*Main file of PyOfWave client. Please acknowledge that I've chosen my own folder structure which I think will work well for PyOfWave over the preset.*/

/*Controller representing the full client area, excluding the toolbar.
That is covered seperately.*/
$.Controller('client', {
   
});
$(document).ready(function() {
   $('#client').client().toolbar();
}