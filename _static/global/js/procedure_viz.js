var chart = Highcharts.chart("process_viz", {
  exporting: {
    enabled: false
  },
  chart: {
    type: "bar",
    height: (5 / 16 * 100) + '%' // 16:5 ratio
  },
  title: {
    text: ""
  },
  xAxis: {
    categories: [""]
  },
  yAxis: {
    min: 0,
    title: {
      text: ""
    },
    tickPositions: [0, 2.5, 5, 6.5],
    labels: {
      formatter: function() {
        return
      }
    },
    plotBands: [{ // mark round 1
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: 0,
      to: 2.5,
      label: {
        text: "Runde 1",
        align: 'center',
        verticalAlign: "bottom",
        y: -20
      }
    }, { // mark round 2
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: 2.5,
      to: 5,
      label: {
        text: "Runde 2",
        align: 'center',
        verticalAlign: "bottom",
        y: -20
      }
    }, { // mark the end
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: 5,
      to: 6.5,
      label: {
        text: "Abschluss",
        align: 'center',
        verticalAlign: "bottom",
        y: -20
      }
    }]
  },
  legend: {
    reversed: true
  },
  tooltip: {
    formatter: function() {
      return this.series.name 
    }
  },
  plotOptions: {
    series: {
      animation:{
        duration: 1500
      },
      pointWidth: 150,
      stacking: "normal",
      dataLabels: {
        enabled: true,
        crop: false,
        allowOverlap: true,
        rotation: 90,
        formatter: function() {
          return this.series.name;
        }
      }
    }
  },
  series: [{
    name: "Auflösung",
    color: "#40FFA2",
    data: [1],
    showInLegend: false
  }, {
    name: "Abschließende Fragen",
    color: "#2EE8C3",
    data: [0.5],
    showInLegend: false
  }, {
    name: 'Frageblock 2',
    color: "#FFE226",
    data: [1],
    showInLegend: false
  }, {
    name: 'Frageblock 1',
    color: "#ffbb33",
    data: [1],
    showInLegend: false
  }, {
    name: "Wettervorhersage",
    color: "#ff4444",
    data: [0.5],
    showInLegend: false
  }, {
    name: 'Frageblock 2',
    color: "#FFE226",
    data: [1],
    showInLegend: false
  }, {
    name: 'Frageblock 1',
    color: "#ffbb33",
    data: [1],
    showInLegend: false
  }, {
    name: "Beobachtetes Wetter",
    color: "#ff4444",
    data: [0.5],
    showInLegend: false
  }]
});
