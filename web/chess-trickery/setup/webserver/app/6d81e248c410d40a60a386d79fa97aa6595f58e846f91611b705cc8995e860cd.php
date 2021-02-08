<?php
# start the session
session_start();
include "../php/config.php";

if ($_SESSION["loggedin"] !== true) {
	header('Location: /login.php');
	die();
}

$con = new SQLite3($database_file);

$query = $con->prepare("SELECT link FROM messages");
$result = $query->execute();
$rows = 0;

while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
	$rows += 1;
	$link = $row['link'];

	$arr = array ('link'=>$link);
	header('Content-type: application/json');
	echo json_encode($arr);
}

$result->finalize();
?>
