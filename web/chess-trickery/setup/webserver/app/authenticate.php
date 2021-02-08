<?php
ini_set("session.cookie_httponly", True);
include "../php/config.php";
$con = new SQLite3($database_file);
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST'){
	if (isset($_POST["username"]) && isset($_POST["password"]))
	{
		$username = $_POST["username"];
		$password = $_POST["password"];

		error_log("Username: " . $username . " Password: " . $password);

		$query = $con->prepare("SELECT username, password FROM users WHERE username=:username and password=:password");
		$query->bindParam(':username', $username);
		$query->bindParam(':password', $password);
		$result = $query->execute();
		$row = $result->fetchArray(SQLITE3_ASSOC);
		if ($row){
			$_SESSION["loggedin"] = true;
			header('Location: /account.php');
			die();
    	}
		else {
        	header('Location: /login.php?error=wrong');
			die();
    	}

		$result->finalize();
	}
}
?>
