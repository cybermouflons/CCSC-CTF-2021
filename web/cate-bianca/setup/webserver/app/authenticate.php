<?php
ini_set("session.cookie_httponly", True);
include "../php/config.php";

try {
    $conn = new PDO("mysql:host=$db_address;dbname=db", $db_username, $db_password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    echo "Connection to the database failed." . $e->getMessage();
}

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST'){
	if (isset($_POST["username"]) && isset($_POST["password"]))
	{
		$username = $_POST["username"];
		$password = $_POST["password"];

		error_log("Username: " . $username . " Password: " . $password);

        $statement = $conn->prepare('SELECT username, password FROM users WHERE username = ? and password = ?');
        $statement->bindParam(1, $username, PDO::PARAM_STR);
        $statement->bindParam(2, $password, PDO::PARAM_STR);

		$statement->execute();
		$row = $statement->fetch();
		if ($row){
			$_SESSION["loggedin"] = true;
			$_SESSION["user"] = $username;
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
