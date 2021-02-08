<?php
include "../php/config.php";
$con = new SQLite3($database_file);

if (isset($_POST["name"]) && !empty($_POST["name"]) && isset($_POST["email"]) && !empty($_POST["email"]) && isset($_POST["subject"]) && !empty($_POST["subject"]) && isset($_POST["message"]) && !empty($_POST["message"]))
{
	if (isset($_POST["link"]) && !empty($_POST["link"])) {
		$link = $_POST["link"];

		if (filter_var($link, FILTER_VALIDATE_URL) && substr($link, 0, 4 ) === "http") {
            $domain = parse_url($link, PHP_URL_HOST);

            # check if user supplied an external domain and quit if true
            if ($domain !== $proxy_ip)
            {
                header('Location: /contact.php?status=failExternal');
                die();
            }
            
            $query = $con->prepare("UPDATE messages SET link=:link WHERE id = 1");
			$query->bindParam(":link", $link, SQLITE3_TEXT);

			$result = $query->execute();

			$result->finalize();

			header('Location: /contact.php?status=success');
			die();
		} else {
			header('Location: /contact.php?status=fail');
			die();
		}
	} else {
		header('Location: /contact.php?status=success');
		die();
	}
} else {
	header('Location: /contact.php?status=failRequired');
	die();
}
?>
