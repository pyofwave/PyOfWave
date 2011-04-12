/*Sets up SDK for the gadget. Some browser API may also be used by gadgets, 
but it is reccommended they stick to the standard SDK outlined by 
docs/protocol/gadget API (which includes some browser API).*/

sharedMethods.getValues = function() {
   var values = new Array();
   for (var key in this) if (key.substr(0,2) != "__") values.push(this[key]);
   return values;
}
sharedMethods.getLength = function() {
   var length = 0;
   for (var key in this) if (key.substr(0,2) != "__") length++;
   return length;
}

sharedMethods.set = function(val) {
   this.__observers |= new Array();
   for (var key in this) this[key] = undefined;
   for (key in val) {
      this[key] = val[key];
      this.__binds.push(this[key].observe(this.__notify));
   }
   
   for (var o in this.__observers) observer(this);
   return this;
}
sharedMethods.observe = function(o) {
   return this.__observers.push(o);
}
sharedMethods.unobserve = function(id) {
   this.__observers.splice(id, 1);
   return this;
}

//display
function Node(style, aria, content) {
    this.style = new NodeStyle(style);
    this.aria = new ARIA(aria);
    this.content = content||new Array();
    this.events = NodeEvents();
}
function NodeStyle(obj) {
    obj |= {}
    for (var key in obj.keys()) this[key] = obj[key];
}
NodeStyle.prototype = {
    background : ,
    border : ,
    outline : ,
    size : ,
    padding : ,
    margin : ,
    font : ,
    position : ,
    zIndex : ,
}
function NodeEvents(obj) {
    obj |= {}
    for (var key in obj.keys()) this[key] = obj[key];
}
function voidf() {}
NodeEvents.prototype = {
    blur : voidf,
    change : voidf,
    dblclick : voidf,
    focus : voidf,
    keydown : voidf,
    keypress : voidf,
    keyup : voidf,
    mousedown : voidf,
    mousemove : voidf,
    mouseout : voidf,
    mouseover : voidf,
    mouseup : voidf,
    gesturestart : voidf,
    gesturemoved : voidf,
    gestureended : voidf,
    gesturecanceled : voidf
}
function ARIA(obj) {
    obj |= {}
    for (var key in obj.keys()) this[key] = obj[key];
}
function Control(type, name, value) {
    this.type = type;
    this.name = name;
    this.value = value;
    Node();
}
function Border() {
    this.thickness = 1;
    this.color = "000000";
    this.style = "solid";
}

//positioning
function Inline() {}
function Text() {}
Text.direction = "l";
Text.letterSpacing = 5;
Text.lineHeight = 10;
Text.textAlign = "l";
Text.textIndent = 10;
Text.verticalAlign = "t";
Text.whitespace = "wrap";
Text.wordSpacing = Text.letterspacing * 2;
function Block() {}
function BlockContainer() {}
function HorizontalContainer() {}
function Float() {}
Float.side = "l";
function Position() {}
Position.pos = [0,0];
function Relative() {}
Relative.delta = [0,0];
function TableCell() {}
TableCell.verticalMatch = null;
TableCell.horizontalMatch = null;
function ClipOverflow() {}
function Scroll() {}
function AddScroll() {}

//state
var publicState;
var privateState;
var participants = {participants : new Array(),
                    viewer : new User(),
                    host : new User()}
function User() {
    this.address = "";
    this.thumbnail = null;
    this.avatar = null;
    this.note = "";
}

//utils
function bind(obj1, obj2) {
   var bindObj1, bindObj2, observeObj1, observeObj2;
   function observeObj1(val) {
      obj1.unobserve(bindObj1);
      obj2 = val; //works due to preprocessor
      bindObj1 = obj1.observe(observeObj1);
   }
   function observeObj2(val) {
      obj2.unobserve(bindObj2);
      obj1 = val;
      bindObj2 = obj2.observe(observeObj2);
   }
   
   bindObj1 = obj1.observe(observeObj1);
   bindObj2 = obj2.observe(observeObj2);
}
function Canvas2D() {
   var el = document.createElement('canvas');
   var canvas = document.getContext('2d');
   canvas.el = el;
   return canvas;
}
function Canvas3D() {
   //will be implemented when needed.
}
function Render(canvas) {
   return canvas.el;
}