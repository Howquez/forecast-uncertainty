console.log("trigger")

var offcanvasWeather = document.getElementById("offcanvasWeather")

// document.addEventListener('DOMContentLoaded', function() {
//    $(weatherModal).modal('show')
// }, false);

// window.onload = function trigger(){
// 	$(weatherModal).modal('show')
// }

$(document).ready(function(){
	$(offcanvasWeather).offcanvas('show')
});