var selected_languages = new Array();
var sentiment_totals = new Array();

$('#submit-form-button').on('click', my_function);

// Load the Visualization API and the piechart package.
google.load('visualization', '1.0', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
//google.setOnLoadCallback(drawChart);
			
function my_function()
{
	// Clear the selected_languages array first
	selected_languages.length = 0;
	
	$("input:checkbox[name=language]:checked").each(function()
	{
		selected_languages.push({
									file_name: $(this).val(),
									display_name: $("label[for='" + $(this).attr('id') + "']").text()
								});
	});
	
	for (var i = 0; i < selected_languages.length ; i++)
	{
		get_sentiment_totals(selected_languages[i].file_name, "2011");
		get_sentiment_totals(selected_languages[i].file_name, "2012");
		get_sentiment_totals(selected_languages[i].file_name, "2013");
	}
	
	drawChart();
}

function get_sentiment_totals(tag, year) {
	tag_string = tag + "_" + year;
	$.ajax({ url: 'happiest_programmers.php',
        data: { tag_filename: 'data/' + tag_string + '.json' },
        type: 'post',
		async: false,
        success: function(output) {
					sentiment_totals[tag_string] = output;
				}
	});
}

// Callback that creates and populates a data table, instantiates chart, passes in the data and draws it.
function drawChart() {
	var titles = new Array("Year");
	var sentiment_totals_2011 = new Array("2011");
	var sentiment_totals_2012 = new Array("2012");
	var sentiment_totals_2013 = new Array("2013");
	
	for (var i = 0; i < selected_languages.length; i++)
	{
		titles.push(selected_languages[i].display_name);
		sentiment_totals_2011.push(parseInt(sentiment_totals[selected_languages[i].file_name + "_2011"]));
		sentiment_totals_2012.push(parseInt(sentiment_totals[selected_languages[i].file_name + "_2012"]));
		sentiment_totals_2013.push(parseInt(sentiment_totals[selected_languages[i].file_name + "_2013"]));
	}
	
	// Create the data table.
	var data = google.visualization.arrayToDataTable([
			/* ['Year',	'Java',				'C++'],
			['2011',  parseInt(sentiment_totals["java_2011"]), parseInt(sentiment_totals["cpp_2011"])],
			['2012',  parseInt(sentiment_totals["java_2012"]), parseInt(sentiment_totals["cpp_2012"])],
			['2013',  parseInt(sentiment_totals["java_2013"]), parseInt(sentiment_totals["cpp_2013"])] */
			titles,
			sentiment_totals_2011,
			sentiment_totals_2012,
			sentiment_totals_2013
        ]);

	var options = {
		title: 'Programmer Happiness',
		hAxis: {title: 'Year'}
	};

	// Instantiate and draw our chart, passing in some options.
	var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
	chart.draw(data, options);
}