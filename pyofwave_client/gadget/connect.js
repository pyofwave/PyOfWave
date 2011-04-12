/*Connects the SDK to input and output*/
cons trustedSource; //To be provided by provider as their domain.

//data
function displayMessage(message, source) {
   if (source != trustedSource) {
      alert("A external site (?) has attempted to update this gadget's data. The data has not changed.".replace("?", source));
      return;
   }
   source = eval(source);

   for (var key in source.public) publicState[key] = source.public[key];
   for (key in source.private) privateState[key] = source.private[key];
}
publicState.observe(function(obj, key, val) {
   parent.postMessage("public,"+key+","+val, trustedSource);
});
private.observe(function(obj, key, val) {
   parent.postMessage("public,"+key+","+val, trustedSource);
});