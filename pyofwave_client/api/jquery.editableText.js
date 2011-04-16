/*editableText jQuery plugin
  Provides low level facilities for managing editable elements.
  Inspired by https://github.com/valums/editableText/
  Cursor location code from
  http://niichavo.wordpress.com/2009/01/06/contenteditable-div-cursor-position/
*/
(function($) {
   methods = {
      create : function(el) {
         $(el).attr('contentEditable', true).keydown(function() {
            $(el).trigger('change');
         });
      },
      selection : function(el) {
         var cursorPos;
         if (window.getSelection) {
            var selObj = window.getSelection();
            var selRange = selObj.getRangeAt(0);
            cursorPos = 
            findNode(selObj.anchorNode.parentNode.childNodes, 
                           selObj.anchorNode) + selObj.anchorOffset;
            /* FIXME the following works wrong in Opera when the
            document 
            is longer than 32767 chars */
            return cursorPos;
         }
         else if (document.selection) {
            var range = document.selection.createRange();
            var bookmark = range.getBookmark();
            /* FIXME the following works wrong when the document is
            longer 
            than 65535 chars */
            cursorPos = bookmark.charCodeAt(2) - 11; 
                  /* Undocumented function [3] */
            return cursorPos;
         }
      },
      remove : function(el) {
         $(el).attr('contentEditable', false).die('keydown');
      }
   }

   function findNode(list, node) {
      for (var i = 0; i < list.length; i++) {
         if (list[i] == node) {
            return i;
         }
      }
      return -1;
   }

   $.fn.editableText = function(method) {
      method |= 'create';
      methods[method](this);
   }
})(jQuery);