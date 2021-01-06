// read data
var weiskirchenRange = [
        [1602979200000 - 14400000, 8, 14],
        [1602979200000 + 14400000, 8, 14],
    ];

var ilomantsiRange = [
        [1602979200000 - 14400000, 2, 8],
        [1602979200000 + 14400000, 2, 8],
    ];

var weiskirchenBestGuess = [
        [1602979200000 - 14400000, 12],
        [1602979200000 + 14400000, 12],
    ];

var ilomantsiBestGuess = [
        [1602979200000 - 14400000, 4],
        [1602979200000 + 14400000, 4],
    ];


// get vars from python
let treatment = js_vars.treatment; // equals "best_guess" or "interval" or "both"
let village = js_vars.location;

// declare variables
var displayForecast = true // only if this script is loaded on pages where the forecast was displayed indeed
var bestGuess;
var range;

if (village == "Ilomantsi"){
    bestGuess = ilomantsiBestGuess;
    range = ilomantsiRange;
} else if (village == "Weiskirchen"){
    bestGuess = weiskirchenBestGuess;
    range = weiskirchenRange;
} 


// text operations
var rangeText = `Experten halten es für sehr wahrscheinlich, dass die Temperatur um 14:00 Uhr zwischen ${range[1][1]}°C und ${range[1][2]}°C betragen wird.`
var bestguessText = `Eine Temperatur von ${bestGuess[1][1]}°C halten Sie für am wahrscheinlichsten.`; 
var forecastText = "&nbsp;";

// treatment definitions
if (treatment == "best_guess" && displayForecast){
    forecastText = bestguessText; 
} else if (treatment == "interval" && displayForecast){
    forecastText = rangeText 
} else if (treatment == "both"  && displayForecast){
    forecastText = rangeText + "&nbsp;" + bestguessText; 
}

 // text operations 2
function fillText() {
    if (displayForecast){
        document.getElementById("forecastText").innerHTML = '<em>"' + forecastText + '"<em>';
    }
}