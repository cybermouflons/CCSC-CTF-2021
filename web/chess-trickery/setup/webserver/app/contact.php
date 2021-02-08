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
			<div class="bannerleftContact">
				<h1>
					Contact Us
				</h1>
				<p id="text">
					Please use the following form to get in touch.
					<br><br>
					If you spot a bug in our website, please let us know by filling the <b>URL</b> field. Sportmanship matters!
				</p>

				<form action="/submit-message.php" method="POST">
				  <fieldset>
					<?php
					if (isset($_GET["status"]))
					{
					  if ($_GET["status"] === "success") {
						echo "<h4 style='text-align:center; color:green;'>Message submitted successfully. We will check your message as soon as possible.</h4>";
					  }
					  else if ($_GET["status"] === "failRequired") {
						echo "<h4 style='text-align:center; color:red;'>Please fill all the required fields and resubmit the form.</h4>";
					  }
					  else if ($_GET["status"] === "fail") {
						echo "<h4 style='text-align:center; color:red;'>Please provide a valid URL. We need to know where the bug is in order to fix it.</h4>";
					  }
					  else if ($_GET["status"] === "failExternal") {
						echo "<h4 style='text-align:center; color:red;'>External domain names / hostnames are not allowed.</h4>";
					  }
					}
					?>
						<div class="form-group">
							<label for="name">Name <span style="color:red">*</span></label><br>
							<input type="text" id="id" name="name" class="form-control">
						</div>
						<div class="form-group">
							<label for="email">Email <span style="color:red">*</span></label><br>
							<input type="text" id="id" name="email" class="form-control">
						</div>
						<div class="form-group">
							<label for="subject">Subject <span style="color:red">*</span></label><br>
							<input type="text" id="id" name="subject" class="form-control">
						</div>
						<div class="form-group">
							<label for="link">URL</label><br>
							<input type="text" id="id" name="link" class="form-control">
						</div>
						<div class="form-group">
							<br>
							<label for="message">Message <span style="color:red">*</span></label><br>
							<div class="controls">
								<textarea id="message" name="message" rows="4" cols="50"></textarea>
							</div>
						</div>
						<br>
						<span style="color:red">*</span> indicates that the field is required.

						<div class="form-actions">
							<br>
							<input type="submit" value="Submit" class="btn btn-primary">
						</div>
					</fieldset>
				</form>
			</div>

		</div>

		<div class="contentafter" id="contentafter1"></div>

	</body>

	<script src="js/script.js"></script>
</html>
