<?php
// start session
session_start();
 
// remove items from the cart
session_destroy();
 
// set page title
$page_title="Thank You!";
 
// include page header HTML
include_once 'layout_header.php';
 
echo "<div class='col-md-12'>";
 
    // tell the user order has been placed
    echo "<div class='alert alert-success'>";
        echo "<strong>Your order has been placed!</strong> Thank you very much!";
    echo "</div>";
 
echo "</div>";
 
// include page footer HTML
include_once 'layout_footer.php';
?>
