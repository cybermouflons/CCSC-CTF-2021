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
        // Check if user exists
		$username = trim($_POST["username"]);
		$password = $_POST["password"];

        $statement = $conn->prepare('SELECT username FROM users WHERE username = ?');
        $statement->bindParam(1, $username, PDO::PARAM_STR);

		$statement->execute();
		$row = $statement->fetch();
		if ($row){
            header('Location: /register.php?status=exists');
			die();
    	}
		else {
            $statement= $conn->prepare('INSERT into users (username, password) VALUES (?,?)');
            $statement->execute([$username, $password]);
        	header('Location: /register.php?status=success');
			die();
    	}

		$result->finalize();
	}
}
?>
