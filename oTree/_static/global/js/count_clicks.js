console.log("engines running: clicktracking");

function countClicks(button){
	var element = "id_review_" + button
	var oldValue = parseInt(document.getElementById(element).value);
	var newValue = oldValue+1;
	document.getElementById(element).value = newValue;
}

// document.getElementById("weather_icon").addEventListener("click", function() {
//     var element = "id_review_weather";
//     console.log(element);
// 	var oldValue = parseInt(document.getElementById(element).value);
// 	var newValue = oldValue+1;
// 	console.log(newValue);
// 	document.getElementById(element).value = newValue;
// } false);

document.getElementById("contact_icon").addEventListener("click", function() {
    countClicks("contact");
}, false);

document.getElementById("weather_icon").addEventListener("click", function() {
    countClicks("weather");
}, false);

document.getElementById("weather_text").addEventListener("click", function() {
    countClicks("weather");
}, false);

document.getElementById("instructions_icon").addEventListener("click", function() {
    countClicks("instructions");
}, false);

if(document.getElementById("instructions_text")){
	document.getElementById("instructions_text").addEventListener("click", function() {
	    countClicks("instructions");
	}, false);
};
