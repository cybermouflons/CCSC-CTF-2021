<div class="nav">
	<ul>
		<li>
			<a href="/index.php">Home</a>
		</li>
		<li>
			<a href="/about.php">About</a>
		</li>
		<li>
			<a href="/contact.php">Contact</a>
		</li>
		<?php
		if (isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true) {
			echo "<li><a href='/account.php'>Account</a></li>";
			echo "<li><a href='/logout.php'>Logout</a></li>";
		}
		else {
			echo "<li><a href='/login.php'>Login</a></li>";
		}
		?>
	</ul>
</div>
