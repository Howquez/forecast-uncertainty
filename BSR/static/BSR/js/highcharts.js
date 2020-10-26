var chart = Highcharts.chart('container', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Ihre Wahrscheinlichkeitsverteilung'
        },
        subtitle: {
            text: 'Hier könnte Ihr Subtitle stehen'
        },
        xAxis: {
            categories: [

            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Wahrscheinlichkeit'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.05,
                borderWidth: 0,
                shadow: false,
                groupPadding: 0,
                color: '#1FE68E'
            }
        },
        series: [{
            name: 'Wahrscheinlichkeit',
            data: []
            }]
    });


$('#calculator').click(function () {
    chart.update({
        xAxis: {
            categories: [
                '20°C',
                '21°C',
                '22°C',
                '23°C'
            ],
            crosshair: true
        },
        series: [{
        name: 'Wahrscheinlichkeit',
        data: [10, 20, 50, 20]
        }]
    });
});

$('#refresher').click(function () {
    chart.update({
        xAxis: {
            categories: [
                JSON.stringify(temps+minTemp)
            ],
            crosshair: true
        },
        series: [{
        name: 'Wahrscheinlichkeit',
        data: [10, 50, 40]
        }]
    });
});

