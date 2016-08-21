<?php
$q = "";
if (isset($_POST['submit'])) {
	$first_name = $_POST['FirstName'];
	$last_name = $_POST['LastName'];
	$email_address = $_POST['EmailAddress'];
	$comments = $_POST['comments'];
	$fp = fopen("formdata.txt", "a");
	$savestring = $first_name . ", " . $last_name . ", " . $email_address .  ", " . $comments . "\n";
	fwrite($fp, $savestring);
	fclose($fp);
	$q = 'The message was sent successfully.';
}
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Home Page">
    <meta name="author" content="Dan Pezzin">
    <link rel="icon" href="../../favicon.ico">

    <title>Dan Pezzin - Contact</title>

	<!-- MY CSS -->
	<link href="/styles/site.css" rel="stylesheet" type="text/css" />
    <link href="/styles/footer.css" rel="stylesheet" type="text/css" />
	<link href="/styles/mobile.css" rel="stylesheet" type="text/css" />
    <link href="/styles/print.css" media="print" rel="stylesheet" type="text/css" />
	<link href="/styles/pages/contact.css" rel="stylesheet" type="text/css" />
    <!-- Bootstrap core CSS -->
    <link href="styles/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap theme -->
    <link href="styles/css/bootstrap-theme.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="theme.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="scripts/bootstrap/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body role="document">

	<!-- Fixed navbar -->
	<div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
	  <div class="container">
		<header class="navbar-header">
		  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
			<span class="sr-only">Toggle navigation</span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
		  </button>
		  <a class="navbar-brand" href="index.html">Dan Pezzin</a>
		</header>
		<nav class="navbar-collapse collapse">		  
		  <ul class="nav navbar-nav">
            <li class="dropdown">
              <a href="index.html" class="dropdown-toggle" data-toggle="dropdown">Networks<span class="caret"></span></a>
              <ul class="dropdown-menu" role="menu">
                <li><a href="http://www.linkedin.com/pub/daniel-pezzin/99/766/734">Linkedin</a></li>
                <li><a href="https://www.facebook.com/dan.pezzin">Facebook</a></li>
                <li><a href="http://open.spotify.com/user/dpezzin">Spotify</a></li>
                <li><a href="https://twitter.com/LieutenantDDan">Twitter</a></li>
                <li><a href="http://vimeo.com/user11714677">Vimeo</a></li>
              </ul>
            </li>
			<li><a href="about.html">About</a></li>
			<li><a href="resources2.html">Resources</a></li>
			<li class="active"><a href="contact.php">Contact</a></li>
		  </ul>
		</nav><!--/.nav-collapse -->
	  </div>
	</div>

	<div class="container theme-showcase" role="main">
			<div class="wrapper">
			<br>
				<section class="feedback">
					<h1>Say Hello</h1>
					<div>
					<?php
						if ($q !== "") {
						echo $q;
					}
					?>
					</div>
					<br>
					<form id=form1 method="post">
                        <div>
							<table>
								<tr>
									<td>
										<label for="first-name">First name <span class="red">*</span></label>
									</td>
								</tr>
								<tr>
									<td>
										<input type="text" id="FirstName" name="FirstName" required="required" autofocus="autofocus"/>
									</td>
								</tr>
								<tr>
									<td>
										<label for="last-name">Last name <span class="red">*</span></label>
									</td>
								</tr>
								<tr>
									<td>
										<input type="text" id="LastName" name="LastName" required="required"/>
									</td>
								</tr>
								<tr>
									<td>
										<label for="email-address">Email address <span class="red">*</span></label>
									</td>
								</tr>
								<tr>
									<td>
										<input type="email" id="EmailAddress" name="EmailAddress" required="required"/>
									</td>
								</tr>
								<tr>
									<td>
										<label>Your message <span class="red">*</span></label>
									</td>
								</tr>
								<tr>
									<td>
										<textarea name="comments" cols="30" rows="5" required="required"></textarea>
									</td>
								</tr>
								<tr>
									<td>
									<br>
										<button type="submit" name="submit" class="btn btn-lg btn-primary">Send</button>
									</td>
								</tr>
							</table>
						</div>
                    </form>
				</section>	
				<br>
				<br>
				<br>
				<br>
				<br>
				<br>
				<br>
				<footer class="page-footer">
					<div class="container">
						<p>
							&#169; 2014 Dan Pezzin
						</p>
					</div>
				</footer>
			</div>
		</div>	
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="scripts/bootstrap/bootstrap.min.js"></script>
    <script src="scripts/bootstrap/docs.min.js"></script>
	<script src="/scripts/jquery.min.js" type="text/javascript"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="scripts/bootstrap/ie10-viewport-bug-workaround.js"></script>
  
  <!--
        <script src="/scripts/pages/contact.js" type="text/javascript"></script>
  -->
  
  </body>
</html>