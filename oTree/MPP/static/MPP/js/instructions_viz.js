// read data


var observed = [
        [1601992800000, null], //20201006
        [1602079200000, 48.3], //20201007 to be displayed
        [1602165600000, 46.9], //20201008 to be displayed
        [1602252000000, 46.1], //20201009 to be displayed
        [1602338400000, 45.2], //20201010
        [1602424800000, 46.0], //20201011
        [1602511200000, 46.2], //20201012
        [1602597600000, 46.5], //20201013
        [1602684000000, 45.9], //20201014
        [1602770400000, 44.8], //20201015
        [1602856800000, 44.2], //20201016
        [1602943200000, 44.6], //20201017
        [1603029600000, 45.0], //20201018 to be revealed // 45.0
        [1603116000000, null], //20201019
    ];

var revelation = [
        [1601992800000, null], //20201006
        [1602079200000, null], //20201007 to be displayed
        [1602165600000, null], //20201008 to be displayed
        [1602252000000, 46.1], //20201009 to be displayed
        [1602338400000, 45.2], //20201010
        [1602424800000, 46.0], //20201011
        [1602511200000, 46.2], //20201012
        [1602597600000, 46.5], //20201013
        [1602684000000, 45.9], //20201014
        [1602770400000, 44.8], //20201015
        [1602856800000, 44.2], //20201016
        [1602943200000, 44.6], //20201017
        [1603029600000, 45.0], //20201018 to be revealed // 45.0
        [1603116000000, null], //20201019
    ];


// display only the first few data points
for (var i = 0; i < observed.length; ++i){
    if (i > 3){
        observed[i][1] = null;
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
var chart = Highcharts.chart("weather_viz", {
    exporting: {
        enabled: false
    },

    chart: {
        height: (6 / 16 * 100) + '%', // 16:6 ratio
        backgroundColor: 'transparent'
    },

    title: {
        text: " " //`Treatment: "${treatment}" in ${village}`
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
            text: "Temperatur in °C"
        },
        min: 0,
    },

    tooltip: {
        crosshairs: true,
        shared: true,
        valueSuffix: "°C",
        xDateFormat: "%A"
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
        showInLegend: false,
    }]
});

// plot options
var revelation = Highcharts.chart("revelation_viz", {
    exporting: {
        enabled: false
    },

    chart: {
        height: (9 / 16 * 100) + '%', // 16:9 ratio
        backgroundColor: 'transparent'
    },

    title: {
        text: "Sahara" //`Treatment: "${treatment}" in ${village}`
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
            text: "Temperatur in °C"
        },
        min: 0,
    },

    tooltip: {
        crosshairs: true,
        shared: true,
        valueSuffix: "°C",
        xDateFormat: "%A"
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
        showInLegend: true,
    }, {
        name: "Auflösung",
        data: revelation,
        zIndex: 1,
        color: forecastColor,//Highcharts.getOptions().colors[0]
        marker: {
            fillColor: "white",
            lineWidth: 2,
            lineColor: forecastColor//Highcharts.getOptions().colors[0]
        },
        showInLegend: true,
    }]
});