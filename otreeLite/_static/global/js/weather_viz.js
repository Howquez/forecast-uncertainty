console.log("weather ready!")


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
var range;

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
var rangeText = `They think it is very likely that the temperature at 14:00 will be between ${range[1][1]}°C and ${range[1][2]}°C. `
var bestguessText = `They consider a temperature of ${bestGuess[1][1]}°C most likely. `;
var forecastText = "&nbsp;";


// display forecast after the first round, i.e. in postBaillon App
if (page == "forecast"){
    displayForecast = true;
}

// display forecast during second decision round
if (iteration){ //marks the second iteration of an App
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
    }

// color definitions
var observedColor = "#FFCC00";
var forecastColor = "#A6219D";

// height of chart
var height = 9;
// if (small){
//     height = 9;
// }
// if (page == "decision"){
//     height = 16;
// }


// language plot options
Highcharts.setOptions({
    lang: {
        weekdays: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        shortWeekdays: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    },
});

// plot options
var chart = Highcharts.chart("weather_viz", {
    exporting: {
        enabled: false
    },

    chart: {
        height: (height / 16 * 100) + '%',
        backgroundColor: 'transparent'
    },

    title: {
        text: ""
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
                    color: "#e8e8e8",
                    width: 10,
                    height: 10,
                    opacity: 0.5
                }
            },
            label: {
                useHTML: true,
                text: "+ one week",
                verticalAlign: "middle",
                align: "center",
                style: {
                    fontWeight: "bold",
                    zIndex: -1
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
            text: "Temperature in °C"
        },
        min: 0,
        max: 35,
    },

    tooltip: {
        backgroundColor: "rgba(255,255,255, 1)",
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
        name: "Observed Temperature",
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
        showInLegend: displayForecast,
    }, {
        name: "Weather Forecast",
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
        showInLegend: displayForecast && displayBestGuess,
        visible: displayForecast && displayBestGuess
    }, {
        name: "Most Probable Range",
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
        showInLegend: displayForecast && displayInterval && treatment !== "both",
        visible: displayForecast && displayInterval,

    }]
});

if(displayForecast){
    if(displayBestGuess){
        chart.tooltip.refresh([chart.series[1].points[1]]);
    }
    if(displayInterval){
        chart.tooltip.refresh([chart.series[2].points[1]]);
    }
    
}
