<?php
include "../php/config.php";

session_start();

if (isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true) {
  header('Location: /account.php');
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

	<div class="nav">
	  <ul>
		<li>
		  <a href="/index.php">Home</a>
		</li>
		<li>
		  <a href="/login.php">Login</a>
		</li>
		<li>
		  <a href="/register.php">Register</a>
		</li>
	  </ul>
	</div>

	<div class="content">

	  <div class="bannerleftAbout">
		<h1>
		  Register
		</h1>

		<form action="/register_user.php" method="POST">
		  <fieldset>
			<?php
			if (isset($_GET["status"]))
			{
			  if ($_GET["status"] === "exists") {
				echo "<h4 style='text-align:center; color:red;'>Username is taken &macr;\_(&#12484;)_/&macr;</h4>";
			  }
			  else if ($_GET["status"] === "success") {
				echo "<h4 style='text-align:center; color: green;'>User registered successfully.</h4>";
			  }
			}
			?>
			<div class="form-group">
			  <label for="username">Username</label><br>
			  <input type="text" id="username" name="username" maxlength="20" class="form-control">
			</div>
			<div class="form-group">
			  <label for="password">Password:</label><br>
			  <div class="controls">
				<input type="password" id="password" name="password" maxlength="20" class="form-control">
			  </div>
			</div>

			<div class="form-actions">
			  <input type="submit" value="Register" class="btn btn-primary">
			</div>
		  </fieldset>
		</form>
	  </div>

	</div>

	<div class="contentafter" id="contentafter1"></div>

  </body>

  <script src="js/script.js"></script>
</html>
