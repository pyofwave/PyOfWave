/*JavaScript for the pop out window.*/
steal('../api/waveUI.js', '../api/uri.js').then(function() {
uri = parseUri(location.hash);

//manage options
if (uri.querykey.css) steal().css(uri.querykey.css);
if (uri.querykey.alias) loginAlias(uri.querykey.alias);

if (uri.host == "__new__") {
   // Send operations to create a new wave with URI options. 
   var wavelet = {} // TODO: fill out. 
   sendOperations(["robot.createWavelet", {waveletData : wavelet, message : "URL create"}, handleResponse]);
}
else {
   sendOperations(
      ["robot.fetchWavelet", {waveId : uri.host, waveletId : uri.host, message : "URL read"}, handleResponse]);
}
});

function loginAlias(alias) {
   
}

function handleResponse(data) {
   //index data
   $('#wave-root').waveletView({wavelet: wavelet});
}