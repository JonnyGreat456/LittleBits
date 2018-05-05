<!--This is the home page that connects all the Customer interface pages together-->
<?phpinclude 'layout_header.php';
 include 'navigation.php'; 
// start session
session_start();
// connect to database
include 'config/database.php';
 
// include objects
include_once "objects/product.php";
include_once "objects/product_image.php";?>
<html>
  
<!-- This Css code is for the buttons through out the pages, the colors chosen (red, orange and yellow) are proven to be appetizing. The buttons highlight when hoverd over and change color when clicked to provide feed back to the customers ordering-->
<style>
.button {
   border: 1px solid #0a3c59;
   background: #b36561;
   background: -webkit-gradient(linear, left top, left bottom, from(#b3160e), to(#b36561));
   background: -webkit-linear-gradient(top, #b3160e, #b36561);
   background: -moz-linear-gradient(top, #b3160e, #b36561);
   background: -ms-linear-gradient(top, #b3160e, #b36561);
   background: -o-linear-gradient(top, #b3160e, #b36561);
   background-image: -ms-linear-gradient(top, #b3160e 0%, #b36561 100%);
   background-image: -ms-linear-gradient(top, #b0733a 0%, #94221c 100%);
   padding: 10.5px 21px;
   -webkit-border-radius: 6px;
   -moz-border-radius: 6px;
   border-radius: 6px;
   -webkit-box-shadow: rgba(255,255,255,0.4) 0 1px 0, inset rgba(255,255,255,0.4) 0 1px 0;
   -moz-box-shadow: rgba(255,255,255,0.4) 0 1px 0, inset rgba(255,255,255,0.4) 0 1px 0;
   box-shadow: rgba(255,255,255,0.4) 0 1px 0, inset rgba(255,255,255,0.4) 0 1px 0;
   text-shadow: #c25555 0 1px 0;
   color: #ffffff;
   font-size: 45px;
   font-family: helvetica, serif;
   text-decoration: none;
   vertical-align: middle;
   }
.button:hover {
   border: 1px solid #0a3c59;
   text-shadow: #9e5b2f 0 1px 0;
   background: #94221c;
   background: -webkit-gradient(linear, left top, left bottom, from(#b0733a), to(#94221c));
   background: -webkit-linear-gradient(top, #b0733a, #94221c);
   background: -moz-linear-gradient(top, #b0733a, #94221c);
   background: -ms-linear-gradient(top, #b0733a, #94221c);
   background: -o-linear-gradient(top, #b0733a, #94221c);
   background-image: -ms-linear-gradient(top, #b0733a 0%, #94221c 100%);
   color: #fff;
   }
.button:active {
   text-shadow: #574c1e 0 1px 0;
   border: 1px solid #403018;
   background: #d69b65;
   background: -webkit-gradient(linear, left top, left bottom, from(#9c893e), to(#94221c));
   background: -webkit-linear-gradient(top, #9c893e, #d69b65);
   background: -moz-linear-gradient(top, #9c893e, #d69b65);
   background: -ms-linear-gradient(top, #9c893e, #d69b65);
   background: -o-linear-gradient(top, #9c893e, #d69b65);
   background-image: -ms-linear-gradient(top, #9c893e 0%, #d69b65 100%);
   color: #fff;
   }
   div {
    
    padding-top: 10px;
    padding-right: 10px;
    padding-bottom: 5px;
    padding-left: 0px;
}
   </style>
      <!-- This is the background for our website-->
   <body background="pexels-photo-326279 (1).jpeg">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <!--Css code for the tab tool bar buttons-->
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color:   #800000;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color:   #800000;
  color: white;
}
</style>
</head>
<!--This is the website tab bar that allows the customer to navigate through the website easily. To access any functionality on our website, two clicks or less are required for ease of use-->
<body>



<div style="padding-left:16px">

</div>
<!--buttons for the different game options-->
   <h1 style="text-align: center;"><span style="color: #ffffff;">Select a Game</span></h1>

   <div><form>
<input class="Button" type="button" value="UNO"onclick="location.href='uno.html';" />
</form><div>
  <div><<form>
<input class="Button" type="button" value="Piano Tiles"onclick="location.href='piano.html';"/>
</form><div>
<div><<form>
<input class="Button" type="button" value="Go Back"onclick="location.href='products.php';"/>
</form><div>

</body>
</html>