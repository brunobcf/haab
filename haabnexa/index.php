<!DOCTYPE html>
<!--
Design by Bruno Ferreira
-->
<html lang="en">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>HAAB - Nexa gateway</title>
		<meta name="keywords" content="" />
		<meta name="description" content="This is an invisible page" />
	</head>
	<body>
		<?php
		$com = $_GET['com'];
		$move = $_GET['move'];
		$cam = $_GET['cam'];
		$command = escapeshellcmd("python ./haabnexa.py -p 5697 -c {$com} -i {$_SERVER["REMOTE_ADDR"]};");
		$command_move = escapeshellcmd("python ./home_commander.py -p /dev/ttyACM0 -c {$move}");
		$command_cam = escapeshellcmd("python ./camcontrol.py -c {$cam}");
		$output = shell_exec($command);
		$output_move = shell_exec($command_move);
		#$out
		#echo $output;
		#echo $output_move;
		echo "Your IP is ";
		echo $_SERVER["REMOTE_ADDR"];
		?>
	</body>
</html>
