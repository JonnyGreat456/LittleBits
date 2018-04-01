Customers Unit Testing
This is the customers Web application html pages.
To Run make sure that all the html files are in a single folder and start with opening "home.html"
Currently the website does not support a database therefore some of the functionalities are currently not working.
The SOS option, Adding items and placing  the order are currently in the works after the database is complete.
Below is a GUI test with time stamps. 
To run the test, simply run run_customer_GUI.cs but before executing, change line 82 and 83 
Report.Log(ReportLevel.Info, "Website", "Opening web site 'file:///C:/Users/hagar/Desktop/html%20pages/home.html' with browser 'chrome' in normal mode.", new RecordItemIndex(0));
            Host.Current.OpenBrowser("file:///C:/Users/hagar/Desktop/html%20pages/home.html", "chrome", "", false, false, false, false, false);
and change the address of the folder accordingly.
Another way to run the GUI test if Ranorex application "https://www.ranorex.com/" is downloaded on your PC.
If so, Run customerGUI.exe. 
If all of the above fails, there is a video "CustomerGUIscreenCapture.mp4" of a screen recording of all the pages being tested.
Below is the time-line of the GUI test using  Ranorex.

New_Recording
Success
 Computer/Endpoint 
DESKTOP-V148L12 
 Execution time 
4/1/2018 5:17:29 PM 

 Operating system 
Windows 10 64bit 
 Screen dimensions 
1920x1080 

 OS Language 
en-US 
 
 Total errors
0 
 Total warnings
0 
Filter: Info

Time

Level

Category

Message

00:00.906 Info Website 

 Opening web site 'file:///C:/Users/hagar/Desktop/html%20pages/home.html' with browser 'chrome' in normal mode.  
00:01.059 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 146;258.  
00:06.748 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 197;257.  
00:08.031 Info Mouse 

 Mouse scroll Vertical by -120 units.  
00:08.541 Info Mouse 

 Mouse scroll Vertical by 240 units.  
00:09.088 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 174;54.  
00:10.405 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 293;428.  
00:11.690 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 812;338.  
00:12.945 Info Mouse 

 Mouse scroll Vertical by -480 units.  
00:13.458 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 1451;828.  
00:14.747 Info Mouse 

 Mouse scroll Vertical by 360 units.  
00:15.263 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 183;50.  
00:16.518 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 311;610.  
00:17.712 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 798;614.  
00:18.980 Info Mouse 

 Mouse scroll Vertical by -240 units.  
00:19.489 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 1493;881.  
00:20.719 Info Mouse 

 Mouse scroll Vertical by 240 units.  
00:21.276 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 135;44.  
00:22.545 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 249;734.  
00:23.748 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 185;53.  
00:25.010 Info Mouse 

 Mouse scroll Vertical by -120 units.  
00:25.523 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 85;617.  
00:26.845 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 144;59.  
00:28.074 Info Mouse 

 Mouse scroll Vertical by -120 units.  
00:28.604 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 154;726.  
00:29.843 Info Mouse 

 Mouse scroll Vertical by 120 units.  
00:30.355 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 156;35.  
00:31.651 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 254;13.  
00:32.859 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 132;311.  
00:34.162 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 115;265.  
00:35.342 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 211;55.  
00:36.711 Info Mouse 

 Mouse Left Down item 'HomeHtml' at 211;55.  
00:37.886 Info Mouse 

 Mouse Left Up item 'HomeHtml' at 238;29.  
00:39.072 Info Mouse 

 Mouse Left Down item 'HomeHtml' at 238;29.  
00:40.197 Info Mouse 

 Mouse Left Up item 'HomeHtml' at 271;11.  
00:41.321 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 128;422.  
00:42.550 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 253;37.  
00:44.225 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 451;70.  
00:45.476 Info Mouse 
Jump to item  Open in Spy
 Mouse Left Click item 'HomeHtml' at 378;60.  
00:46.723 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 597;57.  
00:47.986 Info Mouse 

 Mouse Left Click item 'HomeHtml' at 380;275 
---------------------------------------------------------------------------------------------------------------------------------------------------
