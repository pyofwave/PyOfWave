/* Provides functions managing each section of the UI. */

// TODO: fill in utilities. 

function inboxes() {
   function inbox(obj) {
      //generate list items. 
   }
   // Load the root inbox. 

   return $('<ul>').append(inbox(root)).tree();
}
inboxes.toolbar = [
   $('<input type="search" name="search" value="in:inbox" />').submit(search);
]

function waves() {
   return $('<table>').table({rowLoader : waveLoader, 
      headers : ["unread", "sample", "last changed"],
      rowClick : showWave});
}
inbox.toolbar = [
   // TODO: full in options.
]

function wave() {
   return $('<div><div id="toolbar"></div>').append(
      $('<div>').BlipView({blipId : selwave.rootBlipId}));
}
wave.toolbar = [
   $('<div>').participantsListView({participants : selwave.participants}),
   $('<img>').attr('href', "playback.png").click(playback);
   $('<img>').attr('href', "rss.png").click(follow("RSS")),
   $('<img>').attr('href', "popout.png").click(follow('HTML'))
] 
]