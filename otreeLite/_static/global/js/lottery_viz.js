console.log("pie chart & live updates ready!")


// vars from oTree
let compound = js_vars.compound;
let template = js_vars.template;


// initiate variables
var green = 34;
if (compound) {
  green = 67;
}
var red = 100 - green;
var primary = "#0275d8";

// disable scrolling on number-input
document.addEventListener("wheel", function(event){
    if(document.activeElement.type === "number"){
        document.activeElement.blur();
    }
});

// change content on input
document.getElementById("id_matching_probability").addEventListener('input', () => {
    green = parseInt(document.getElementById("id_matching_probability").value) || 0;
    red = 100 - green;

    if(green<=0){
        document.getElementById("submitCheckLabel").innerHTML = `<small>Ich würde mich nie für die Wette entscheiden.</small>`;
    } else if (green > 100) {
        document.getElementById("submitCheckLabel").innerHTML = `<small>Ich würde mich immer für die Wette entscheiden.</small>`;
    } else {
        document.getElementById("submitCheckLabel").innerHTML = `<small>Bei ${green - 1} oder weniger grünen Kugeln würde ich mich für die Wette entscheiden.</small>`;
    }

    if(template!="instructions"){
        document.getElementById("submitButton").removeAttribute("disabled");
    }
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

var pie;

// define pie chart
$(function () {
	$(document).ready(function(){

		$('.pieChart').each(function(){

            pie = new Highcharts.chart({
              exporting: {
                enabled: false
              },
              chart: {
                renderTo: this,
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
         });
	});
});
