<?php
// start session
session_start();
 
// get the product id
$id = isset($_GET['id']) ? $_GET['id'] : "";
$name = isset($_GET['name']) ? $_GET['name'] : "";
 
// remove the item from the array
unset($_SESSION['cart'][$id]);
 
// redirect to product list and tell the user it was added to cart
header('Location: cart.php?action=removed&id=' . $id);
?>