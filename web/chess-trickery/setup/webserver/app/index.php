<?php
include "../php/config.php";

session_start();
?>

<!doctype html>
<HTML>
	<head>
		<title>Let's Play</title>
		<meta charset="UTF-8">
		<meta name="description" content="">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Lobster" />
		<link rel="stylesheet" href="css/style.css" type="text/css">
	</head>
	<body>

		<!-- Nav -->
		<?php include_once("../php/nav.php"); ?>

		<div class="content">

			<div class="bannerleft">
				<h1>
					When you see a good move, look for a better one.
				</h1>
				<p>- Emanuel Lasker</p>
			</div>

		</div>

		<div class="contentafter" id="contentafter1"></div>

	</body>

	<script src="js/script.js"></script>
</html>
