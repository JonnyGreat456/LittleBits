-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 10, 2016 at 03:44 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `shop_cart_sessions_1`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE IF NOT EXISTS `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(512) NOT NULL,
  `description` text NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `created` datetime NOT NULL,
  `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COMMENT='products that can be added to cart' AUTO_INCREMENT=41 ;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `description`, `price`, `created`, `modified`) VALUES
(27, 'San Antonio Spurs Kawhi Leonard #2 \nAdidas Black T-Shirt', '&lt;p&gt;Kawhi Leonard San Antonio Spurs T shirt, made by Adidas the official on court producers of NBA apparel and jerseys.&lt;/p&gt;\r\n&lt;p&gt;Leonard and 2 are printed on the back in authentic font.&lt;/p&gt;\r\n&lt;ul&gt;\r\n&lt;li&gt;Basic Print&lt;/li&gt;\r\n&lt;li&gt;Officially licensed NBA Product&lt;/li&gt;\r\n&lt;li&gt;NBA Hologram Sticker&lt;/li&gt;\r\n&lt;li&gt;Mens Sizing&lt;/li&gt;\r\n&lt;li&gt;100% Cotton&lt;/li&gt;\r\n&lt;li&gt;Adidas &quot;Go To Tee&quot;&lt;/li&gt;\r\n&lt;/ul&gt;', '99.99', '2016-10-28 20:49:40', '2016-10-28 12:49:40'),
(28, 'LaMarcus Aldridge San Antonio Spurs NBA Adidas Player Black T-Shirt', '&lt;p&gt;Looks like a jersey, wears like a tee -- this 100% cotton Adidas NBA player name and number t-shirt sports screen prints of your favorite player''s name and number, plus team graphics on the chest.&lt;/p&gt;\r\n&lt;p&gt;Officially licensed by the NBA.&lt;/p&gt;', '49.99', '2016-10-28 20:52:43', '2016-10-28 12:52:43'),
(29, 'Tim Duncan San Antonio Spurs Jersey Name and Number T-Shirt', '&lt;p&gt;Cheer on Tim Duncan and the Spurs as they begin their road to repeating as NBA champions.&lt;/p&gt;\r\n&lt;p&gt;Show your support for Duncan and the San Antonio Spurs in your very own black Spurs Name and Number Tee.&lt;/p&gt;', '29.99', '2016-10-28 20:56:23', '2016-10-28 12:56:23'),
(30, 'Women''s Customized San Antonio Spurs Black Replica Basketball Jersey', '&lt;p&gt;San Antonio Spurs Custom Jerseys with any name and number.&lt;/p&gt;\r\n&lt;p&gt;Choose the style and size.&lt;/p&gt;\r\n&lt;p&gt;There''s no better way to prove your loyalty than to make this jersey your own.&lt;/p&gt;', '29.99', '2016-10-28 20:58:02', '2016-10-28 12:58:02'),
(31, 'Klay Thompson Golden State Warriors Jersey Name and Number T-Shirt', '&lt;p&gt;It''s Splash Time!&lt;/p&gt;\r\n&lt;p&gt;Make sure to show your support for the second half of the splash bros and get your very own Warriors Name and Number Tee.&lt;/p&gt;', '29.99', '2016-10-28 20:59:20', '2016-10-28 12:59:20'),
(32, 'Stephen Curry Golden State Warriors #30 NBA Youth Climalite Player T-Shirt Blue', '&lt;p&gt;Featuring your favorite player''s name and number on back with team logo at front, this Climalite polyester t-shirt provides the ultimate display of pride for a die-hard fan!&lt;/p&gt;', '29.99', '2016-10-28 21:03:19', '2016-10-28 13:03:19'),
(33, 'Adidas Men''s NBA Golden State Warriors-Kevin Durant #35-Mesh Logo T-Shirt', '&lt;p&gt;Show off how excited you are to welcome Kevin Durant to you Golden State Warriors with this Mesh Logo Tee from adidas.&lt;/p&gt;\r\n&lt;p&gt;It features cool graphics made from jersey like mesh and has KD''s name and number on the back.&lt;/p&gt;\r\n&lt;p&gt;A great look, whether you''re at the game, or a friends house watching the new look Warriors.&lt;/p&gt;', '29.99', '2016-10-28 21:05:30', '2016-10-28 13:05:30'),
(34, 'Klay Thompson Golden State Warriors Charcoal Chinese New Year Name and Number T-shirt', '&lt;p&gt;Cheer on Klay all the way to the NBA Finals in style with this unique Chinese New Year Jersey Name and Number t-shirt by adidas.&lt;/p&gt;', '29.99', '2016-10-28 21:06:34', '2016-10-28 13:06:34'),
(35, 'Kevin Durant #35 Women''s Replica Name and Number Short Sleeve', '&lt;p&gt;Let everyone know who you will be cheering for this season in the adidas U Series high density name &amp;amp; number tee.&lt;/p&gt;\r\n&lt;p&gt;Adidas is the official outfitter of the NBA and this tee is the authentic take down name &amp;amp; number tee of your MVP.&lt;/p&gt;\r\n&lt;p&gt;A high density screen print on a soft cotton tee is a must have for every true NBA fan.&lt;/p&gt;', '32.24', '2016-10-28 21:08:05', '2016-10-28 13:08:05'),
(36, 'LeBron James Men''s Navy Cleveland Cavaliers adidas Swingman Jersey', '&lt;p&gt;Prove you are the #1 LeBron James fan with this Swingman jersey from adidas!&amp;nbsp;&lt;/p&gt;\r\n&lt;p&gt;This Swingman is the ultimate Cleveland Cavaliers jersey. Whether it''s going to the game, spending time with your friends or anything in-between - this jersey does it all.&amp;nbsp;&lt;/p&gt;\r\n&lt;p&gt;The Swingman includes adidas Climacool &amp;reg; performance mesh fabrication and one layer twill wordmark, name &amp;amp; number applications.&amp;nbsp;&lt;/p&gt;\r\n&lt;p&gt;The NBA Swingman jersey - the most authentic Swingman ever made.&lt;/p&gt;', '109.93', '2016-10-28 21:08:52', '2016-10-28 13:08:52'),
(37, 'NBA Cleveland Cavaliers Kyrie Irving #2 Men''s Replica Jersey', '&lt;p&gt;Detailed to look like a real NBA jersey and priced to make you cheer!&lt;/p&gt;\r\n&lt;p&gt;This quality NBA Adidas Replica Revolution Jersey features screen printed team graphic, screen printed player name and number on the front and back, tagless collar, and embroidered Adidas and NBA logo''s on the front.&lt;/p&gt;\r\n&lt;p&gt;This new style Adidas replica jersey is made of breathable, easy-care 100% polyester with Clima Cool fabrication. Officially licensed by the NBA.&lt;/p&gt;', '46.99', '2016-10-28 21:09:44', '2016-10-28 13:09:44'),
(38, 'Kevin Love Cleveland Cavaliers #0 NBA Youth Road Jersey Wine', '&lt;p&gt;Detailed to look like a real NBA jersey, sized for a youth, and priced to make you cheer!&lt;/p&gt;\r\n&lt;p&gt;This quality NBA Adidas Replica Jersey features screen printed team graphic, screen printed player name and number on the front and back, tagless collar, and embroidered Adidas and NBA logo''s on the front.&lt;/p&gt;\r\n&lt;p&gt;Perfect for your child or for gift giving. Made of breathable, easy-care 100% polyester with Clima Cool fabrication. Officially licensed by the NBA.', '29.99', '2016-10-28 21:46:06', '2016-10-28 13:46:06'),
(40, 'For Mens San Antonio Spurs Kawhi Leonard #2 Cream White Christmas Day Swingman Basketball Jersey', '&lt;p&gt;This is 100% mesh polyester breathable and quick-dry jersey.&lt;/p&gt;\r\n&lt;p&gt;Player name and number graphics deliver classic style. priced to make you cheer.&lt;/p&gt;\r\n&lt;p&gt;It will be the best gift for you or your friend and family.&lt;/p&gt;', '32.00', '2016-11-02 20:15:38', '2016-11-02 12:15:38');

-- --------------------------------------------------------

--
-- Table structure for table `product_images`
--

CREATE TABLE IF NOT EXISTS `product_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `name` varchar(512) NOT NULL,
  `created` datetime NOT NULL,
  `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT='image files related to a product' AUTO_INCREMENT=105 ;

--
-- Dumping data for table `product_images`
--

INSERT INTO `product_images` (`id`, `product_id`, `name`, `created`, `modified`) VALUES
(83, 30, 'p41.jpg', '2016-10-28 20:58:02', '2016-10-28 12:58:02'),
(82, 29, 'p32.jpg', '2016-10-28 20:56:23', '2016-10-28 12:56:23'),
(81, 29, 'p31.jpg', '2016-10-28 20:56:23', '2016-10-28 12:56:23'),
(80, 28, 'p22.jpg', '2016-10-28 20:52:43', '2016-10-28 12:52:43'),
(79, 28, 'p21.jpg', '2016-10-28 20:52:43', '2016-10-28 12:52:43'),
(77, 27, 'p11.jpg', '2016-10-28 20:49:40', '2016-10-28 12:49:40'),
(78, 27, 'p12.jpg', '2016-10-28 20:49:40', '2016-10-28 12:49:40'),
(84, 31, 'p51.jpg', '2016-10-28 20:59:20', '2016-10-28 12:59:20'),
(85, 31, 'p52.jpg', '2016-10-28 20:59:20', '2016-10-28 12:59:20'),
(86, 32, 'p61.jpg', '2016-10-28 21:03:19', '2016-10-28 13:03:19'),
(87, 32, 'p62.jpg', '2016-10-28 21:03:19', '2016-10-28 13:03:19'),
(89, 33, 'p71.jpg', '2016-10-28 21:05:30', '2016-10-28 13:05:30'),
(90, 33, 'p72.jpg', '2016-10-28 21:05:30', '2016-10-28 13:05:30'),
(91, 34, 'p81.jpg', '2016-10-28 21:06:34', '2016-10-28 13:06:34'),
(92, 34, 'p82.jpg', '2016-10-28 21:06:34', '2016-10-28 13:06:34'),
(93, 34, 'p83.jpg', '2016-10-28 21:06:34', '2016-10-28 13:06:34'),
(94, 35, 'p91.jpg', '2016-10-28 21:08:05', '2016-10-28 13:08:05'),
(95, 35, 'p92.jpg', '2016-10-28 21:08:05', '2016-10-28 13:08:05'),
(96, 36, 'p101.jpg', '2016-10-28 21:08:52', '2016-10-28 13:08:52'),
(97, 36, 'p102.jpg', '2016-10-28 21:08:52', '2016-10-28 13:08:52'),
(98, 36, 'p103.jpg', '2016-10-28 21:08:52', '2016-10-28 13:08:52'),
(99, 37, 'p111.jpg', '2016-10-28 21:09:44', '2016-10-28 13:09:44'),
(100, 37, 'p112.jpg', '2016-10-28 21:09:44', '2016-10-28 13:09:44'),
(101, 37, 'p113.jpg', '2016-10-28 21:09:44', '2016-10-28 13:09:44'),
(102, 38, 'p121.jpg', '2016-10-28 21:46:06', '2016-10-28 13:46:06'),
(103, 38, 'p122.jpg', '2016-10-28 21:46:06', '2016-10-28 13:46:06'),
(104, 40, 'p131.jpg', '2016-11-02 20:15:38', '2016-11-02 12:15:38'),
(51, 14, 'gardman-r687-4-tier-mini-greenhouse-1.jpg', '0000-00-00 00:00:00', '2015-03-19 08:45:42'),
(52, 14, 'gardman-r687-4-tier-mini-greenhouse-2.jpg', '0000-00-00 00:00:00', '2015-03-19 08:45:42'),
(53, 15, 'spalding-nba-street-basketball-1.jpg', '0000-00-00 00:00:00', '2015-03-19 08:48:34'),
(54, 16, 'bandai-hobby-thousand-sunny-model-ship-one-piece-grand-ship-collection-1.jpg', '0000-00-00 00:00:00', '2015-03-19 09:02:25'),
(55, 16, 'bandai-hobby-thousand-sunny-model-ship-one-piece-grand-ship-collection-2.jpg', '0000-00-00 00:00:00', '2015-03-19 09:02:25'),
(56, 16, 'bandai-hobby-thousand-sunny-model-ship-one-piece-grand-ship-collection-3.jpg', '0000-00-00 00:00:00', '2015-03-19 09:02:25'),
(57, 16, 'bandai-hobby-thousand-sunny-model-ship-one-piece-grand-ship-collection-4.jpg', '0000-00-00 00:00:00', '2015-03-19 09:02:25'),
(59, 17, 'bandai-tamashii-nations-nami-new-world-ver-one-piece-figuartszero-bandai-tamashii-nations-2.jpg', '0000-00-00 00:00:00', '2015-03-19 09:07:20'),
(73, 17, '29097235540_b2fefed80d_k.jpg', '2016-09-17 22:01:17', '2016-09-17 14:01:17'),
(74, 25, '14194449_1363884933625826_1306807357_n.jpg', '2016-09-18 01:03:15', '2016-09-17 17:03:15'),
(61, 17, 'bandai-tamashii-nations-nami-new-world-ver-one-piece-figuartszero-bandai-tamashii-nations-4.jpg', '0000-00-00 00:00:00', '2015-03-19 09:07:20'),
(71, 17, 'bandai-tamashii-nations-nami-new-world-ver-one-piece-figuartszero-bandai-tamashii-nations-5.jpg', '2016-08-17 15:53:17', '2016-08-17 07:53:17'),
(67, 19, 'products.jpg', '0000-00-00 00:00:00', '2015-03-26 03:29:34'),
(69, 20, 'tp-link-mr3420-2.jpg', '2016-08-08 14:12:59', '2016-08-08 06:12:59'),
(70, 21, 'd-link-universal-modem.jpg', '2016-08-08 14:24:19', '2016-08-08 06:24:19'),
(75, 25, '29097235540_b2fefed80d_k.jpg', '2016-09-18 01:03:15', '2016-09-17 17:03:15'),
(76, 20, 'aaa.png', '2016-10-13 16:31:58', '2016-10-13 08:31:58');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
