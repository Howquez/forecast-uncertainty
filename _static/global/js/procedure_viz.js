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
  tooltip: {
    enabled: false
  },
  series: [{
    data: [{
      name: "Einleitung",
      label: "Allgemeine Erklärungen",
      description: ""
    }, {
      name: "1. Aufgabe",
      label: "Erklärung der Aufgabe und sechs Entscheidungssituationen",
      description: ""
    }, {
      name: "2. Aufgabe",
      label: "Erklärung der Aufgabe und eine Entscheidungssituationen",
      description: ""
    }, {
      name: "3. Aufgabe",
      label: "Erneutes Ausfüllen der ersten Aufgabe mit Hilfe einer Wettervorhersage",
      description: ""
    }, {
      name: "4. Aufgabe",
      label: "Erneutes Ausfüllen der zweiten Aufgabe mit Hilfe einer Wettervorhersage",
      description: ""
    }, {
      name: "Schluss",
      label: "Fragen zu Ihrer Person und Auflösung sowie Bezahlung",
      description: ""
    }]
  }]
});