var example = Highcharts.chart("example_viz", {
    exporting: {
        enabled: false
    },

    chart: {
        type: "bar",
        height: (9 / 16 * 100) + '%', // 16:9 ratio
        backgroundColor: 'transparent'
    },
    title: {
        text: event,
    },
    subtitle: {
        text: "",
    },
    xAxis: {
        categories: [""],
    },
    yAxis: {
        min: 0,
        max: 24,
        tickPositions: ticksArray,
        labels: {
            formatter: function () {
                var label = this.axis.defaultLabelFormatter.call(this);
                if (label == ticksArray[0]) {
                    return "-"
                } else if (label == ticksArray[ticksArray.length - 1]) {
                    return "+"
                } else {
                    label = (parseInt(label) - treatmentDiff).toString();
                    return label.concat("°C")
                }
            },
            style: {
                    fontWeight: "bold",
                }
        },

        title: {
            text: ""
        }
    },
    legend: {
        reversed: true
    },

    tooltip: {
        formatter: function() {
            if (this.series.color == successColor) {
                return "Sie gewinnen 10 Euro.";
            } else {
                return "Sie gewinnen nichts."
            }
        }
    },

    plotOptions: {
        series: {
            stacking: "normal",
            dataLabels: {
                enabled: enabledLabel,
                formatter: function() {                
                    return this.series.name;
                    }
            }
        }
    },

    series: [{
        label: "Series3",
        name: "14,0°C und drüber", //`${labelArray[2]}°C und drüber` ,// "14°C und drüber",
        data: [ticksArray[3] - ticksArray[2]],
        showInLegend: false,
        color: lossColor,
    }, {
        label: "Series2",
        name: "8,0°C bis einschließlich 13,9°C", //`${labelArray[1]}°C bis ${labelArray[2]}°C` ,//"8°C bis 14°C",
        data: [ticksArray[2] - ticksArray[1]],
        showInLegend: false,
        color: successColor,
    }, {
        label: "Series1",
        name: "bis einschließlich 7,9°C", //`bis zu ${labelArray[1]}°C` , //"bis zu 8°C",
        data: [ticksArray[1] - ticksArray[0]],
        showInLegend: false,
        color: lossColor,
    }]
});

