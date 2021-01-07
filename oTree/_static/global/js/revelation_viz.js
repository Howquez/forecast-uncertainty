
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

// get vars from python
let village = js_vars.location;   // equals "Weiskirchen" or "Ilomantsi"
let treatment = js_vars.treatment; // equals "best_guess" or "interval"

// page and treatment specific operations
var displayForecast = false;
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
function fillText() {

    document.getElementById("revelation").innerHTML = observed[11][1];
    }

// color definitions
var opacity = 0.1;
var observedColor = "#FFCC00"; // "#5DE58E";
var forecastColor = "#A6219D"; //"#7B6FA6";


// language plot options
Highcharts.setOptions({
    lang: {
        months:        ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
        shortMonths:   ["Jan.", "Feb.", "März", "Apr.", "Mai", "Jun.", "Jul.", "Aug.", "Sept.", "Okt.", "Nov.", "Dez."],
        weekdays:      ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'],
        shortWeekdays: ['So.', 'Mo.', 'Di.', 'Mi.', 'Do.', 'Fr.', 'Sa.']
    },
});

// plot options
var chart = Highcharts.chart("weather_viz", {
    exporting: {
        enabled: false
    },

    chart: {
        height: (4 / 16 * 100) + '%', // 16:9 ratio
        backgroundColor: 'transparent'
    },

    plotOptions: {
        series: {
            animation:{
                duration: 2000
            }
        }
    },

    title: {
        text: ""
    },

    xAxis: {
        type: "datetime",
        accessibility: {
            rangeDescription: ""
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
                    opacity: 0.25
                }
            },
        }]
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
        valueSuffix: "°C"
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
        name: "Gemessene Temperatur in °C",
        data: observed,
        type: "area",
        color: observedColor,
        fillOpacity: 0.1,
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
        zIndex: 1,
        color: observedColor,//Highcharts.getOptions().colors[0]
        showInLegend: displayForecast,
    }, {
        name: "Wettervorhersage",
        data: bestGuess,
        zIndex: 1,
        color: forecastColor,
        showInLegend: displayForecast,
        visible: displayForecast
    }, {
        name: "Wahrscheinlichster Bereich",
        data: range,
        type: "arearange",
        lineWidth: 0,
        linkedTo: ":previous",
        color: forecastColor, 
        fillOpacity: 0.3,
        zIndex: 0,
    }]
});

chart.tooltip.refresh([chart.series[0].points[11]]);
