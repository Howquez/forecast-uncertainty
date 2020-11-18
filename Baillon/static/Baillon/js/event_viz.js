// get vars from python
    let ticksArray   = js_vars.ticks;
    let event        = js_vars.event_decision;
    let enabledLabel = js_vars.enabledLabel;
    console.log(enabledLabel)

// set constants
    // const events = ["E1", "E2", "E3", "E12", "E23", "E13"];
    const successColor = "#5DE58E";
    const lossColor    = "#FF5B66";

// set variables
    var treatmentDiff = 0; // legacy
    var S1Col = lossColor;
    var S2Col = lossColor;
    var S3Col = lossColor;
    var subHeader;

    var labelArray = ticksArray.map( function(value) {return value - treatmentDiff} );


// set color (and implicitly the label) of barchart
    if (/1/.test(event)){
        S1Col = successColor
    }

    if (/2/.test(event)){
        S2Col = successColor
    }

    if (/3/.test(event)){
        S3Col = successColor
    }

// set subheader of table
    var E1SubHeader  = "<em>Sie gewinnen 10 Euro, wenn die Temperatur bis einschließlich 7,9°C beträgt (und sonst nichts).</em>";
    var E2SubHeader  = "<em>Sie gewinnen 10 Euro, wenn die Temperatur zwischen 8,0°C und 13,9°C beträgt (und sonst nichts).</em>";
    // var E3SubHeader  = "<em>Sie gewinnen 10 Euro, wenn die Temperatur mindestens 14,0°C beträgt (und sonst nichts).</em>";
    var E3SubHeader  = `<em>Sie gewinnen 10 Euro, wenn die Temperatur mindestens ${labelArray[2]}°C (und sonst nichts).</em>`;
    // var E12SubHeader = "<em>Sie gewinnen 10 Euro, wenn die Temperatur höchstens 13,9°C beträgt (und sonst nichts).</em>";
    var E12SubHeader = `<em>Sie gewinnen 10 Euro, wenn die Temperatur höchstens ${labelArray[2]-1},9°C beträgt (und sonst nichts).</em>`;
    var E23SubHeader = `<em>Sie gewinnen 10 Euro, wenn die Temperatur mindestens ${labelArray[1]},0°C oder mehr beträgt (und sonst nichts).</em>`;
    var E13SubHeader = "<em>Sie gewinnen 10 Euro, wenn die Temperatur bis einschließlich 7,9°C oder 14,0°C und mehr beträgt (und sonst nichts).</em>";

    // var E1SubHeader  = `<em>Sie gewinnen 10 Euro, wenn die Temperatur bis einnschließlich ${labelArray[1]}°C beträgt (und sonst nichts).</em>`;
    // var E2SubHeader  = `<em>Sie gewinnen 10 Euro, wenn die Temperatur ${labelArray[1]}°C bis ${labelArray[2]}°C beträgt (und sonst nichts).</em>`;
    // var E3SubHeader  = `<em>Sie gewinnen 10 Euro, wenn die Temperatur ${labelArray[2]}°C oder mehr beträgt (und sonst nichts).</em>`;
    // var E12SubHeader = `<em>Sie gewinnen 10 Euro, wenn die Temperatur bis zu ${labelArray[2]}°C beträgt (und sonst nichts).</em>`;
    // var E23SubHeader = `<em>Sie gewinnen 10 Euro, wenn die Temperatur ${labelArray[1]}°C oder mehr beträgt (und sonst nichts).</em>`;
    // var E13SubHeader = `<em>Sie gewinnen 10 Euro, wenn die Temperatur bis zu ${labelArray[1]}°C oder ${labelArray[2]}°C oder mehr beträgt (und sonst nichts).`;


    subHeader = window[event.concat("SubHeader")];
    console.log(subHeader)
    document.getElementById("subHeader").innerHTML = subHeader;


var chart = Highcharts.chart('container', {
    exporting: {
        enabled: false
    },

    chart: {
        type: "bar",
        height: (9 / 16 * 100) + '%', // 16:9 ratio
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
        color: S3Col,
    }, {
        label: "Series2",
        name: "8,0°C bis einschließlich 13,9°C", //`${labelArray[1]}°C bis ${labelArray[2]}°C` ,//"8°C bis 14°C",
        data: [ticksArray[2] - ticksArray[1]],
        showInLegend: false,
        color: S2Col,
    }, {
        label: "Series1",
        name: "bis einschließlich 7,9°C", //`bis zu ${labelArray[1]}°C` , //"bis zu 8°C",
        data: [ticksArray[1] - ticksArray[0]],
        showInLegend: false,
        color: S1Col,
    }]
});