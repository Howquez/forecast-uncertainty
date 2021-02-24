// vars from oTree
let compound   = js_vars.compound;


// initiate variables
var green = 33;
if (compound) {
  green = 66;
}
var red = 100 - green;
var primary = "#0275d8";

// change content on input
document.getElementById("id_matching_probability").addEventListener('input', () => {
    green = parseInt(document.getElementById("id_matching_probability").value) || 0;
    red = 100 - green;

    if(green>0){
        document.getElementById("submitCheckLabel").innerHTML = `<small>Bei ${green - 1} oder weniger grünen Kugeln würde ich mich für die Wette entscheiden.</small>`;
    } else {
        document.getElementById("submitCheckLabel").innerHTML = `<small>Ich würde mich nie für die Wette entscheiden.</small>`;
    }

    //document.getElementById("submitCheck").setAttribute("checked", "");
    document.getElementById("submitButton").removeAttribute("disabled");
    document.getElementById("collapseSubmit").setAttribute("aria-expanded", "true");
    document.getElementById("collapseSubmit").className = "";

    pie.series[0].update({
        data: [{
            y: red,
          },
          {
            y: green,
          }
        ]
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
    // height: "105%",
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
        y: red,
        sliced: true,
        selected: true,
        color: lossColor
      },
      {
        name: "grün",
        y: green,
        sliced: true,
        selected: true,
        color: successColor
      }
    ]
  }]
});
