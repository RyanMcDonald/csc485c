<!DOCTYPE html>

<html>

    <head>
	
        <link rel="stylesheet" type="text/css" href="css/index.css" />
		<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
        <title>CSC 485C - Term Project 1 by Ryan McDonald</title>
		
    </head>
	
    <body>
	
        <div id="input-container">
            <h1>CSC 485C - Term Project 1</h1>
			<div id="language-checkboxes">
				<input type="checkbox" id="java" name="language" value="java">
				<label for="java">Java</label>
				<input type="checkbox" id="cpp" name="language" value="cpp">
				<label for="cpp">C++</label>
				<input type="checkbox" id="cs" name="language" value="cs">
				<label for="cs">C#</label>
				<input type="checkbox" id="python" name="language" value="python">
				<label for="python">Python</label>
				<input type="checkbox" id="ruby" name="language" value="ruby">
				<label for="ruby">Ruby</label>
				<input type="checkbox" id="perl" name="language" value="perl">
				<label for="perl">Perl</label>
				<input type="checkbox" id="php" name="language" value="php">
				<label for="php">PHP</label>
			</div>
			
				<button id="submit-form-button" type="button">SHOW RESULTS</button>
		</div>
		
		<div id="chart_div"></div>
		
    </body>
	
	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
	<script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript" src="js/index.js"></script>
</html>
