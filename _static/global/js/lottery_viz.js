// initiate variables
var red = 100;
var green = 0;
var primary = "#0275d8"



// get pattern stuff done
// function getColorPattern() {
//     var colors = Highcharts.getOptions().colors,
//         patternColor = lossColor

//     return {
//         pattern: {
//             path: pattern,
//             color: patternColor,
//             width: 5,
//             height: 5
//         }
//     };
// }



// change content on input
document.getElementById("id_probability").addEventListener('input', () => {
  green = parseInt(document.getElementById("id_probability").value) || 0;
  red = 100 - green;

  document.getElementById("quote").innerHTML = `<b><u>${green}</u></b>`;
  document.getElementById("bubbleId").className = "bubble lead";

  pie.series[0].update({
    data: [{
        y: red,
      },
      {
        y: green,
      }
    ]

  });

  tradeoff.series[0].update({
    data: [red]
  });

  tradeoff.series[1].update({
    data: [green]
  });

  tradeoff.yAxis[0].update({
    tickPositions: [0, green, 100]
  });

});


// define pie chart
var pie = Highcharts.chart('pieChart', {
  exporting: {
    enabled: false
  },
  chart: {
    plotBackgroundColor: null,
    plotBorderWidth: null,
    plotShadow: false,
    type: "pie",
    backgroundColor: "transparent"
  },
  title: {
    text: ""
  },
  tooltip: {
    formatter: function() {
      if (this.point.color == successColor) {
        return "Sie gewinnen 10 Euro.";
      } else {
        return "Sie gewinnen nichts."
      }
    }
  },
  accessibility: {
    point: {
      valueSuffix: "%"
    }
  },
  plotOptions: {
    pie: {
      allowPointSelect: true,
      cursor: "pointer",
      dataLabels: {
        distance: 15,
        enabled: true,
        format: "{point.percentage:.0f} %", //"<b>{point.name}</b>: {point.percentage:.0f} %"
        style: {
          fontWeight: "normal"
        }
      },
    }
  },
  series: [{
    name: "Kugeln",
    colorByPoint: true,
    data: [{
        name: "rot",
        y: 50,
        sliced: true,
        selected: true,
        color: lossColor
      },
      {
        name: "grün",
        y: 50,
        sliced: true,
        selected: true,
        color: successColor
      }
    ]
  }]
});



// define horizontal trade-off bar
var tradeoff = Highcharts.chart("tradeoff_bar", {
  exporting: {
    enabled: false
  },
  chart: {
    type: "bar",
    height: 11 + '%',
  },
  title: {
    text: ""
  },
  xAxis: {
    categories: [""]
  },
  yAxis: {
    min: 0,
    max: 100,
    tickPositions: [0, 50, 100],
    labels: {
      formatter: function() {
        var label = this.axis.defaultLabelFormatter.call(this);
        label = (parseInt(label)).toString();
        if (label == this.axis.tickPositions[1]){
          return label.concat(" grüne Kugeln")
        } else {
          return label//.concat(" Kugeln")
        }
        
      },
      style: {
        fontWeight: "normal",
      }
    },
    title: {
      text: ""
    }
  },
  legend: {
    reversed: true
  },
  plotOptions: {
    series: {
      stacking: "normal",
      pointWidth: 150,
      dataLabels: {
        enabled: true,
        borderWidth: 0,
        style: {
          color: primary,
          textOutline: 0,
          fontWeight: "normal",
        },
        formatter: function() {
          return "Ich bevorzuge die "+ this.series.name;
        }
      }
    }
  },
  series: [{
    name: "Lotterie",
    color: "transparent",
    borderWidth: 2,
    borderColor: primary,
    showInLegend: false,
    data: [50]
  }, {
    name: "Wette",
    color: primary,
    borderWidth: 2,
    borderColor: primary,
    showInLegend: false,
    dataLabels: {style: {color: "#FFFFFF"}},
    data: [50]
  }]
});


