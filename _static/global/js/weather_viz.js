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

// https://kachelmannwetter.com/de/messwerte/63-e-491-n/temperatur/20201009-1100z.html#obs-detail-J728-72h
// https://kachelmannwetter.com/de/messwerte/63-e-491-n/temperatur/20201019-1100z.html#obs-detail-J728-72h
var weiskirchenObserved = [
        [1602028800000, 12], 
        [1602115200000, 12], 
        [1602201600000, 12], 
        [1602288000000, 11], 
        [1602374400000, 12], 
        [1602460800000, 9], 
        [1602547200000, 9], 
        [1602633600000, 11], 
        [1602720000000, 9], 
        [1602806400000, 9], 
        [1602892800000, 9], 
        [1602979200000, 9],  
        [1602979200000 + 14400000, null],  
    ];

// https://kachelmannwetter.com/de/messwerte/ostfinnland/temperatur/20201019-1100z.html#obs-detail-029390-72h
// https://kachelmannwetter.com/de/messwerte/ostfinnland/temperatur/20201009-1100z.html#obs-detail-029390-72h
var ilomantsiObserved = [
        [1602028800000, 12],
        [1602115200000, 12],
        [1602201600000, 12],
        [1602288000000, 10],
        [1602374400000, 9],
        [1602460800000, 9],
        [1602547200000, 8],
        [1602633600000, 6],
        [1602720000000, 3],
        [1602806400000, 1],
        [1602892800000, 4],
        [1602979200000, 3],
    ];


var instructionsObserved = [
        [1602115200000, 48], //20201007 to be displayed
        [1602201600000, 46], //20201008 to be displayed
        [1602288000000, 46.1], //20201009 to be displayed
        [1602374400000, 46.1], //20201010
        [1602460800000, 46.1],  //20201011
        [1602547200000, 46.1],  //20201012
        [1602633600000, 46.1],  //20201013
        [1602720000000, 46.1], //20201014
        [1602806400000, 46.1],  //20201015
        [1602892800000, 46.1],  //20201016
        [1602979200000, 46.1],  //20201017
        [1603065600000, 46.1],  //20201018 to be revealed
    ];

// get vars from python
let village = js_vars.location;   // equals "Weiskirchen" or "Ilomantsi"
let treatment = js_vars.treatment; // equals "best_guess" or "interval" or "both"
let page = js_vars.page; // equals "historic" or "forecast" or "decision" or "revelation" or "instructions"
let iteration  = js_vars.treatment_displayed;
let small = js_vars.small || false; // determines size of visualization


// page and treatment specific operations
var displayForecast = false;
var displayBestGuess = false;
var displayInterval = false;
var opacity = 0.66;
var observed;
var bestGuess;
var Range;

if (village == "Ilomantsi"){
    observed = ilomantsiObserved;
    bestGuess = ilomantsiBestGuess;
    range = ilomantsiRange;
} else if (village == "Weiskirchen"){
    observed = weiskirchenObserved;
    bestGuess = weiskirchenBestGuess;
    range = weiskirchenRange;
} 


// text operations
var rangeText = `Sie halten es für sehr wahrscheinlich, dass die Temperatur um 14:00 Uhr zwischen ${range[1][1]}°C und ${range[1][2]}°C betragen wird. `
var bestguessText = `Eine Temperatur von ${bestGuess[1][1]}°C halten Sie dabei für am wahrscheinlichsten. `; 
var forecastText = "&nbsp;";


// display forecast after the first round, i.e. in postBaillon App
if (page == "forecast"){
    displayForecast = true;
}

// display forecast during second decision round
if (iteration == "True"){ //marks the second iteration of an App
    displayForecast = true;
    opacity = 0;

}


// display only the first few data points
for (var i = 0; i < observed.length; ++i){
    if (page != "revelation"){
        if (i > 2){
            observed[i][1] = null;
        }
    }
}

// treatment definitions
if (treatment == "best_guess" && displayForecast){
    displayBestGuess = true;
    forecastText = bestguessText; 
} else if (treatment == "interval" && displayForecast){
    displayInterval = true;
    forecastText = rangeText 
} else if (treatment == "both" && displayForecast){
    displayBestGuess = true;
    displayInterval = true;
    forecastText = rangeText + bestguessText; 
}

 // text operations 2
function fillText() {
    var reportArray = [observed[1][1],
    observed[2][1],
    observed[3][1]];
    if (displayForecast){
        document.getElementById("forecastText").innerHTML = forecastText;
    }
    
    // document.getElementById("report0").innerHTML = reportArray[0];
    // document.getElementById("report1").innerHTML = reportArray[1];
    // document.getElementById("report2").innerHTML = reportArray[2];
    }

// color definitions
var observedColor = "#FFCC00"; // "#5DE58E";
var forecastColor = "#A6219D"; //"#7B6FA6";

// height of chart
var height = 9;
if (small){
    height = 9;
}


// language plot options
Highcharts.setOptions({
    lang: {
        weekdays: ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'],
        shortWeekdays: ['So.', 'Mo.', 'Di.', 'Mi.', 'Do.', 'Fr.', 'Sa.']
    },
});

// plot options
var chart = Highcharts.chart("weather_viz", {
    exporting: {
        enabled: false
    },

    chart: {
        height: (height / 16 * 100) + '%', // 16:9 ratio
        backgroundColor: 'transparent'
    },

    title: {
        text: `Treatment: "${treatment}" in ${village}`
    },

    xAxis: {
        breaks: [{
                from: 1602288000000,
                to: 1602979200000 - 14400000,
            }],
        tickInterval: 24 * 3600 * 1000,
        type: "datetime",
        labels: {
            formatter: function() {
            var dayStr = Highcharts.dateFormat('%a', this.value);
            if (dayStr == "Sa."){
                return ""
            } else if(dayStr == "So."){
                return "<b>So.</b>"
            } else {
                return dayStr
            };
            }
        },
        plotBands: [{
            from: 1602201600000,
            to: 1602979200000 - 14400000,
            color: {
                pattern: {
                    path: "M 0 0 L 5 10 L 10 0",
                    color: "#e8e8e8", //"#FF5B66";,
                    width: 10,
                    height: 10,
                    opacity: 0.5
                }
            },
            label: {
                useHTML: true,
                text: "+ eine Woche", //'<svg width="2em" height="2em" style="color:#555555" viewBox="0 0 16 16" class="bi bi-calendar-range-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4 .5a.5.5 0 0 0-1 0V1H2a2 2 0 0 0-2 2v1h16V3a2 2 0 0 0-2-2h-1V.5a.5.5 0 0 0-1 0V1H4V.5zM16 7V5H0v5h5a1 1 0 1 1 0 2H0v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9h-6a1 1 0 1 1 0-2h6z"/> /svg>',
                verticalAlign: "middle",
                align: "center",
                style: {
                    fontWeight: "bold"
                }
            }
        }, {
            from: 1602979200000 - 14400000,
            to: 1602979200000 + 14400000,
            color: {
                pattern: {
                    path: "M 0 10 L 10 0 M -1 1 L 1 -1 M 9 11 L 11 9",
                    color: forecastColor,
                    width: 10,
                    height: 10,
                    opacity: opacity
                }
            },
            label: {
                text: "", // Content of the label. 
                verticalAlign: "middle",
            }
        }],
    },

    yAxis: {
        title: {
            text: "Temperatur in °C"
        },
        min: 0,
        max: 20,
    },

    tooltip: {
        crosshairs: true,
        shared: true,
        valueSuffix: "°C",
        xDateFormat: "%A"
    },

    plotOptions: {
        series: {
            marker: {
                enabled: false
            }
        },
        line: {
            dataLabels: {
                enabled: true,
                borderWidth: 0,
                    style: {
                        fontWeight: "bold",
                        textOutline: 0,
                    },
                color: "#8E8E8E",
            },
        }
    },

    series: [{
        name: "Gemessene Temperatur",
        type: "area",
        fillOpacity: 0.1,
        data: observed,
        zIndex: 1,
        color: observedColor,
        lineWidth: 2.5,
        dataLabels: {
                enabled: true,
                borderWidth: 0,
                    style: {
                        fontWeight: "bold",
                        textOutline: 0,
                    },
                color: "#8E8E8E",
            },
        // marker: {
        //     fillColor: "white",
        //     lineWidth: 2,
        //     lineColor: observedColor//Highcharts.getOptions().colors[0]
        // },
        showInLegend: displayForecast,
    }, {
        name: "Wettervorhersage",
        data: bestGuess,
        zIndex: 1,
        color: forecastColor,
        dataLabels: {
            formatter: function() {
                if(this.x == 1602979200000 + 14400000){
                    return this.y
                }
            },
            color: "#000000"
        },
        // marker: {
        //     fillColor: 'white',
        //     lineWidth: 2,
        //     lineColor: forecastColor
        // },
        showInLegend: displayForecast && displayBestGuess,
        visible: displayForecast && displayBestGuess
    }, {
        name: "Wahrscheinlichster Bereich",
        data: range,
        type: "arearange",
        lineWidth: 0,
        linkedTo: ":previous",
        color: forecastColor, 
        fillOpacity: 0.33,
        zIndex: 0,
        dataLabels: {
            enabled: true,
            formatter: function() {
                if(this.x == 1602979200000 + 14400000){
                    return this.y
                }
            }
        },
        // marker: {
        //     enabled: true
        // },
        showInLegend: displayForecast && displayInterval && treatment !== "both",
        visible: displayForecast && displayInterval,

    }]
});

if(displayForecast){
    chart.tooltip.refresh([chart.series[1].points[1]]);
}
