<?php
    include_once('pet.php');
    $cat = new Pet(); //Objects of a class are created using the 'new' keyword.
    $cat->id = 1;
    $cat->name = 'Sparky';
    $cat->race = 'cat';
    $cat->breed = 'tabby';
    $cat->gender = 'male';
    print_r($cat);

    echo "<br>";

    $dog = new Pet();
    $dog->set_Pet(2,'Kite', 'dog', 'husky','female',);
    print_r($dog);

    $cat->display();
    $dog->display();

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
</html>
