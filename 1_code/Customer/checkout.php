<?php
// start session
session_start();

   

 
// connect to database
include 'config/database.php';
 
// include objects
include_once "objects/product.php";
include_once "objects/product_image.php";
 
// get database connection
$database = new Database();
$db = $database->getConnection();
$memory_db = new PDO('sqlite:/xampp/htdocs/php-shopping-cart-using-sessions-level-1/thing.db');
    // Set errormode to exceptions
    $memory_db->setAttribute(PDO::ATTR_ERRMODE, 
                              PDO::ERRMODE_EXCEPTION);
							  
 // $memory_db->exec("CREATE TABLE messages (
                  //    id INTEGER PRIMARY KEY, 
                    //  quan INTEGER )");

 
// initialize objects
$product = new Product($db);
$product_image = new ProductImage($db);
$conn= mysqli_connect("localhost","root","","shop_cart_sessions_1");
if (!$conn){
	die("Connection lost".mysqli_connect_error());
}

 
// set page title
$page_title="Checkout";
 
// include page header html
include 'layout_header.php';

 
if(count($_SESSION['cart'])>0){
 
    // get the product ids
    $ids = array();
    foreach($_SESSION['cart'] as $id=>$value){
        array_push($ids, $id);
		$it=1;
		$quantity=$_SESSION['cart'][$id]['quantity'];
		//echo"<script> alert({$id}) </script>";
		$sql="INSERT INTO things (es,quan)
	VALUES ('$id','$quantity')";
	$insert = "INSERT INTO items (ids,quan) 
                VALUES (0'$id','$quantity')";
	$result=mysqli_query($conn,$sql);
    }
 
    $stmt=$product->readByIds($ids);

 
    $total=0;
    $item_count=0;
 
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)){
        extract($row);
 
        $quantity=$_SESSION['cart'][$id]['quantity'];
        $sub_total=$price*$quantity;
 
       // echo "<div class='product-id' style='display:none;'>{$id}</div>";
        //echo "<div class='product-name'>{$name}</div>";
 
        // =================
        echo "<div class='cart-row'>";
            echo "<div class='col-md-8'>";
 
                echo "<div class='product-name m-b-10px'><h4>{$name}</h4></div>";
                echo $quantity>1 ? "<div>{$quantity} items</div>" : "<div>{$quantity} item</div>";
 
            echo "</div>";
 
            echo "<div class='col-md-4'>";
                echo "<h4>&#36;" . number_format($price, 2, '.', ',') . "</h4>";
            echo "</div>";
        echo "</div>";
        // =================
 
        $item_count += $quantity;
        $total+=$sub_total;
    }
 
    // echo "<div class='col-md-8'></div>";
    echo "<div class='col-md-12 text-align-center'>";
        echo "<div class='cart-row'>";
            if($item_count>1){
                echo "<h4 class='m-b-10px'>Total ({$item_count} items)</h4>";
            }else{
                echo "<h4 class='m-b-10px'>Total ({$item_count} item)</h4>";
            }
            echo "<h4>&#36;" . number_format($total, 2, '.', ',') . "</h4>";
           // echo "<a href='place_order.php' class='btn btn-lg btn-success m-b-20px'>";
                echo "<span class='glyphicon glyphicon-shopping-cart'></span>";
            echo "</a>";
        echo "</div>";
    echo "</div>";
 
}
 
else{
    echo "<div class='col-md-12'>";
        echo "<div class='alert alert-danger'>";
            echo "No products found in your cart!";
			
        echo "</div>";
    echo "</div>";
}

include 'layout_footer.php';
?>
<style>
.wrapper {
    text-align: center;
}

.button {
    position: absolute;
    top: 50%;
}</style>
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick" >
<input type="hidden" name="hosted_button_id" value="NRL77R92MH5AL" align="center">
<table>
<tr><td><input type="hidden" name="on0" value="Add Tips">Add Tips</td></tr><tr><td><select name="os0">
	<option value="Without Tips">Without Tips $42.00 USD</option>
	<option value="With 10% tips">With 10% tips $46.20 USD</option>
	<option value="With 20% tip">With 20% tip $50.40 USD</option>
</select> </td></tr>
</table>
<input type="hidden" name="currency_code" value="USD">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynowCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>


