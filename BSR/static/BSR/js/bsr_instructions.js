// Make instructions interactive with a little quiz
	// initiate fields
	var minField = document.getElementById("test_minTemp");
	var maxField = document.getElementById("test_maxTemp");
	var field47  = document.getElementById("id_prob47");
	var chance47 = document.getElementById("chance2win47");

	// initiate alerts
	var maxmin_false = document.getElementById("maxminFalse");
	var maxmin_true  = document.getElementById("maxminTrue");
	var field47_false = document.getElementById("field47False");
	var field47_true  = document.getElementById("field47True");

	// initiate tabs
	var limits_tab = document.getElementById("limits_tab");
	var choice_tab = document.getElementById("choice_tab");
	var viz_tab    = document.getElementById("viz_tab");

	// initiate overarching elements
	var next_button = document.getElementById("nextButton");
	var part3_tab   = document.getElementById("part3-tab")
	var part4_tab   = document.getElementById("part4-tab")

	function validateMinMax(){
		if (minField.value == 42 && maxField.value == 47){
			minField.setAttribute("readonly", ""); 
			maxField.setAttribute("readonly", "");
			maxmin_true.style = "";
			maxmin_false.style ="display:none";
			choice_tab.className = "nav-link";

		} else {
			maxmin_false.style ="";
		}
	}

	function validationGuess(){
		if (field47.value == 10){
			field47.setAttribute("readonly", "");
			chance47.innerHTML = "50%";
			field47_true.style = "";
			field47_false.style ="display:none";
			viz_tab.className = "nav-link";

			next_button.style = "";
			part3_tab.className = "nav-link";
			part4_tab.className = "nav-link";
			
		} else {
			field47_false.style = "";
		}
	}







// ---------------------------------------------------------------------------------------------
// Make viz
	var chart = Highcharts.chart("example_viz", {
		exporting: {
			enabled: false
		},
        chart: {
            type: 'column'
        },
        title: {
            text: 'Ihre Gewinnchancen'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: ["42°C", "43°C", "44°C", "45°C", "46°C", "47°C"]// temps
            ,
            crosshair: true,
            showEmpty: false,

        },
        yAxis: {
            min: 0,
            max: 100,
            title: {
                text: 'Gewinnchance'
            }
        },
        tooltip: {
		    formatter: function() {
		        var s = '<b>'+ this.x +'</b>';
		        var chart = this.points[0].series.chart; //get the chart object
		        var categories = chart.xAxis[0].categories; //get the categories array
		        var index = 0;
		        while(this.x !== categories[index]){index++;} //compute the index of corr y value in each data arrays           
		        $.each(chart.series, function(i, series) { //loop through series array
		            s += '<br/>'+ series.name +': ' +
		                series.data[index].y +'%';     //use index to get the y value
		        });           
		        return s;
		    },
		    shared: true
		},
        plotOptions: {
            column: {
                pointPadding: 0.05,
                borderWidth: 0,
                shadow: false,
                groupPadding: 0,
                color: "#C582FF"// "#33b5eb" // "#3479F6"//'#1FE68E'
            }
        },
        series: [
        	{
            name: 'Beispielhafte Schätzung',
            data: [10, 20, 30, 20, 10, 10],
            showInLegend: false,
            visible: false
            },
            {
            name: "Gewinnchance",
            data: [50, 60, 70, 60, 50, 50],
            visible: true,
            showInLegend: false
        	}
    	]
	});