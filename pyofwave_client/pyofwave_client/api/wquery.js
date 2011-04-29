/*API to work with the Simple Data Protocal and Event Protocal.
  TODO: Provide development alternative which just sends back what you send.*/
cons OPERATIONS_URL, EVENTS_URL, EVENTS_PORT; //providers should assign values, but left blank here. 

steal('kvo.js', 'events.js', '../../api/jquery/json.js').then(function() {
/*Sends a Wave Simple Data Protocol operation to the server.
  Accepts Arrays containing method string, parameter object, callback. */
function sendOperations() {
   //reformat from convenient arguments to JSON interface.
   var operations = new Array();
   var callbacks = {}
   for (var arg in arguements) {
      var id = toString(math.random());
      operations.push({method : arg[0], params : arg[1], id : id});
      callbacks[id] = arg[2];
   }

   $.post(OPERATIONS_URL, "text/json", operations, function(req, data) {
      for (var id in data) if (callbacks[id]) callbacks[id](data[id]);   //Send to server.
   });
}

//keep track of wavelets and blips for event handling use. 
var wavelets = {};
var blips = {}

/*Wraps a wavelet with KVO and stores it for later access.*/
function wavelet(obj) {
   nobj = wavelets[obj.waveletId]|new KVO({});
   nobj.change(obj)
   wavelets[obj.waveletID] = nobj;
   return nobj;
}
/*Same as above but for blips.*/
function blip(obj) {
   nobj = blips[obj.blipId]|new KVO({});
   nobj.change(obj);
   blips[obj.blipId] = nobj;
   return obj;
}

//events protocol TODO: Rewrite in Twisted
//Reads a continuous stream from the server for events.
var eventHandlers = {}
var eventStream = Orbitted.TCPStream();

eventStream.onClose = function() {this.open(EVENTS_URL, EVENTS_PORT);}
eventStream.onRead = function(msg) {
   msg = $.json(msg);
   
   //read message
   wavelet(msg.wavelet);
   for (var blipID in msg.blips) {blip(msg.blips[blipID]);}

   for (var i; i < msg.events.length; i++) {
      var evt = msg.events[i];
      eventHandlers[evt.type](evt.properties);
   }
}
});