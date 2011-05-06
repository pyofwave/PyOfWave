/* Provides functions managing each section of the UI. */

// TODO: fill in utilities. 
function search(query) {
   sendOperations("robot.search", {
      query : query,
      index : $.table.top(),
      numResults : $.table.height()
   }, function(response) {
      $.table.setRows(response.results);
   }]);
}

function newWave() {
   sendOperations("robot.createWavelet", {}. function() {
      $.table.selected({waveId : wave.waveId});
   });
}

$.Controller('table', {
   init : function(el, ops) {
      $.table = this;
      this.headers = {};
      for (var header in ops.headers) 
         this.headers[header] = ops.headers[header].split('?');
      this.rowHeight = $(el, 'tr').style('height');

      // set initial values.
      this._selected = [];
      this._top = 0;
      this.resize();
   },
   setRows : function(rows, index, height) {
      index |= this.top();
      height |= this.height();

      var replace = $(this.el, 'tr').slice(index, index + height);

      // generate rows.
      var rowEl = $('<div>');
      $.foreach(rows, function(row) {
         var el = $('<tr>').data('table-data', row)

         for (var header in this.headers) {
            var td = $('td');
            $.foreach(this.headers[header], function(key) {
               if (!row[key].find('?')) td.append(row[key]);
               else {
                  var key = key.split('?')
                  if (row[key[0]]) td.append($('<img>').attr(key[1]);
               }
            });
         }
         $(rowEl).append();
      });

      $(rowEl, 'tr').replace(replace);
   },
   selected : function() {
      return $(this.el, '.selected');
   },
   top : function(val) {
      if (val != undefined) this._top = val;
      else return this._top;
   },
   height : function() {
      if (val != undefined) this._height = val;
      else return this._top;
   },

   'scroll' : function() {
      this.top(($(this.el).offset().top / this.rowHeight
      ).toDecimalPlaces(0));
   },
   resize : function() {
      this.height(($(this.el).style('height') / this.rowHeight
         ).toDecimalPlaces(0);
   },
   'tr click' : function(evt) {
      if (!evt.shiftKey)
         $(this.el, '.selected').removeClass('selected');

      $(evt.target).toggleClass('selected');
      $(this.el).change();
   }
});
var selWave = new KVO({});

// Define sections.
function inboxes() {
   function inbox(obj) {
      var icon = obj.shift();
      var name = obj.shift();
      var query = obj.shift();
      var children = obj.shift();

      var el = $('<li>').append($('<img>').attr('href', icon)).append(name).click(function() {
         $('#client-search').attr('value', query).submit();
      });

      $.foreach(children, function(child) {
         $(el).append(inbox(child));
      });
      return el;
   }
   // Load the root inbox. 
   var el = $('<ul>').treeview();
   sendOperations(
      ["robot.fetchFolders", {}, function(response) {
         el.append(inbox(response.folder));
      }]
   );

   return el;
}
inboxes.toolbar = [
   $('<form id="client-search"><input type="search" name="search" value="" /></form>').submit(search)
]

function waves() {
   return $('<table>').table({
      headers : {"unread" : "unreadCount?unread.png", "wave" : "title snippet", "last changed" : "lastModified"},
      }).scroll(function(evt) {
         sendOperations(["robot.search", {query : $('#client-search').serialize()['search'],
               index : $.table.top(),
               numResults : $.table.height()}, 
            function(response) {
               $.table.setRows(response.results, index, numResults);
            }]
         );
      }).change(function() {
         selWave.set($($.table.selected()[0]).data('table-data').waveId);
      });
}
inbox.toolbar = [
   $('<img>').attr('href', 'plus.png').click(newWave),
   $('<img>').attr('href', 'folder.png').click(function() {
      function sendMenuOperation(op, tag) {
         return function() {
            args = {
               modifyHow : op,
               waveId : $.table.selected().join(" ")
            }
            if (tag) args.tag = prompt("Enter tag(s):");

            sendOperations(["robot.folderAction", args, function() {}]);
         }
      }

      createMenu({x : $(this).style('left'), y : $(this).style('bottom')}, {
         "Mark as Read" : sendMenuOperation("markAsRead"),
         "Mark as Unread" : sendMenuOperation("markAsUnread"),
         Mute : sendMenuOperation("mute"),
         "Add Tag" : sendMenuOperation("addTag", true),
         "Remove Tag" : sendMenuOperation("removeTag", true),
         "Add Public Tag" : sendMenuOperation("addPublicTag", true),
         "Remove Public Tag" : sendMenuOperation("removePublicTag", true)
      });
   }).class('left');
]

function wave() {
   return $('<div><div id="toolbar"></div>').append(
      $('<div>').BlipView({blipId : selwave.rootBlipId}));
}
wave.toolbar = [
   $('<div>').participantsListView({participants : selwave.participants}),
   $('<img>').attr('href', "playback.png").click(playback).class('left'),
   $('<img>').attr('href', "rss.png").click(follow("RSS")).class('left'),
   $('<img>').attr('href', "popout.png").click(follow('HTML')).class('left')
] 
]