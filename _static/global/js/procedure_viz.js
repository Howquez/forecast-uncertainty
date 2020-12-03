let cloudiness = js_vars.opacity || 1;

var timeline = Highcharts.chart("timeline_viz", {
  exporting: {
    enabled: false
  },
  chart: {
    type: "timeline"
  },
  accessibility: {
    screenReaderSection: {
      beforeChartFormat: '<h5>{chartTitle}</h5>' +
        '<div>{typeDescription}</div>' +
        '<div>{chartSubtitle}</div>' +
        '<div>{chartLongdesc}</div>' +
        '<div>{viewTableButton}</div>'
    },
    point: {
      valueDescriptionFormat: '{index}. {point.label}. {point.description}.'
    }
  },
  xAxis: {
    visible: false
  },
  yAxis: {
    visible: false
  },
  title: {
    text: ""
  },
  subtitle: {
    text: ""
  },
  colors: [
    '#4185F3',
    '#427CDD',
    '#406AB2',
    '#3E5A8E',
    '#3B4A68',
    '#363C46'
  ],
  series: [{
    data: [{
      name: "Einleitung",
      label: "Allgemeine Erklärungen",
      description: '22 July 1951 First dogs in space (Dezik and Tsygan) '
    }, {
      name: "1. Aufgabe",
      label: "Mit spezifischen Instruktionen",
      description: '4 October 1957 First artificial satellite. First signals from space.'
    }, {
      name: "2. Aufgabe",
      label: "Besteht aus sechs Entscheidungssituationen",
      description: 'First human spaceflight (Yuri Gagarin), and the first human-crewed orbital flight'
    }, {
      name: "3. Aufgabe",
      label: "Besteht aus einer Enntscheidungssituation",
      description: 'First human on the Moon, and first space launch from a celestial body other than the Earth. First sample return from the Moon'
    }, {
      name: "4. Aufgabe",
      label: "Wie die zweite Aufgabe aber mit Zusatzinformationen",
      description: 'Salyut 1 was the first space station of any kind, launched into low Earth orbit by the Soviet Union on April 19, 1971.'
    }, {
      name: "Schluss",
      label: "Auflösung und Bezahlung",
      description: 'The mission included both joint and separate scientific experiments, and provided useful engineering experience for future joint US–Russian space flights, such as the Shuttle–Mir Program and the International Space Station.'
    }]
  }]
});


// console.log(cloudiness);

// var chart = Highcharts.chart("process_viz", {
//   exporting: {
//     enabled: false
//   },
//   chart: {
//     type: "bar",
//     height: (5 / 16 * 100) + '%', // 16:5 ratio
//     backgroundColor: 'transparent'
//   },
//   title: {
//     text: ""
//   },
//   xAxis: {
//     categories: [""],
//   },
//   yAxis: {
//     min: 0,
//     title: {
//       text: ""
//     },
//     tickPositions: [-2, 0, 2.5, 4.5, 5.5],
//     labels: {
//       formatter: function() {
//         return
//       }
//     },
//     plotBands: [{
//       color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
//       from: -1.5,
//       to: 0,
//       label: {
//         text: "Bereich:",
//         align: 'right',
//         x: -20,
//         verticalAlign: "bottom",
//         y: -10,
//         style: {
//           fontWeight: "bold"
//         }
//       }
//     }, {
//       color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
//       from: -1.5,
//       to: 0,
//       label: {
//         text: "Aufgabe:",
//         align: "right",
//         x: -20,
//         verticalAlign: "middle",
//         y: 0,
//         style: {
//           fontWeight: "bold"
//         }
//       }
//     }, {
//       color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
//       from: -1.5,
//       to: 0,
//       label: {
//         text: "Verfügbare Informationen:",
//         align: "right",
//         x: -20,
//         verticalAlign: "top",
//         y: +20,
//         style: {
//           fontWeight: "bold"
//         }
//       }
//     }, { // mark round 1
//       color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
//       from: 0,
//       to: 2.5,
//       label: {
//         text: "Runde #1",
//         align: 'center',
//         verticalAlign: "bottom",
//         y: -10
//       }
//     }, { // mark round 1
//       color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
//       from: 0,
//       to: 2.5,
//       label: {
//         text: "Gemessene Temperaturen",
//         align: "center",
//         verticalAlign: "top",
//         y: +20
//       }
//     }, { // mark round 2
//       color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
//       from: 2.5,
//       to: 4.5,
//       label: {
//         text: "Runde #2",
//         align: 'center',
//         verticalAlign: "bottom",
//         y: -10
//       }
//     }, { // mark round 2
//       color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
//       from: 2.5,
//       to: 4.5,
//       label: {
//         text: "Wettervorhersage",
//         align: "center",
//         verticalAlign: "top",
//         y: +20
//       }
//     }, { // mark the end
//       color: "rgba(173, 0, 155, 0)", // add opacity 0<opacity<1 here
//       from: 4.5,
//       to: 5.5,
//       label: {
//         text: "Abschluss",
//         align: 'center',
//         verticalAlign: "bottom",
//         y: -10
//       }
//     }]
//   },
//   legend: {
//     reversed: true
//   },
//   tooltip: {
//     formatter: function() {
//       return this.series.name
//     }
//   },
//   plotOptions: {
//     series: {
//     borderWidth: 1,
//       animation: {
//         duration: 1500
//       },
//       pointWidth: 150,
//       stacking: "normal",
//       dataLabels: {
//         enabled: true,
//         crop: false,
//         allowOverlap: true,
//         formatter: function() {
//           return this.series.name;
//         }
//       }
//     }
//   },
//   series: [{
//     name: "Auflösung",
//     color: "#7500c0",
//     dataLabels: {
//       rotation: 90
//     },
//     data: [0.5],
//     showInLegend: false
//   }, {
//     name: "Abschließende Fragen",
//     color: "#e6dcff",
//     dataLabels: {
//       rotation: 90
//     },
//     data: [0.5],
//     showInLegend: false
//   }, {
//     name: 'Frageblock 2',
//     color: "rgba(160, 85, 245, 1)", // "#a055f5",
//     data: [1],
//     showInLegend: false
//   }, {
//     name: 'Frageblock 1',
//     color: "rgba(190, 130, 255, 1)", // "#be82ff",
//     data: [1],
//     showInLegend: false
//   }, {
//     name: 'Frageblock 2',
//     color: `rgba(160, 85, 245, ${cloudiness})`, // "#a055f5",
//     data: [1],
//     showInLegend: false
//   }, {
//     name: "Instruktionen",
//     color: "#e6dcff",
//     dataLabels: {
//       rotation: 90
//     },
//     data: [0.25],
//     showInLegend: false
//   }, {
//     name: 'Frageblock 1',
//     color: `rgba(190, 130, 255, ${cloudiness})`, // "#be82ff",
//     data: [1],
//     showInLegend: false
//   }, {
//     name: "Instruktionen",
//     color: "#e6dcff",
//     dataLabels: {
//       rotation: 90
//     },
//     data: [0.25],
//     showInLegend: false
//   }]
// });
