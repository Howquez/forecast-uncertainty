var ranges = [
        [1248048000000, null, null], //11.0, 19.3],
        [1248134400000, null, null], //11.0, 19.3],
        [1248220800000, null, null], //11.0, 19.3],
        [1248307200000, null, null], //11.0, 19.3],
        [1248393600000, null, null], //11.0, 19.3],
        [1248480000000, null, null], //11.0, 19.3],
        [1248566400000, null, null], //11.0, 19.3],
        [1248652800000, null, null], //11.0, 19.3],
        [1248739200000, null, null], //11.0, 19.3],
        [1248825600000, 3.3, 9.3],
        [1248912000000, 2.1, 8.1],
        [1248998400000, 2.2, 8.2]
    ],
    averages = [
        [1248048000000, 12.4],
        [1248134400000, 12.7],
        [1248220800000, 12.7],
        [1248307200000, null],
        [1248393600000, null],
        [1248480000000, null],
        [1248566400000, null],
        [1248652800000, null],
        [1248739200000, null],
        [1248825600000, 4.3],
        [1248912000000, 3.7],
        [1248998400000, 3.6]
    ];


var chart = Highcharts.chart('container', {

    title: {
        text: 'July temperatures'
    },

    xAxis: {
        type: 'datetime',
        accessibility: {
            rangeDescription: 'Range: Jul 1st 2009 to Jul 31st 2009.'
        }
    },

    yAxis: {
        title: {
            text: null
        }
    },

    tooltip: {
        crosshairs: true,
        shared: true,
        valueSuffix: '°C'
    },

    series: [{
        name: 'Temperature',
        data: averages,
        zIndex: 1,
        marker: {
            fillColor: 'white',
            lineWidth: 2,
            lineColor: Highcharts.getOptions().colors[0]
        }
    }, {
        name: 'Range',
        data: ranges,
        type: 'arearange',
        lineWidth: 0,
        linkedTo: ':previous',
        color: Highcharts.getOptions().colors[0],
        fillOpacity: 0.3,
        zIndex: 0,
        marker: {
            enabled: false
        }
    }]
});