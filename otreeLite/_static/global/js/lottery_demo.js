var chart = Highcharts.chart("lottery_demo", {

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
                return "You win 10 euros.";
              } else {
                return "You win nothing."
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
            name: "balls",
            colorByPoint: true,
            data: [{
                name: "red",
                y: 50,
                sliced: true,
                selected: true,
                color: lossColor
              },
              {
                name: "green",
                y: 50,
                sliced: true,
                selected: true,
                color: successColor
              }
            ]
            }]
            });

