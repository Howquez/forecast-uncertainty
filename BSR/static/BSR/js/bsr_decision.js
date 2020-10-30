console.log("bsr_decision_js is running")


// ---------------------------------------------------------------------------------------------
// Schritt 1 Tab
	function validation(){
		// declare variables
		// get field values
		var minTemp = parseInt(document.getElementById("id_minTemp").value);
		var maxTemp = parseInt(document.getElementById("id_maxTemp").value);
		// get fields
		var minField = document.getElementById("id_minTemp");
		var maxField = document.getElementById("id_maxTemp");
		// get tabs
		var choice_tab = document.getElementById("choice_tab");
		// get buttons
		var limits_validation = document.getElementById("limits_validation");
		var limits_revision = document.getElementById("limits_revision");


		//
		if (maxTemp < minTemp) {
			alert("Die höchste Temperatur, die sie für möglich halten, muss höher sein, als die niedrigste Temperatur, die Sie für möglich halten.");
			choice_tab.className = "nav-link disabled";
			return false;
		}

		//
		if (maxTemp == NaN || minTemp == NaN) {
			alert("Bitte tragen Sie ganze Zahlenwerte ein.");
			choice_tab.className = "nav-link disabled";
			return false;
		}

		//
		if (minTemp <= maxTemp){
			minField.setAttribute("readonly", "");
			maxField.setAttribute("readonly", "");
			choice_tab.className = "nav-link";
			limits_validation.style = "display:none";
			limits_revision.style = "";
			createTable();
			createCols();
			createHiddenFields();
			// calcChance2win();

		}
	}

	function revision(){
		// get fields
		var minField = document.getElementById("id_minTemp");
		var maxField = document.getElementById("id_maxTemp");
		// get tabs
		var viz_tab = document.getElementById("viz_tab");
		var choice_tab = document.getElementById("choice_tab");
		// get buttons
		var limits_validation = document.getElementById("limits_validation");
		var limits_revision = document.getElementById("limits_revision");

		//
		limits_validation.style = "";
		limits_revision.style = "display:none";

		//
		minField.removeAttribute("readonly");
		maxField.removeAttribute("readonly");

		//
		choice_tab.className = "nav-link disabled";
		viz_tab.className = "nav-link disabled";

		//
		removeTable()
	}

// ---------------------------------------------------------------------------------------------
// Schritt 2 Tab


// tge following two functions create or remove a table, that is later to be filled with createCols()
	function createTable(){
		document.getElementById("table-wrapper").innerHTML = '<div id="table-scroll"> <table class="table table-highlight table-hover"> <tr id="guessRow"> <th>Ihre Schätzung</th> </tr> <tr id="tempRow"> <th>Temperatur</th> </tr> <tr id="chanceRow"> <th>Ihre Gewinnchance</th> </tr> </table> </div>'
	}

	function removeTable(){
		document.getElementById("table-wrapper").innerHTML = ""
	}

// hidden fields contain forms that are not used but assigned to the page. They'll default to zero
	function createHiddenFields(){
		var minTemp = parseInt(document.getElementById("id_minTemp").value);
		var maxTemp = parseInt(document.getElementById("id_maxTemp").value);
		var temps = Array.from(seq(minTemp, maxTemp));

		var div = document.getElementById("hidden_fields");
		var div_content = ""

		for (i = 0; i <= minTemp; ++i){
			div_content += `<input name="prob${i}" id="id_prob${i}" type="hidden" value="0" min="0" max="0" readonly>`
		}

		for (j = maxTemp + 1; j <= 100; ++j){
			div_content += `<input name="prob${j}" id="id_prob${j}" type="hidden" value="0" min="0" max="0" readonly>`
		}

		div.innerHTML = div_content;

	}

// create Cols loops throug the available temperaturs between minTemp and maxTemp and creates form fields 
// with labels and a prelimenarily empty chance2win. One column for each temperature.
	function createCols(){

		//
		var minTemp = parseInt(document.getElementById("id_minTemp").value);
		var maxTemp = parseInt(document.getElementById("id_maxTemp").value);
		var temps = Array.from(seq(minTemp, maxTemp));

		//
		var field_row  = document.getElementById("guessRow");
		var label_row  = document.getElementById("tempRow");
		var chance_row = document.getElementById("chanceRow");

		//
		var step = 0;
		for (temp = minTemp; temp <= maxTemp; ++temp){
			
			step += 1;

			var new_field   = field_row.insertCell(step);
			var new_label   = label_row.insertCell(step);
			var new_chance  = chance_row.insertCell(step);

			new_field.innerHTML  = `<input name="prob${temp}" id="id_prob${temp}" type="number" value="0" min="0" max="100" >`; // class="form-control form-control-sm"
			new_label.innerHTML  = `${temp}°C`;
			new_chance.innerHTML = `<div id="chance2win${temp}"></div>`;
		}

	}

		// calc chances to win and plot them accordingly
	function calcChance2win(){

		//
		var minTemp = parseInt(document.getElementById("id_minTemp").value);
		var maxTemp = parseInt(document.getElementById("id_maxTemp").value);
		var temps = Array.from(seq(minTemp, maxTemp));

		var losses  = Array(temps.length).fill(0);
		var gains   = Array(temps.length).fill(0);
		var inputs  = Array(temps.length).fill(0);
		var loss;
		var gain;
		var input;
		var guess;

		var viz_tab = document.getElementById("viz_tab");


		// get all the probabilities assigned
		for (var i = minTemp; i <= maxTemp; ++i){
			input = parseInt(document.getElementById("id_prob".concat("", i)).value);
			input = input || 0;
			inputs[i - minTemp] = input;
		}

		for (var winningTempIndex = 0; winningTempIndex < temps.length; ++winningTempIndex){
			
			// get guesses and define losses
			for (var enteredTemp = minTemp; enteredTemp <= maxTemp; ++enteredTemp){
				
				guess = document.getElementById("id_prob".concat("", enteredTemp)).value / 100;
				guess = guess || 0;

				if (enteredTemp == temps[winningTempIndex]) {
					loss = weight*(1-guess)**2;
				} else {
					loss = weight*guess**2;
				}

				losses[winningTempIndex] += loss;
			}

			// calculate winningprobabilities
			var gain = 1 - 1 * losses[winningTempIndex];
			if (gain >= 0) {
				gains[winningTempIndex] = Math.round(((gain*100) + Number.EPSILON) * 100) / 100;
			} else {
				gains[winningTempIndex] = 0;
			}
		}

		// write winning probabilities into table
		for (var t = minTemp; t <= maxTemp; ++t) {
			chance2win = gains[t-minTemp]
			document.getElementById("chance2win".concat(t)).innerHTML = chance2win + "%";
		}

		// make viz_tab visible
		viz_tab.className = "nav-link";


		// make viz
		var chart = Highcharts.chart("container", {
			exporting: {
				enabled: false
			},
	        chart: {
	            type: 'column'
	        },
	        title: {
	            text: 'Ihre Wahrscheinlichkeitsverteilung'
	        },
	        subtitle: {
	            text: ''
	        },
	        xAxis: {
	            categories: temps.map(i => i + "°C")// temps
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
	            name: 'Ihre Schätzung',
	            data: inputs,
	            showInLegend: false,
	            visible: false
	            },
	            {
	            name: "Gewinnchance",
	            data: gains,
	            visible: true,
	            showInLegend: false
	        	}
	    	]
		});


	}

// ---------------------------------------------------------------------------------------------
// Veranschaulichung Tab
	function chanceViz(){



		
	}
	

	





// ---------------------------------------------------------------------------------------------

// General stuff

	// vars from python
	let weight  = js_vars.weight;

	// get seq() function 
	function* seq( start, end, step = 1 ){
	  if( end === undefined ) [end, start] = [start, 0];
	  for( let n = start; n <= end; n += step ) yield n;
	}














