<?php

// Parse the sentiment file and create a dictionary with all the words and their sentiment values
$sentiment_file = fopen("data/AFINN-111.txt", "r");

$sentiment_values = array();

$total_sentiment_sum = 0;

# Read one line at a time
while (($line = fgets($sentiment_file)) !== false) {
	$term = preg_split('/\t/', $line);
	$sentiment_values[$term[0]] = $term[1];
}

// get contents of a file into a string
$filename = $_POST['tag_filename'];
$handle = fopen($filename, "r");
$contents = fread($handle, filesize($filename));

$json = json_decode($contents);

foreach ($json->items as $question) {
	# This holds the sum of the sentiment for this particular question
	$question_sentiment_sum = 0;
	
	# Make the tweet text all lower case in case there are some words with capitals, which wouldn't match our dict keys
	$body = strtolower($question->body);
	
	$body_terms = explode(" ", $body);
	
	# TODO: Remove all the punctuation from the beginning/end of the terms
	
	foreach ($body_terms as $term) {
		if (array_key_exists($term, $sentiment_values)) {
			$question_sentiment_sum += $sentiment_values[$term];
		}
	}
	
	$total_sentiment_sum += $question_sentiment_sum;
}

echo $total_sentiment_sum;

fclose($handle);

?>