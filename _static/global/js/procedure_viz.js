var chart = Highcharts.chart("process_viz", {
  exporting: {
    enabled: false
  },
  chart: {
    type: "bar",
    height: (5 / 16 * 100) + '%', // 16:5 ratio
    backgroundColor: 'transparent'
  },
  title: {
    text: ""
  },
  xAxis: {
    categories: [""],
  },
  yAxis: {
    min: 0,
    title: {
      text: ""
    },
    tickPositions: [-2, 0, 2.5, 4.5, 5.5],
    labels: {
      formatter: function() {
        return
      }
    },
    plotBands: [{
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: -1.5,
      to: 0,
      label: {
        text: "Bereich:",
        align: 'right',
        x: -20,
        verticalAlign: "bottom",
        y: -10,
        style: {
          fontWeight: "bold"
        }
      }
    }, {
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: -1.5,
      to: 0,
      label: {
        text: "Aufgabe:",
        align: "right",
        x: -20,
        verticalAlign: "middle",
        y: 0,
        style: {
          fontWeight: "bold"
        }
      }
    }, {
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: -1.5,
      to: 0,
      label: {
        text: "Verfügbare Informationen:",
        align: "right",
        x: -20,
        verticalAlign: "top",
        y: +20,
        style: {
          fontWeight: "bold"
        }
      }
    }, { // mark round 1
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: 0,
      to: 2.5,
      label: {
        text: "Runde #1",
        align: 'center',
        verticalAlign: "bottom",
        y: -10
      }
    }, { // mark round 1
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: 0,
      to: 2.5,
      label: {
        text: "Gemessene Temperaturen",
        align: "center",
        verticalAlign: "top",
        y: +20
      }
    }, { // mark round 2
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: 2.5,
      to: 4.5,
      label: {
        text: "Runde #2",
        align: 'center',
        verticalAlign: "bottom",
        y: -10
      }
    }, { // mark round 2
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: 2.5,
      to: 4.5,
      label: {
        text: "Wettervorhersage",
        align: "center",
        verticalAlign: "top",
        y: +20
      }
    }, { // mark the end
      color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
      from: 4.5,
      to: 5.5,
      label: {
        text: "Abschluss",
        align: 'center',
        verticalAlign: "bottom",
        y: -10
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
    borderWidth: 1,
      animation: {
        duration: 1500
      },
      pointWidth: 150,
      stacking: "normal",
      dataLabels: {
        enabled: true,
        crop: false,
        allowOverlap: true,
        formatter: function() {
          return this.series.name;
        }
      }
    }
  },
  series: [{
    name: "Auflösung",
    color: "#7500c0",
    dataLabels: {
      rotation: 90
    },
    data: [0.5],
    showInLegend: false
  }, {
    name: "Abschließende Fragen",
    color: "#e6dcff",
    dataLabels: {
      rotation: 90
    },
    data: [0.5],
    showInLegend: false
  }, {
    name: 'Frageblock 2',
    color: "#a055f5",
    data: [1],
    showInLegend: false
  }, {
    name: 'Frageblock 1',
    color: "#be82ff",
    data: [1],
    showInLegend: false
  }, {
    name: 'Frageblock 2',
    color: "#a055f5",
    data: [1],
    showInLegend: false
  }, {
    name: "Instruktionen",
    color: "#e6dcff",
    dataLabels: {
      rotation: 90
    },
    data: [0.25],
    showInLegend: false
  }, {
    name: 'Frageblock 1',
    color: "#be82ff",
    data: [1],
    showInLegend: false
  }, {
    name: "Instruktionen",
    color: "#e6dcff",
    dataLabels: {
      rotation: 90
    },
    data: [0.25],
    showInLegend: false
  }]
});
