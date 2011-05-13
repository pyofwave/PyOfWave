/*Wave views which may not be wave specific.*/

steal('../../api/jquery/jquery-1.5.min.js', 
'../../api/jquery/jqueryui-1.8.12.custom.min.js', //TODO: Include jQueryUI slider, doesn't unzip on my machine.
'../../api/jquery/farbtastic.js').then(function() {
/*displays a menu for selection. Options is a object mapping labels to callbacks. */
function createMenu(pos, options) {
  var menu = $('<ul>').class("menu").style("top", pos.x).style("left", pos.y);
  $('body').append(menu);
  for (var option in options) {$(menu).append($.('<li>').text(option).click(function(evt) {
     $(menu).remove(); options[option]();
  });}
}

/*A pop up card showing contact details. */
function contactCard(pos, user, buttons) {
   //retrieve keys from buttons
   var bttnNames = new Array();
   for (var bttn in buttons) bttnNames.push(bttn);

   var view = $('body').append("card.ejs", {pos : pos, user : user, buttons : bttnNames});  //TODO: Implement card.ejs

   //register handlers
   for (bttn in buttons) $(view).byID(bttn).click(function(evt) {
      $(view).remove(); buttons[bttn]();
   });
}

//toolbar creation
/*toolbar uses 'ul#wave-toolbar' element and takes a sequence of toolbarOptions to populate it. (for flexibility)
  This is the 'sub' toolbar for the wave section, used for editting and playback.*/
function toolbar() {
   var el = $('ul#wave-toolbar').clear();

   //fill with arguments.
   for (var i = 0; i < arguments.length; i++) el.append($('<li>').append(arguments[i]));
}
/*A toolbar option in above.*/
function toolbarOption(icon, action) {
   return $('<img>').attr('href', icon).click(action);
}

//advanced 
/*A toolbar option that can be toggled on and off.*/
function toolbarCheck(icon, onToggle) {
   return toolbarOption(icon, function() {
      var on = $(this).parent().toggle("selected"); 
      onToggle(on);
   });
}
/*A toolbar option that contains a menu.*/
function toolbarDropdown(icon, options, onSelect) {
   $(this).data('selected', options[0]);
   var menuOptions = new Array();
   for (var i = 0; i < options.length, i++) 
      menuOptions[options[i]] = function() {
         $(this).data('selected', options[i]); 
         onSelect(options[i]);
         //TODO: Check selected option.
      });

   return toolbarOption(icon, function() {
      createMenu({x : $(this).style('left'), y : $(this).style('bottom')}, options);
   }
}
/*A toolbar checkbox of which only one in a group can be checked.
  A group is identified by a name.*/
function toolbarRadio(icon, name, onSelect) {
   //create and return toolbarCheck.
   var el =  toolbarOption(icon, function() {
      $('#wave-toolbar .selected .' + name).removeClass('selected');
      $(this).parent().toggleClass('selected'); //TODO: ensure deselect works. 
      OnSelect();
   });
   el.parent().class(name);
   return el;
}
/*An element for the toolbar that includes a jQuery UI slider.*/
function toolbarSlider(value, max, onChange) {
   return $('<span>').slider({value : value, max : max}).change(onChange);
}
/*A toolbar option that drops down a Farbtastic colour picker.*/
toolbarColor(icon, onChange, onSubmit) {
   return toolbarOption(icon, function() {
      var color = $(this).parent().style('background-color');  //get current colour to revert

      var el = $('<div id="picker-box"><div id="picker"></div><p><a>O. K.</a><a>Cancel</a></p></div>')
      $(el, "#picker-box").farbtastic($(this).parent(), onChange);  //create the picker
      $('body').append($(el).style('top', $(this).style('bottom')).style('left', $(this).style('left')));  //Display the dropdown
   });
}
});