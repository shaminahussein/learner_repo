<?php
    session_start();
    error_reporting(0);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        if($_SESSION['username'] == 'admin'){
            echo 'Index for admin';
        } else{
            echo '
                    <form action="dashboard.php" method="post">
                        <input type="text" name="username" id="" placeholder="Enter Username">
                        <input type="password" name="password" id="" placeholder="Enter Password">
                        <input type="submit" value="Login">
                    </form>
            ';
        }
    ?>

</body>
</html>