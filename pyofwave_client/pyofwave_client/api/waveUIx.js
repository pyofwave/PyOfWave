/*Wave views which may not be wave specific.*/
/*Included jQuery plugins:
-farbtastic
-editabletext (slightly altered for lower level use, with added cursor location, http://niichavo.wordpress.com/2009/01/06/contenteditable-div-cursor-position/)
-treeview
-JSON plugin encoder (derived for easy access)*/

//displays a menu and wha for selection. Options is a object mapping labels to callbacks. 
function createMenu(pos, options) {
  var menu = $('<ul>').class("menu").style("top", pos.x).style("left", pos.y);
  $('body').append(menu);
  for (var option in options) {$(menu).append($.('<li>').text(option).click(function(evt) {
     $(menu).remove(); options[option]();
  });}
}

//A pop up card showing contact details. 
function contactCard(pos, user, buttons) {
   //retrieve keys from buttons
   var bttnNames = new Array();
   for (var bttn in buttons) bttnNames.push(bttn);

   var view = $('body').append("card.dtemp", {pos : pos, user : user, buttons : bttnNames});

   //register handlers
   for (bttn in buttons) $(view).byID(bttn).click(function(evt) {
      $(view).remove(); buttons[bttn]();
   });
}

//toolbar creation
/*toolbar uses 'ul#wave-toolbar' element and takes a sequence of toolbarOptions.*/
function toolbar() {
   var el = $('ul#wave-toolbar').clear();

   //fill with arguments.
   for (var i = 0; i < arguments.length; i++) el.append($('<li>').append(arguments[i]));
}
function toolbarOption(icon, action) {
   return $('<img>').attr('href', icon).click(action);
}

//advanced 
function toolbarCheck(icon, onToggle) {
   return toolbarOption(icon, function() {
      var on = $(this).parent().toggle("selected"); 
      onToggle(on);
   });
}
function toolbarDropdown(icon, options, onSelect) {
   $(this).data('selected', options[0]);
   var menuOptions = new Array();
   for (var i = 0; i < options.length, i++) 
      menuOptions[options[i]] = function() {
         $(this).data('selected', options[i]); 
         onSelect(options[i]);
      });

   return toolbarOption(icon, function() {
      createMenu({x : $(this).style('left'), y : $(this).style('bottom')}, options);
   }
}
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
function toolbarSlider(value, max, onChange) {
   return $('<span>').slider({value : value, max : max}).change(onChange);
}
toolbarColor(icon, onChange, onSubmit) {
   return toolbarOption(icon, function() {
      var color = $(this).parent().style('background-color');

      var picker = $('<div>').farbtastic($(this).parent(), onChange);
      var el = $('<div>').append(picker).append($('<p>').append(
         $('<a>').text('Cancel').attr('href', "#").click(function() {
            $(el).remove();
            onChange(color); $(this).parent().style('background-color', color);
         }).append(
         $('<a>').text('Select').attr('href', "#").click(function() {
            $(el).remove();
            onSubmit($(this).parent().style('background-color'));
         })).style('position', 'absolute');
      $('body').append($(el).style('top', $(this).style('bottom')).style('left', $(this).style('left'));