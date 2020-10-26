// read data
// https://kachelmannwetter.com/de/messwerte/63-e-491-n/temperatur/20201009-1200z.html#obs-detail-J728-72h
var weiskirchenRanges = [
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

// get vars from python
// let location = js_vars.location;   // equals "Weiskirchen" or "Ilomantsi"
let treatment = js_vars.treatment; // equals "best_guess" or "interval"
let page = js_vars.page; // equals "historic" or "forecast" or "revelation"


// page and treatment specific operations
var displayForecast = false;


// display forecast after the first round, i.e. in postBaillon App
if (page == "forecast"){
    displayForecast = true;
}

for (var i = 0; i < weiskirchenObserved.length; ++i){
    if (page != "revelation"){
        if (i > 3){
            weiskirchenObserved[i][1] = null;
        }
    }
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
        weekdays: ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'],
        shortWeekdays: ['So.', 'Mo.', 'Di.', 'Mi.', 'Do.', 'Fr.', 'Sa.']
    },
});

// plot options
var chart = Highcharts.chart('container', {
    exporting: {
        enabled: false
    },

    title: {
        text: ""
    },

    xAxis: {
        type: "datetime",
        accessibility: {
            rangeDescription: ""
        },
        labels: {
            formatter: function() {
            var dayStr = Highcharts.dateFormat('%a', this.value);
            return dayStr;
            }
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
            text: null
        },
        min: 0,
        max: 25,
    },

    tooltip: {
        crosshairs: true,
        shared: true,
        valueSuffix: "°C",
        xDateFormat: "%A"
    },

    series: [{
        name: "Beobachtete Temperatur in °C",
        data: weiskirchenObserved,
        zIndex: 1,
        color: observedColor,//Highcharts.getOptions().colors[0]
        marker: {
            fillColor: "white",
            lineWidth: 2,
            lineColor: observedColor//Highcharts.getOptions().colors[0]
        },
        showInLegend: displayForecast,
    }, {
        name: "Best Guess",
        data: weiskirchenBestGuess,
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
        data: weiskirchenRanges,
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