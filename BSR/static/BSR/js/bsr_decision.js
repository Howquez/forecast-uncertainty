console.log("bsr_decision_js is running")


// ---------------------------------------------------------------------------------------------
// Schritt 1 Tab

// The validation function shall be called in Schritt 1 to check if inputs are eligible
// if yes, allow the respondent to proceed. if not, prohibit that and warn her.
	function validation(){
		// get field values
		var minTemp = parseInt(document.getElementById("id_minTemp").value);
		var maxTemp = parseInt(document.getElementById("id_maxTemp").value);
		// get fields
		var minField = document.getElementById("id_minTemp");
		var maxField = document.getElementById("id_maxTemp");

		// force inputs to be ints
		minField.value = minTemp;
		maxField.value = maxTemp;

		// the error condition
		if (maxTemp < minTemp) {
			maxmin_alert.style = "";
			// alert("Die höchste Temperatur, die sie für möglich halten, muss höher sein, als die niedrigste Temperatur, die Sie für möglich halten.");
			choice_tab.className = "nav-link disabled"; // disable Schritt 2 Tab
			return false;
		}

		// warning condition if no values are entered
		if (maxTemp == NaN || minTemp == NaN) {
			nan_alert.style = "";
			// alert("Bitte tragen Sie ganze Zahlenwerte ein.");
			choice_tab.className = "nav-link disabled";
			return false;
		}

		// everything is working as it should condition
		if (minTemp <= maxTemp){
			minField.setAttribute("readonly", ""); 		// block forms in Schritt 1
			maxField.setAttribute("readonly", ""); 		// block forms in Schritt 1
			choice_tab.className = "nav-link";			// enable Schritt 2 Tab
			limits_validation.style = "display:none";	// hide validation button and..
			limits_revision.style = "";					// ..display revision button
			createTable();								// call function to create Table for Schritt 2
			createCols();								// call function to fill Table for Schritt 2
			createHiddenFields();						// call function to create&hide all forms not included in the table
			// hide alerts
			maxmin_alert.style = "display:none";
			nan_alert.style = "display:none";
		}
	}

// The revision function shall be called in Schritt 2 to change one's inputs
	function revision(){

		// hide and unhide revision and validation button
		limits_validation.style = "";
		limits_revision.style = "display:none";

		// unblock forms from Schritt 1
		minField.removeAttribute("readonly");
		maxField.removeAttribute("readonly");

		// daisble Schritt 2 and Viz Tab
		choice_tab.className = "nav-link disabled";
		viz_tab.className = "nav-link disabled";

		// erase the table in Schritt 2 Tab
		removeTable()

		// make submit button invisible
		submitButton.style = "display:none";
	}

// ---------------------------------------------------------------------------------------------
// Schritt 2 Tab


// the following two functions create or remove a table, that is later to be filled with createCols()
	function createTable(){
		//create table with three rows and row ids
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

		// identify div that will be filled with div_content, which is an initially empty string that will be 
		// concatenated within two for loops
		var div = document.getElementById("hidden_fields");
		var div_content = ""

		// create hidden fields/forms for temps lower than mintemp
		for (var i = lower_limit; i < minTemp; ++i){
			var i_string = String(i).replace("-", "minus");
			console.log(i_string)
			div_content += `<input name="prob${i_string}" id="id_prob${i_string}" type="hidden" value="0" min="0" max="0" readonly>`
		}

		// create hidden fields/forms for temps higher than maxtemp
		for (var j = maxTemp + 1; j <= upper_limit; ++j){
			var j_string = String(j).replace("-", "minus");
			div_content += `<input name="prob${j_string}" id="id_prob${j_string}" type="hidden" value="0" min="0" max="0" readonly>`
		}

		div.innerHTML = div_content;

	}

// create Cols loops throug the available temperaturs between minTemp and maxTemp and creates form fields 
// with labels and a prelimenarily empty chance2win. One column for each temperature.
	function createCols(){

		// given the table from createTable(), we'll add maxTemp-minTemp columns
		var minTemp = parseInt(document.getElementById("id_minTemp").value);
		var maxTemp = parseInt(document.getElementById("id_maxTemp").value);
		var temps = Array.from(seq(minTemp, maxTemp));

		// with the given three rows
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

			var temp_string = String(temp).replace("-", "minus");
			console.log(temp_string)

			new_field.innerHTML  = `<input name="prob${temp_string}" id="id_prob${temp_string}" class="form-control" type="number" value="0" min="0" max="100" >`; // class="form-control form-control-sm"
			new_label.innerHTML  = `${temp}°C`;
			new_chance.innerHTML = `<div id="chance2win${temp}"></div>`;
		}

	}

// long function to calculate chances to win and plot them accordingly
	function calcChance2win(){

		// get all the variables needed
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

		// get all the probabilities assigned within the (unhidden) forms/fields
		for (var i = minTemp; i <= maxTemp; ++i){
			var i_string = String(i).replace("-", "minus");
			input = parseInt(document.getElementById("id_prob".concat("", i_string)).value);
			input = input || 0;
			inputs[i - minTemp] = input;
		};

		// sum inputs and trigger alerts if they exceed or undercut 100%
		var sum = inputs.reduce(function(a,b){
			return a+b;
		}, 0)

		if (sum < 100){
			undercut_alert.style = "";
			exceed_alert.style = "display:none";
		} else if (sum > 100){
			undercut_alert.style = "display:none";
			exceed_alert.style = "";
			return false;
		} else {
			exceed_alert.style = "display:none";
			undercut_alert.style = "display:none";

		}


		// retrieve these probabilities (guesses) once more to define losses and chances to win
		for (var winningTempIndex = 0; winningTempIndex < temps.length; ++winningTempIndex){
			
			// get guesses and define losses
			for (var enteredTemp = minTemp; enteredTemp <= maxTemp; ++enteredTemp){
				
				var enteredTemp_string = String(enteredTemp).replace("-", "minus");
				guess = document.getElementById("id_prob".concat("", enteredTemp_string)).value / 100;
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
			var t_string = String(t).replace("-", "minus");
			document.getElementById("chance2win".concat(t)).innerHTML = chance2win + "%";
		}

		
		submitButton.style = "";		// make submit button visible
		viz_tab.className = "nav-link";	// make viz_tab visible


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

	

	





// ---------------------------------------------------------------------------------------------
// General stuff

	// global vars
	// initiate fields
	var minField = document.getElementById("id_minTemp");
	var maxField = document.getElementById("id_maxTemp");
	// initiate tabs
	var viz_tab = document.getElementById("viz_tab");
	var choice_tab = document.getElementById("choice_tab");
	// initiate buttons
	var limits_validation = document.getElementById("limits_validation");
	var limits_revision = document.getElementById("limits_revision");
	var submitButton = document.getElementById("submit_button");
	// initiate alerts
	var maxmin_alert = document.getElementById("maxminAlert");
	var nan_alert = document.getElementById("nanAlert");
	var exceed_alert = document.getElementById("exceedAlert");
	var undercut_alert = document.getElementById("undercutAlert");

	// initiate vars from python
	let weight  = js_vars.weight;
	let lower_limit = js_vars.lower_limit;
	let upper_limit = js_vars.upper_limit;

	// define seq() function as in R
	function* seq( start, end, step = 1 ){
	  if( end === undefined ) [end, start] = [start, 0];
	  for( let n = start; n <= end; n += step ) yield n;
	}














