/* Replace wquery.js with this file to unbind yourself from PyOfWave Server or any Wave Server.*/
steal('kvo.js', 'events.js').then(function() {
function sendOperations() {
  for (var arg in arguments) {
    res = operations[arg[0]](arg[1]);
    arg[2](res);
  }
}

//keep track of wavelets and blips for event handling use. 
var wavelets = new Array();
var blips = {}

/*Wraps a wavelet with KVO and stores it for later access.*/
function wavelet(obj) {
   obj = new KVO(obj);
   wavelets.push(obj);
   return obj;
}
/*Same as above but for blips.*/
function blip(obj) {
   obj = new KVO(obj);
   blips[obj.get("blipId")] = obj;
   return obj;
}

//Domains for protocol local protocol routines
var eventHandlers = {}

var operations = {
  'robot.createWavelet' : function(args) {
    
  },
  'robot.fetchFolders' : function(args) {
    
  },
  'robot.fetchWavelet' : function(args) {
    
  },
  'robot.search' : function(args) {
    
  }
}
});