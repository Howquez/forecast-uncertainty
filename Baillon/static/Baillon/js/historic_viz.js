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
        [1603029600000, 7.6, 13.8],
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
        [1603029600000, 12.3],
        [1603116000000, null],
    ];

var weiskirchenObserved = [
        [1601992800000, null],
        [1602079200000, 11.8],
        [1602165600000, 12.3],
        [1602252000000, 12.2],
        [1602338400000, null],
        [1602424800000, null],
        [1602511200000, null],
        [1602597600000, null],
        [1602684000000, null],
        [1602770400000, null],
        [1602856800000, null],
        [1602943200000, null],
        [1603029600000, null],
        [1603116000000, null],
    ];

// color definitions
var opacity = 0.1
var observedColor = "#5DE58E";
var observedRGBA  = `rgba(93, 229, 142, ${opacity})` 
var forecastColor = "#FF5B66";
var forecastRGBA  = `rgba(255, 91, 102, ${opacity})`

// language options
Highcharts.setOptions({
    lang: {
        weekdays: ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'],
        shortWeekdays: ['So.', 'Mo.', 'Di.', 'Mi.', 'Do.', 'Fr.', 'Sa.']
    },
});



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
        valueSuffix: "°C"
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
        showInLegend: true,
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
        showInLegend: true,
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


// var chart = Highcharts.chart('container', {
// 	exporting: {
// 		enabled: false
// 	},
//     chart: {
//         type: 'line'
//     },
//     title: {
//         text: 'Monthly Average Temperature'
//     },
//     subtitle: {
//         text: 'Quelle: Kachelmannwetter.com' // https://kachelmannwetter.com/de/vorhersage/2812071-weiskirchen/ensemble/euro
//     },
//     xAxis: {
//         categories: ['Mo.', 'Di.', 'Mi.', 'Do.', 'Fr.', 'Sa.', 'So.', 
//         'Mo.', 'Di.']
//     },
//     yAxis: {
//         title: {
//             text: 'Temperatur in °C'
//         },
//         min: 0,
//     },
//     plotOptions: {
//         line: {
//             dataLabels: {
//                 enabled: true
//             },
//             enableMouseTracking: false
//         }
//     },
//     series: [{
//         name: "Weiskirchen (DE)",
//         data: [12.0, 12.0, 12.0],
//         visible: true,
//         showInLegend: true
//     }, {
//         name: "Full Weiskirchen (DE)",
//         data: [12.0, 12.0, 12.0, 12.5, 12.4, 13.5, 11.2, 10.5, 9.0],
//         visible: true,
//         showInLegend: true
//     }, {
//         name: "Ilomantsi (FI)",
//         data: [12.0, 12.0, 12.0, null, null, null, null, null, 9.0],
//         visible: true,
//         showInLegend: true
//     }, {
//         name: "Full Ilomantsi (FI)",
//         data: [12.0, 12.0, 12.0, 11.5, 10.9, 8.2, 6.0, 4.6, 3.0],
//         visible: true,
//         showInLegend: true
//     }]
// });