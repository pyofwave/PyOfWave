/*JavaScript for the pop out window.*/
steal('../api/waveUI.js', '../api/uri.js').then(function() {
uri = parseUri(location.hash);

//manage options
if (uri.querykey.css) steal().css(uri.querykey.css);
if (uri.querykey.alias) loginAlias(uri.querykey.alias);

if (uri.host == "__new__") {
   // Send operations to create a new wave with URI options. 
}
else {
   // Send operations to retrieve uri.host
}
});

function loginAlias(alias) {
   
}