<?php
    session_start();
    error_reporting(0);
    $pwd = $_POST['password'];
    $encpwd = password_hash($_POST['password'], PASSWORD_DEFAULT);
    //echo $encpwd.'<br>';
    if(($_POST['username'] == 'admin') && (password_verify($_POST['password'],$encpwd))){
        $validation = true;
        $_SESSION['username'] = $_POST['username'];
    } else{
        $validation = false;
    }

    if($validation){
        echo 'Welcome '.$_POST['username'];
    } else{
        echo 'Invalid login';
    }
    echo '<br><a href="index.php">Return</a>';
?>