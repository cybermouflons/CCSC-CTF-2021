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

			<div class="bannerleftAbout">
				<h1>
					About
				</h1>
				<p id="text">
					Our club gives its members the opportunity<br>
					to play against the best chess players in the world.<br><br>
					For this reason, <span style="color: red">ONLY</span> grandmasters can join our club.<br>
					If you believe you have the skills to join our club, <a href="contact.php">contact us</a>.
				</p>
			</div>

		</div>

		<div class="contentafter" id="contentafter1"></div>

	</body>

	<script src="js/script.js"></script>
</html>
