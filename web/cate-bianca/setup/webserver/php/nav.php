<div class="nav">
  <ul>
	<li>
	  <a href="/index.php">Home</a>
	</li>
	<?php
	if (isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true) {
	  echo "<li><a href='/account.php'>Account</a></li>";
	  echo "<li><a href='/logout.php'>Logout</a></li>";
	}
	else {
	  echo "<li><a href='/login.php'>Login</a></li>";
	  echo "<li><a href='/register.php'>Register</a></li>";
	}
	?>
  </ul>
</div>
