<?php
# start the session
session_start();
include "../php/config.php";

if ($_SESSION["loggedin"] !== true) {
	header('Location: /login.php');
	die();
}
?>

<!doctype html>
<HTML>
	<head>
	  <title>The memoirs of Cate Bianca</title>
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

			<div class="bannerleftAccount">
			  <h1 class="voila">
				Account
			  </h1>
			  <?php
			  if ($_SESSION["user"] === "admin") {
				echo "<span style='color: red;'>$FLAG</span>";
				echo '<br><br><br><iframe width="500px" height="350px" src="https://www.youtube.com/embed/VRm8WNlEvwk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
			  }
			  else {
				echo "<p>Welcome " . htmlEntities($_SESSION['user'], ENT_QUOTES);
				echo "<p>Noting to see here &macr;\_(&#12484;)_/&macr;</p>";
			  }
			  ?>
			</div>

		</div>

		<div class="contentafter" id="contentafter1"></div>

	</body>

	<script src="js/script.js"></script>
</html>
