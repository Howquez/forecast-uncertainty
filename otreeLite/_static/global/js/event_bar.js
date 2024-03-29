console.log("barchart ready!")

// get vars from python
    let ticksArray   = js_vars.ticks;
    let event        = js_vars.event_decision;
    let enabledLabel = js_vars.enabledLabel;
    let results = js_vars.results || true; // determines size of visualization

// set constants
    const pattern = "M 0 0 L 10 10 M 9 -1 L 11 1 M -1 9 L 1 11"; //"M 3 0 L 3 10 M 8 0 L 8 10"; // more patterns here: https://www.highcharts.com/docs/chart-design-and-style/pattern-fills
    const successColor = "#36D6B0";
    const successLabel = {
        backgroundColor: "rgba(255, 255, 255, 0.33)",
        style: {
            fontWeight: "normal",
            textOutline: 0,
        },
    };

    const lossColor = {
        pattern: {
            path: pattern,
            color: "#FF0B5F",
            width: 10,
            height: 10,
            patternTransform: "scale(2)"
        }
    };
    const lossLabel = {
        style: {
            color: "#000000"
        }
    }


// set variables
    var S1Col = lossColor;
    var S2Col = lossColor;
    var S3Col = lossColor;

    var S1Label = lossLabel
    var S2Label = lossLabel
    var S3Label = lossLabel
    var subHeader;

    var labelArray = ticksArray;

// height of chart
    var height = 9;
    if (results){
        height = 5;
    }


// set color (and implicitly the label) of barchart
    if (/1/.test(event)){
        S1Col = successColor
        S1Label = successLabel
    }

    if (/2/.test(event)){
        S2Col = successColor
        S2Label = successLabel
    }

    if (/3/.test(event)){
        S3Col = successColor
        S3Label = successLabel
    }

// set subheader of table
    var E1SubHeader  = "<small>You win 10 euros if the temperature is below 8°C (and nothing otherwise).</small>";
    var E2SubHeader  = "<small>You win 10 euros if the temperature is between 8°C and 14°C inclusive (and nothing otherwise).</small>";
    var E3SubHeader  = "<small>You win 10 euros if the temperature is above 14°C beträgt (and nothing otherwise).</small>";
    var E12SubHeader = "<small>You win 10 euros if the temperature is 14°C or less (and nothing otherwise).</small>";
    var E23SubHeader = "<small>You win 10 euros if the temperature is 8°C or more  (and nothing otherwise).</small>";
    var E13SubHeader = "<small>You win 10 euros if the temperature is below 8°C or above 14°C (and nothing otherwise).</small>";

    // var E1SubHeader  = `<em>Sie gewinnen 10 Euro, wenn die Temperatur bis einschließlich ${labelArray[1]}°C beträgt (und sonst nichts).</em>`;
    // var E2SubHeader  = `<em>Sie gewinnen 10 Euro, wenn die Temperatur ${labelArray[1]}°C bis ${labelArray[2]}°C beträgt (und sonst nichts).</em>`;
    // var E3SubHeader  = `<em>Sie gewinnen 10 Euro, wenn die Temperatur ${labelArray[2]}°C oder mehr beträgt (und sonst nichts).</em>`;
    // var E12SubHeader = `<em>Sie gewinnen 10 Euro, wenn die Temperatur bis zu ${labelArray[2]}°C beträgt (und sonst nichts).</em>`;
    // var E23SubHeader = `<em>Sie gewinnen 10 Euro, wenn die Temperatur ${labelArray[1]}°C oder mehr beträgt (und sonst nichts).</em>`;
    // var E13SubHeader = `<em>Sie gewinnen 10 Euro, wenn die Temperatur bis zu ${labelArray[1]}°C oder ${labelArray[2]}°C oder mehr beträgt (und sonst nichts).`;


    subHeader = window[event.concat("SubHeader")];
    // console.log(subHeader)
    document.getElementById("subHeader").innerHTML = subHeader;

$(function () {
	$(document).ready(function(){

		$('.event_bar').each(function(){
            var bar = new Highcharts.chart({
                    exporting: {
                        enabled: false
                    },

                    chart: {
                        renderTo: this,
                        type: "column",
                        // height: (5 / 15 * 100) + '%', // 16:9 ratio
                        backgroundColor: 'transparent'
                    },
                    title: {
                        text: "" //event,
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
                                    label = parseInt(label).toString();
                                    return label.concat("°C")
                                }
                            },
                            style: {
                                    fontWeight: "normal",
                                }
                        },
                        //showFirstLabel: false,
                        //showLastLabel: false,
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
                                return "You win 10 euros.";
                            } else {
                                return "You win nothing."
                            }
                        }
                    },

                    plotOptions: {
                        series: {
                            stacking: "normal",
                            pointWidth: 150,
                            dataLabels: {
                                enabled: enabledLabel,
                                borderWidth: 0,
                                style: {
                                    fontWeight: "bold",
                                    textOutline: 1,
                                },
                                color: "#000000",
                                backgroundColor: "rgba(255, 255, 255, 0.75)",
                                borderRadius: 5,
                                padding: 4,
                                formatter: function() {
                                    return this.series.name;
                                    }
                            }
                        }
                    },

                    series: [{
                        label: "Series3",
                        name: "above 14°C", //`${labelArray[2]}°C und drüber` ,// "14°C und drüber",
                        data: [ticksArray[3] - ticksArray[2]],
                        showInLegend: false,
                        color: S3Col,
                        dataLabels: S3Label
                    }, {
                        label: "Series2",
                        name: "from 8°C to <br> 14°C inclusive", //`${labelArray[1]}°C bis ${labelArray[2]}°C` ,//"8°C bis 14°C",
                        data: [ticksArray[2] - ticksArray[1]],
                        showInLegend: false,
                        color: S2Col,
                        dataLabels: S2Label
                    }, {
                        label: "Series1",
                        name: "below 8°C", //`bis zu ${labelArray[1]}°C` , //"bis zu 8°C",
                        data: [ticksArray[1] - ticksArray[0]],
                        showInLegend: false,
                        color: S1Col,
                        dataLabels: S1Label
                    }]
            });
        });
	});
});

