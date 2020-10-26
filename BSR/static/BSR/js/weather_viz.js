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
        [1603029600000, 12.3],
        [1603116000000, null],
    ];

var observedColor = "#5DE58E";
var forecastColor = "#FF5B66";


var chart = Highcharts.chart("container", {
    exporting: {
        enabled: false
    },

    title: {
        text: ""
    },

    xAxis: {
        type: "datetime",
        accessibility: {
            rangeDescription: 'Range: Jul 1st 2009 to Jul 31st 2009.'
        }
    },

    yAxis: {
        title: {
            text: null
        },
        min: 0,
    },

    tooltip: {
        crosshairs: true,
        shared: true,
        valueSuffix: "°C"
    },

    series: [{
        name: "Observed Data",
        data: weiskirchenObserved,
        zIndex: 1,
        color: observedColor,
        marker: {
            fillColor: "white",
            lineWidth: 2,
            lineColor: observedColor
        }
    }, {
        name: "Forecast Best Guess",
        data: weiskirchenBestGuess,
        zIndex: 1,
        color: forecastColor,//Highcharts.getOptions().colors[0]
        marker: {
            fillColor: "white",
            lineWidth: 2,
            lineColor: forecastColor//Highcharts.getOptions().colors[0]
        }
    }, {
        name: "Forecast Range",
        data: weiskirchenRanges,
        type: "arearange",
        lineWidth: 0,
        linkedTo: ":previous",
        color: forecastColor, //Highcharts.getOptions().colors[0]
        fillOpacity: 0.3,
        zIndex: 0,
        marker: {
            enabled: true
        }
    }]
});