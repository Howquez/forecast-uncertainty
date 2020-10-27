// read data
var weiskirchenRange = [
        [1601992800000, null, null],
        [1602079200000, null, null],
        [1602165600000, null, null],
        [1602252000000, null, null],
        [1602338400000, null, null],
        [1602424800000, null, null],
        [1602511200000, null, null],
        [1602597600000, null, null],
        [1602684000000, null, null],
        [1602770400000, null, null],
        [1602856800000, null, null],
        [1602943200000, null, null],
        [1603029600000, 7.6, 13.8], //20201018 to be displayed
        [1603116000000, null, null],
    ];

var ilomantsiRange = [
        [1601992800000, null, null],
        [1602079200000, null, null],
        [1602165600000, null, null],
        [1602252000000, null, null],
        [1602338400000, null, null],
        [1602424800000, null, null],
        [1602511200000, null, null],
        [1602597600000, null, null],
        [1602684000000, null, null],
        [1602770400000, null, null],
        [1602856800000, null, null],
        [1602943200000, null, null],
        [1603029600000, 2.0, 8.0], //20201018 to be displayed
        [1603116000000, null, null],
    ];

var weiskirchenBestGuess = [
        [1601992800000, null],
        [1602079200000, null],
        [1602165600000, null],
        [1602252000000, null],
        [1602338400000, null],
        [1602424800000, null],
        [1602511200000, null],
        [1602597600000, null],
        [1602684000000, null],
        [1602770400000, null],
        [1602856800000, null],
        [1602943200000, null],
        [1603029600000, 12.3], //20201018 to be displayed
        [1603116000000, null],
    ];

var ilomantsiBestGuess = [
        [1601992800000, null],
        [1602079200000, null],
        [1602165600000, null],
        [1602252000000, null],
        [1602338400000, null],
        [1602424800000, null],
        [1602511200000, null],
        [1602597600000, null],
        [1602684000000, null],
        [1602770400000, null],
        [1602856800000, null],
        [1602943200000, null],
        [1603029600000, 4.2], //20201018 to be displayed
        [1603116000000, null],
    ];

// https://kachelmannwetter.com/de/messwerte/63-e-491-n/temperatur/20201009-1100z.html#obs-detail-J728-72h
// https://kachelmannwetter.com/de/messwerte/63-e-491-n/temperatur/20201019-1100z.html#obs-detail-J728-72h
var weiskirchenObserved = [
        [1601992800000, null], //20201006
        [1602079200000, 11.8], //20201007 to be displayed
        [1602165600000, 12.3], //20201008 to be displayed
        [1602252000000, 12.2], //20201009 to be displayed
        [1602338400000, 10.6], //20201010
        [1602424800000, 11.8], //20201011
        [1602511200000, 9.4],  //20201012
        [1602597600000, 9.4],  //20201013
        [1602684000000, 11.0], //20201014
        [1602770400000, 8.8],  //20201015
        [1602856800000, 9.1],  //20201016
        [1602943200000, 8.7],  //20201017
        [1603029600000, 8.5],  //20201018 to be revealed
        [1603116000000, null], //20201019
    ];

// https://kachelmannwetter.com/de/messwerte/ostfinnland/temperatur/20201019-1100z.html#obs-detail-029390-72h
// https://kachelmannwetter.com/de/messwerte/ostfinnland/temperatur/20201009-1100z.html#obs-detail-029390-72h
var ilomantsiObserved = [
        [1601992800000, null], //20201006
        [1602079200000, 12.0], //20201007 to be displayed
        [1602165600000, 11.9], //20201008 to be displayed
        [1602252000000, 12.1], //20201009 to be displayed
        [1602338400000, 10.1], //20201010
        [1602424800000, 9.1],  //20201011
        [1602511200000, 8.9],  //20201012
        [1602597600000, 8.0],  //20201013
        [1602684000000, 5.9], //20201014
        [1602770400000, 3.4],  //20201015
        [1602856800000, 1.0],  //20201016
        [1602943200000, 4.1],  //20201017
        [1603029600000, 3.2],  //20201018 to be revealed
        [1603116000000, null], //20201019
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

    document.getElementById("revelation").innerHTML = observed[12][1];
    document.getElementById("village").innerHTML = village;

    }

// color definitions
var opacity = 0.1;
var observedColor = "#5DE58E";
var observedRGBA  = `rgba(93, 229, 142, ${opacity})`;
var forecastColor = "#C582FF";
var forecastRGBA  = `rgba(197, 130, 255, ${opacity*1.5})`;


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
var chart = Highcharts.chart('container', {
    exporting: {
        enabled: false
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
        from: 1602079200000 - 43200000,
        to: 1602252000000 + 43200000,
        color: observedRGBA,
        label: {
            text: "", // Content of the label. 
            verticalAlign: "middle",
        }
      }, {
        from: 1603029600000 - 43200000,
        to: 1603029600000 + 43200000,
        color: forecastRGBA,
        label: {
            text: "", // Content of the label. 
            verticalAlign: "middle",
        }
      }]
    },
    yAxis: {
        title: {
            text: "Temperatur in °C"
        },
        min: 0,
        max: 25,
    },

    tooltip: {
        crosshairs: true,
        shared: true,
        valueSuffix: "°C"
    },

    series: [{
        name: "Beobachtete Temperatur in °C",
        data: observed,
        zIndex: 1,
        color: observedColor,//Highcharts.getOptions().colors[0]
        marker: {
            fillColor: "white",
            lineWidth: 2,
            lineColor: observedColor//Highcharts.getOptions().colors[0]
        },
        showInLegend: displayForecast,
    }, {
        name: "Wettervorhersage",
        data: bestGuess,
        zIndex: 1,
        color: forecastColor,
        marker: {
            fillColor: 'white',
            lineWidth: 2,
            lineColor: forecastColor
        },
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
        marker: {
            enabled: true
        }
    }]
});