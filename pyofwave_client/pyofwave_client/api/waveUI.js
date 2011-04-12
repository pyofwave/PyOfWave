/*Wave views which presents a wave to the user and allows editing.*/
/*Each displays a particular piece of the wave structure*/
var sessionId; //to be provided by server

$.Controller('WaveletView', {
   init : function(el, options) {
      $(el).append("waveletView.html");

      $(el, '.participants').ParticipantsBar({participants : options.wavelet.get("participants")});
      $(el '.blips').BlipView({id : options.wavelet.get("rootBlipId")});
});
$.Controller('ParticipantsBar', {
   init : function(el, options) {
      $(el).append("participants.html", {participants : options.participants});
      this.kvoID = options.participants.observe(function(obj, index, value) {
         if (value) {
            //redraw participant value at index
         }
         else $(el.children[index]).remove();
      });
   }
});
$.Controller('BlipsListView', {
   init : function(el, options) {
      $(el).append("blipsList.html", {blips : options.blips});

      this.kvoID = options.blips.observe(function(obj, index, value) {
         if (value) {
            //redraw blip at Index
         }
         else $(el.children[index]).remove();
      });
   }
});

$.Controller('BlipView', {
   init : function(el, options) {
      if (options.blip && options.blip.class == "KVO") var blip = options.blip;
      else if (options.id) var blip = blips[options.id];
      else var blip = blips[options.blip];

      $(el).append("node.html", {blip : blip,});
      this.blip = blip;

      //tie to observers
      var kvoIDs = new Array();
      renderContent = this.callback(this.renderContent);
      renderContent();

      kvoIDs.push(blip.get('annotations').observe(renderContent));
      kvoIDs.push(blip.get('elements').observe(renderContent));
      kvoIDs.push(blip.get('content').observe(renderContent));
   },
   '> .blip .content click' : function(evt) {
      createMenu({x:evt.mousex, y:evt.mousey}, {
         reply : function() {
            sendOperations(["document.modify", {
               waveId : this.blip.get('waveId'),
               waveletId : this.blip.get('waveletId'),
               blipId : this.blip.get('blipId'),
               index : //calculate index of selection. ,
               modifyHow : {
                  elements : [{
                     type : "thread",
                     children : new Array()
                  },],
               }
            }]);
         },
         edit : this.callback(this.edit)
      }]);
   },
   '> .blip .status click' : function(evt) {
      //generate menu. 
      el = $(el '> .blip .status');
      createMenu({x : el.style('left'), y : el.style('bottom')}, {
         edit : this.callback(this.edit),
         reply : function() {
            $(this.el, '> .thread').BlipsListView('newBlip');
         },
         delete : function() {
            sendOperations(["blip.remove", {
               waveId : this.blip.get('waveId'),
               waveletId : this.blip.get('waveletId'),
               dblipId : this.blip.get('blipId')
            }]);
         },
         'copy link' : function() {
            prompt("The URL for this blip is: ", "wave://"+this.blip.get('blipId'));
         }
   }
}).extend({
   renderContent : function() {
      var content = this.blip.get('content');
      var lastIndex = 0;
      var prevChild = $();
      var el = $('<p>').data('start', 0);

      //apply annotations.
      for (var i=0; i<this.blip.annotations._object.length; i++) {
         var annotation = blip.get('annotations').get(i);
         var child = $('<span>').text(content.substr(annotation.range.start, annotation.range.end)
            ).data('start', annotation.get('range').get('start');
         
         //apply style
         switch annotation.get('key') {
         case "style/background":
            child.style('background-color', annotation.get('value'));
            break;
         case "style/color":
            child.style('color', annotation.get('value'));
            break;
         case "style/fontFamily":
            child.style('font-family', annotation.get('value'));
            break;
         case "style/fontSize":
            child.style('font-size', annotation.get('value'));
            break;
         case "style/fontStyle":
            child.style('font-style', annotation.get('value'));
            break;
         case "style/fontWeight":
            child.style('font-weight', annotation.get('value'));
            break;
         case "style/textDecoration":
            child.style('text-decoration', annotation.get('value'));
            break;
         case "style/verticalAlign":
            child.style('vertical-align', annotation.get('value'));
            break;

         case "user/d/" + sessionId:
            break;
         case "user/r/" + sessionId:
            child.style('border-color', getUser(annotation.get('value')).color).style('border', "thin solid");
            break;
         case "user/e/" + sessionId:
            child.append($('<span>').style('background-color', getUser(annotation.get('value')).color));
            break;

         case "link/manual":
            child.click(function() {location.replace(annotation.get('value'));});
            break;
         case "link/auto":
            child.click(function() {location.replace(location.replace($(this).text());});
            break;
         }

         //select element to add child to
         var parent;
         var start = annotation.get('range').get('start');
         if (lastIndex > start) 
            for (parent = prevChild; ! $(parent).data('start') <= start; parent = $(parent).parent()) {}
         else parent = el;

         //add child to parent
         start = parent.data('start');
         range = annotation.get('range')
         parent.replace(range.get('start') - start, range.get('end') - start, child);
      }

      //apply elements.
      for (i=0; i < this.blip.get('elements')._obj.length; i++) {
         var element = this.blip.get('elements').get(i);
         el.replace(element.get('index'), element.get('index'), 
            EL_TYPES[element.get('type')](element));
      }
   },
   edit : function() {
      function sendModification(modification) {
         sendOperations(
            ["document.modify", {
               waveId : this.blip.get('waveId'),
               waveletId : this.blip.get('waveletId'),
               blipId : this.blip.get('blipId'),
               range : $(this, '[contenteditable]').editableText('selection'),
               modifyHow : modification
            }]
         );
      $(this.blip, ' > .blip .content').editableText().change(function(evt) {
         sendModifications({content : evt.text,});
      });

      //create edit toolbar.
      createToolbar(
         toolbarCheck("imgs/edit/bold.png", function(checked) {
            sendModifications({annotation : {name : 'style/bold', value : checked},});
         }),
         toolbarCheck("imgs/edit/italic.png", function(checked) {
            sendModifications({annotation : {name : 'style/italic', value : checked},});
         }),
         toolbarCheck("imgs/edit/underline.png", function(checked) {
            sendModifications({annotation : {name : 'style/underline', value : checked},});
         }),
         toolbarSeperator(),
         toolbarColor("imgs/edit/text.png", "000000", function(color) {$(this, '[contenteditable]').editableText('selElement').style('color', color);}, 
            function(color) {
               sendModifications({annotation : {name : 'style/color', value : color},});
         }),
         toolbarColor("imgs/edit/background.png", "FFFFFF", function(color) {
               $(this, '[contenteditable]').editableText('selElement').style('background-color', color);
            }, 
            function(color) {
               sendModifications({annotation : {name : 'style/color', value : color},});
         }),
         toolbarSeperator(),
         toolbarDropdown("imgs/edit/textSize.png", range(1, 42), function(size) {
            sendModifications({annotation : {name : 'style/fontSize', value : size},});
         }),
         toolbarDropdown("imgs/edit/textFamily.png", [], function(family) {
            sendModifications({annotation : {name : 'style/fontFamily', value : family},});
         }),
         toolbarDropDown("imgs/edit/textStyle.png", [], function(style) {
            sendModifications({lineStyle : style});
         }),
         toolbarSeperator(),
         toolbarOption("imgs/edit/indent.png", function() {
            sendModifications({lineIndent : $(this, '[contenteditable]').editableText('indent') + 1,});
         }),
         toolbarOption("imgs/edit/dedent.png", function() {
            sendModifications({lineIndent : $(this, '[contenteditable]').editableText('indent') - 1,});
         }),
         toolbarSeperator(),
         toolbarOption("imgs/edit/link.png", function() {
            var url = prompt("Enter a URL, or web address, for the link. (Default is selected text");
            if (url) sendModifications({annotation : {name : 'link/manual', value : url},});
            else sendModifications({annotation : {name : 'link/auto', value : true},});
         }),
         toolbarOption("imgs/edit/unlink.png", function() {
            sendModifications({annotation : [{name : 'link/manual', value : False},
               {name : 'link/auto', value : False}],});
         }),
         toolbarOption("imgs/edit/attach.png", function() {
            createMenu({x : $(this).style('left'), y : $(this).style('bottom')}, {
               gadget : function() {
                  sendModifications({elements : {type : 'gadget', src : prompt(
                     "Please enter Gadget address.")},});
               },
               attachment : function() {
                  sendModifications({elements : {type : 'attachment', src : prompt(
                     "Please enter Gadget address.")},});
               }
            });
         })
      )
   },
});

$.Controller('GadgetView', {
   init : function(el, options) {
      $(el).append("gadget.html", options);
      $(el, 'iframe').get()[0].message = function(text) {
         var public, name, value;
         [public, name, value] = text.spllit(',');
         var doc = public == "public" ? options.publicDoc : options.privateDoc;
         doc[name] = value;

         //update server
         sendOperatioins(
            ['wavelet.setDataDoc', {
               waveId : options.blip.get('waveId'),
               waveletId : options.blip.get('waveletId'),
               dataDocName : doc.__name__,
               dataDocValue : doc
            }]);
   }
}).extend({
   update : function(delta) {
      $(this.el, 'iframe').get()[0].postMessage($.encode(delta));
   }
});