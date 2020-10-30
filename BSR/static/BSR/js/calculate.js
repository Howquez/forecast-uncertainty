// Scope things?
// calculate();
console.log("engines running");
// get vars from python
    let minTemp = js_vars.minTemp;
	let maxTemp = js_vars.maxTemp;
	let weight  = js_vars.weight;

// constants
	const temps   = Array.from(range(minTemp, maxTemp));
	const next    = document.getElementById("BSR_next");

// get range() function 
function* range( start, end, step = 1 ){
  if( end === undefined ) [end, start] = [start, 0];
  for( let n = start; n <= end; n += step ) yield n;
}

function calculate() {

// initiate variables
    // var temps   = Array.from(range(minTemp, maxTemp));
	var inputs  = Array(temps.length).fill(0);
	var input;
	var loss;
	var losses  = Array(temps.length).fill(0);
	var gain;
	var gains   = losses;
	// var next    = document.getElementById("BSR_next");
	var sum;


// get all the probabilities assigned
	for (var i = minTemp; i <= maxTemp; ++i){
		input = parseInt(document.getElementById("id_prob".concat("", i)).value);
		input = input || 0;
		inputs[i - minTemp] = input;
	}
	console.log(inputs)

// display error/warning messages and change button's appearance
	// sum all inputs for conditions
	sum = inputs.reduce(function(a,b){
		return a+b;
	}, 0)

	// display error modal and less salient next button if  sum < 100
	if (sum < 100) {
		warningModal.style.display = "block";
		// $('#warningModal').modal('show');
		next.className  = "nexttab btn-outline-success btn";

	}

	// display eeor modal and hide next button if sum > 100
	if (sum > 100) {
		errorModal.style.display = "block";
		next.style  = "display:none"; // hide next button
		// alert("Die Summe der von Ihnen geschätzten Wahrscheinlichkeiten ist größer als 100%.")
		return false
	}

	// display next button after validation and only if sum of probabilities is less or equal to 100
	if (sum <= 100) {
		next.style  = "";
	}

	// make next button more salient if sum of probabilities is to 100
	if (sum == 100) {
		next.className  = "nexttab btn-success btn";
	}


// get inputs and define losses
	for (var winningTempIndex = 0; winningTempIndex < temps.length; ++winningTempIndex) {
		for (var enteredTemp = minTemp; enteredTemp <= maxTemp; ++enteredTemp){
			input = document.getElementById("id_prob".concat("", enteredTemp)).value / 100;
			input = input || 0;

			if (enteredTemp == temps[winningTempIndex]) {
				loss = weight*(1-input)**2;
			} else {
				loss = weight*input**2;
			}
			console.log("- - - - - - - - - - -")
			console.log("field: ".concat(enteredTemp));
			console.log("winning temperature is: ".concat(temps[winningTempIndex]));
			console.log("tempeature is:".concat(temps[winningTempIndex]));
			console.log("assigned probability:".concat(input));
			console.log("loss is:".concat(loss));
			losses[winningTempIndex] += loss;
		}

		// calculate winning probabilities
		var temp = 1 - 1 * losses[winningTempIndex];
		if (temp >= 0) {
			gains[winningTempIndex] = Math.round(((temp*100) + Number.EPSILON) * 100) / 100;
		} else {
			gains[winningTempIndex] = 0;
		}
		//console.log("________NEW LOOP_______");
	}
	//console.log(losses);


	// write winning probabilities into table
	for (var w = minTemp; w <= maxTemp; ++w) {
		gain = gains[w-minTemp]
		document.getElementById("winprob_".concat(w)).innerHTML = gain + "%";
	}


	console.log("gains: ".concat(gains))

// print for testing purposes
	//document.getElementById('total').innerHTML = 'You entered ' + inputs;
	console.log(inputs)

// Highcharts
	var chart = Highcharts.chart('container', {
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
                color: "#33b5eb" // "#3479F6"//'#1FE68E'
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

// next button's (dis)appearance
next.onmouseover = function() {
	var temps   = Array.from(range(minTemp, maxTemp));
	var inputs  = Array(temps.length).fill(0);
	var input;
	var sum;

	// get all the probabilities assigned
	for (var i = minTemp; i <= maxTemp; ++i){
		input = parseInt(document.getElementById("id_prob".concat("", i)).value);
		input = input || 0;
		inputs[i - minTemp] = input;
	}
	console.log("hover next button")

	for (var i = minTemp; i <= maxTemp; ++i){
		input = parseInt(document.getElementById("id_prob".concat("", i)).value);
		input = input || 0;
		inputs[i - minTemp] = input;
	}

	sum = inputs.reduce(function(a,b){
		return a+b;
	}, 0)

	if (sum > 100) {
		// next.setAttribute("disabled", "")
		next.style  = "display:none";
		console.log("hide next button")
	}
	// if (sum <= 100) {
	// 	next.style  = "";
	// }
}

// calculator button's text change
function change() {
    var elem = document.getElementById("calcButton");
    if (elem.value=="Gewinnwahrscheinlichkeit berechnen") elem.value = "Gewinnwahrscheinlichkeit erneut berechnen";
    else elem.value = "Gewinnwahrscheinlichkeit erneut berechnen";
}

function displayChart() {
  var disp = document.getElementById("container");
  disp.style.display = "block"
}


// show less show more
// function readMore() {
//   var dots = document.getElementById("dots");
//   var moreText = document.getElementById("more");
//   var btnText = document.getElementById("foldText");

//   if (dots.style.display === "none") {
//     dots.style.display = "inline";
//     btnText.innerHTML = "Instruktionen anzeigen"; 
//     moreText.style.display = "none";
//   } else {
//     dots.style.display = "none";
//     btnText.innerHTML = "Instruktionen ausblenden"; 
//     moreText.style.display = "inline";
//   }
// }

// replace missing inputs with 0
// function replace_NaN() {
// 	// get vars from python
//     let minTemp = js_vars.minTemp;
// 	let maxTemp = js_vars.maxTemp;
// // initiate variables
//     var temps   = Array.from(range(minTemp, maxTemp));
// 	var inputs  = Array(temps.length).fill(0);
// 	var input;
// // get all the probabilities assigned
// 	for (var i = minTemp; i <= maxTemp; ++i){
// 		inputs[i - minTemp] = parseInt(document.getElementById("id_prob".concat("", i)).value);
// 	}
// // get inputs and define losses
// 	for (var i = minTemp; i <= maxTemp; ++i){
// 		input = document.getElementById("id_prob".concat("", i)).value;
// 		// console.log(input)
// 		if (input == NaN) {
// 			document.getElementById("id_prob".concat("", i)).value = 0;
// 		}
// 	}

// }