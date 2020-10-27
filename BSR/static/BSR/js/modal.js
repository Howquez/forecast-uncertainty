// Get the button that opens the modal
var openInstructions = document.getElementById("openInstructions");

// Get the button that closes the modal
var closeInstructions = document.getElementById("closeInstructions");
var closeWarning = document.getElementById("closeWarning");
var closeError = document.getElementById("closeError");
var closeWeather = document.getElementById("closeWeather");


// When the user clicks the button, open the modal 
openInstructions.onclick = function() {
  instructionsModal.style.display = "block";
}
pre_BSR_weather.onclick = function() {
  weatherModal.style.display = "block";
}

// When the user clicks the button, close the modal 
closeInstructions.onclick = function() {
  instructionsModal.style.display = "none";
}
closeWarning.onclick = function() {
  warningModal.style.display = "none";
}
closeError.onclick = function() {
  errorModal.style.display = "none";
}
closeWeather.onclick = function() {
	weatherModal.style.display = "none"
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == errorModal || event.target == warningModal || event.target == instructionsModal || event.target == weatherModal) {
    errorModal.style.display = "none";
    warningModal.style.display = "none";
    instructionsModal.style.display = "none";
    weatherModal.style.display = "none";

  }
}