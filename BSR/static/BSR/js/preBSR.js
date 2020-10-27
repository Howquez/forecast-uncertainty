function validation(){
	var minTemp;
	var maxTemp;
	var valid;
	var next;

	minTemp = parseInt(document.getElementById("id_minTemp").value);
	maxTemp = parseInt(document.getElementById("id_maxTemp").value);

	minField = document.getElementById("id_minTemp");
	maxField = document.getElementById("id_maxTemp");

	valid   = document.getElementById("pre_BSR_validation");
	revise  = document.getElementById("pre_BSR_revision");
	next    = document.getElementById("pre_BSR_next");

	// console.log("Min: ".concat(minTemp));
	// console.log("Max: ".concat(maxTemp));
	// console.log(window.location.href)


	if (maxTemp < minTemp) {
		lowMaxModal.style.display = "block";
		// alert("Die höchste Temperatur, die sie für möglich halten, muss höher sein, als die niedrigste Temperatur, die Sie für möglich halten.");
		return false;
	}

	if (maxTemp == NaN || minTemp == NaN) {
		alert("Bitte tragen Sie ganze Zahlenwerte ein.")
		return false;
	}

	if (minTemp <= maxTemp){
		console.log("Prüf-Button verschwindet, Next erscheint, Eingabe ist fix")
		// if (elem.value == "Eingabe prüfen") elem.value = "Weiter";
		// else elem.value = "Weiter";
		minField.setAttribute("readonly", "")
		maxField.setAttribute("readonly", "")
		valid.style = "display:none"
		revise.style = ""
		next.style  = ""
	}
}

function revision(){

	minTemp = parseInt(document.getElementById("id_minTemp").value);
	maxTemp = parseInt(document.getElementById("id_maxTemp").value);

	minField = document.getElementById("id_minTemp");
	maxField = document.getElementById("id_maxTemp");

	valid   = document.getElementById("pre_BSR_validation");
	revise  = document.getElementById("pre_BSR_revision");
	next    = document.getElementById("pre_BSR_next");

	valid.style  = ""
	revise.style = "display:none"
	next.style   = "display:none"

	minField.removeAttribute("readonly")
	maxField.removeAttribute("readonly")
}

// Modals
// Get the button that close the modal
var closeLowMax  = document.getElementById("closeLowMax");
var closeWeather = document.getElementById("closeWeather");

// When the user clicks the button, open the modal 
pre_BSR_weather.onclick = function() {
  weatherModal.style.display = "block";
}

// When the user clicks the button, close the modal 
closeLowMax.onclick = function() {
	lowMaxModal.style.display = "none";
}
closeWeather.onclick = function() {
	weatherModal.style.display = "none"
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == lowMaxModal || event.target == weatherModal) {
    lowMaxModal.style.display = "none";
    weatherModal.style.display = "none";
  }
}