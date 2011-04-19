/*Connects the SDK to input and output*/
cons trustedSource; //To be provided by provider as their domain.

//data
/*Recieves messages from the gadget view.
function displayMessage(message, source) {
   if (source != trustedSource) {
      alert("A external site (?) has attempted to update this gadget's data. The data has not changed.".replace("?", source));
      return;
   }
   message = eval(message);

   for (var key in source.public) publicState[key] = message.public[key];
   for (key in source.private) privateState[key] = message.private[key];
}
/*Send changes to the gadgetView as a comma seperated data of public,key,value*/
publicState.observe(function(obj, key, val) {
   parent.postMessage("public,"+key+","+val, trustedSource);
});
/*Send changes to the gadgetView as a comma seperated data of private,key,value*/
private.observe(function(obj, key, val) {
   parent.postMessage("public,"+key+","+val, trustedSource);
});

//TODO: Tie the view to the display.