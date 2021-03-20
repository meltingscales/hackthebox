<?php
include("db.php");
if($_COOKIE["user"]==="34322" || $_COOKIE["user"]==="86575")
{
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Admin Panel</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel='stylesheet' href='/css/bootstrap.min.css'>
<link rel='stylesheet' href='/css/ionicons.min.css'>
<style>
.container {
  max-width: 960px;
}
.navbar-survival101 {
  background-color:#2B6DAD;
}
/* .navbar-survival101 .navbar-brand {
  margin-right: 2.15rem;
  padding: 3px 0 0 0;
  line-height: 36px;	
} */

.navbar-survival101 .navbar-brand img {
  vertical-align: baseline;
}

.navbar-expand-lg .navbar-nav .nav-link {
  color: #fff;
}

.search-box {
  position: relative;
  height: 34px;
}
.search-box input {
  border: 0;
  border-radius: 3px !important;
  padding-right: 28px;
  font-size: 15px;
}

.search-box .input-group-btn {
  position: absolute;
  right: 0;
  top: 0;
  z-index: 999;
}

.search-box .input-group-btn button {
  background-color: transparent;
  border: 0;
  padding: 4px 8px;
  color: rgba(0,0,0,.4);
  font-size: 20px;
}

.search-box .input-group-btn button:hover,
.search-box .input-group-btn button:active,
.search-box .input-group-btn button:focus {
  color: rgba(0,0,0,.4);
}

@media (min-width: 992px) {
  .navbar-expand-lg .navbar-nav .nav-link {
    padding-right: .7rem;
    padding-left: .7rem;
  }

.new {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width:30%;
}

table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 60%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
} 
  .search-box {
    width: 300px !important;
  }
}

.caroulsel {
  width: 100%;
  overflow: hidden;
  padding: 5px 0 5px 5px;
}

.caroulsel-wrap {
  white-space: nowrap;
  font-size: 0;
}

.caroulsel-wrap a {
  display: inline-block;
  width: 134px;
  height: 92px;
  background-color: silver;
  border: #ccc 1px solid;
  margin-right: 5px;
}
</style>
<script>
  window.console = window.console || function(t) {};
</script>
<script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
</script>
</head>
<body translate="no">
<nav class="navbar navbar-expand-lg navbar-dark navbar-survival101">
<div class="container">
<a class="navbar-brand" href="#">
MegaCorp Automotive
</a>
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="navbarColor02">
<ul class="navbar-nav mr-auto">
<li class="nav-item active">
<a class="nav-link" href="/cdn-cgi/login/admin.php?content=accounts&id=1">Account<span class="sr-only">(current)</span></a>
</li>
<li class="nav-item">
<a class="nav-link" href="/cdn-cgi/login/admin.php?content=branding&brandId=10">Branding</a>
</li>
<li class="nav-item">
<a class="nav-link" href="/cdn-cgi/login/admin.php?content=clients&orgId=1">Clients</a>
</li>
<li class="nav-item">
<a class="nav-link" href="/cdn-cgi/login/admin.php?content=uploads">Uploads</a></li>
<li class="nav-item">
<a class="nav-link" href="#">Logged in as Admin</a>
</li>
</ul>
<form class="form-inline">
</span>
</div>
</form>
</div>
</div>
</nav>
<br /><br /><center><h1>Repair Management System</h1><br /><br />
<?php
if($_GET["content"]==="branding" && $_GET["brandId"]!="")
{
	$stmt=$conn->prepare("select model,price from branding where id=?");
	$stmt->bind_param('i',$_GET["brandId"]);
	$stmt->execute();
	$stmt=$stmt->get_result();
	$stmt=$stmt->fetch_assoc();
	$model=$stmt["model"];
	$price=$stmt["price"];
	echo '<table><tr><th>Brand ID</th><th>Model</th><th>Price</th></tr><tr><td>'.$_GET["brandId"].'<td>'.$model.'</td><td>'.$price.'</td></tr></table';
}
	else
	{
		if($_GET["content"]==="clients"&&$_GET["orgId"]!="")
		{
			$stmt=$conn->prepare("select name,email from clients where id=?");
			$stmt->bind_param('i',$_GET["orgId"]);
			$stmt->execute();
			$stmt=$stmt->get_result();
			$stmt=$stmt->fetch_assoc();
			$name=$stmt["name"];
			$email=$stmt["email"];
			echo '<table><tr><th>Client ID</th><th>Name</th><th>Email</th></tr><tr><td>'.$_GET["orgId"].'</td><td>'.$name.'</td><td>'.$email.'</td></tr></table';
		}
		else
		{
			if($_GET["content"]==="accounts"&&$_GET["id"]!="")
			{
	                        $stmt=$conn->prepare("select access,name,email from accounts where id=?");
	                        $stmt->bind_param('i',$_GET["id"]);
	                        $stmt->execute();
	                        $stmt=$stmt->get_result();
	                        $stmt=$stmt->fetch_assoc();
				$id=$stmt["access"];
	                        $name=$stmt["name"];
	                        $email=$stmt["email"];
	                        echo '<table><tr><th>Access ID</th><th>Name</th><th>Email</th></tr><tr><td>'.$id.'</td><td>'.$name.'</td><td>'.$email.'</td></tr></table';
			}
			else
			{
				if($_GET["content"]==="uploads")
				{
					if($_COOKIE["user"]==="34322")
					{
						echo 'This action require super admin rights.';
					}
					else
					{
						if($_GET["action"]==="upload")
						{
							$target_dir = "/var/www/html/uploads/";
							$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
							if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
							        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
							    } else {
									echo "Sorry, there was an error uploading your file.";
    								}				}else{	?>

<h2>Branding Image Uploads</h2><br /><form action="/cdn-cgi/login/admin.php?content=uploads&action=upload" method="POST" enctype="multipart/form-data">
<table class="new"><tr><td>Brand Name</td><td><input name="name" type="text"/></td></tr><tr><td colspan="2"><input type="file" name="fileToUpload"/><input type="submit" value="Upload"/></td></tr></table></form>
<?php	} }

				}
				else {
					?><img src="/images/3.jpg"/>
				<?php }
			}
		}
	}?>
<script src='/js/jquery.min.js'></script>
<script src='/js/bootstrap.min.js'></script>
</body>
</html>
<?php }
else
{
	header('Location: /cdn-cgi/login/index.php');
}
?>
