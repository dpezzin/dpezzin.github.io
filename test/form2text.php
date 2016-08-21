<?php
$first_name = $_POST['FirstName'];
$last_name = $_POST['LastName'];
$email_address = $_POST['EmailAddress'];
$comments = $_POST['comments'];
$fp = fopen("formdata.txt", "a");
$savestring = $first_name . ", " . $last_name . ", " . $email_address .  ", " . $comments . "\n";
fwrite($fp, $savestring);
fclose($fp);
echo "<h1>Your data has been saved in a text file!</h1>";
?>