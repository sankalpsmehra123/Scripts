# WiFi Login Script

Small Script for loging into college, or office wifi using Mozilla Firefox web browser. Steps to use :

1.Download or clone the script to your local machine. (preferably in home folder)

2.Download geckodriver for mozilla firefox ([link Given Below][1])

3.Change perameters website_link, username1, and password1 in script.py file
  -Example : 
   website_link = "http://192.168.56.2:8090/"
   username1 = "pine"
   password1 = "qwerty"

4.Change PATH variable accoding to location of geckodriver
  -Example: 
   export PATH=$PATH:/home/usr/geckodriver-v0.24.0-linux64

5.After that make script.sh file executable by using 'chmod +x' command.(use sudo if required)

6.then run the script.sh on terminal while connected to Wifi.

[1] https://github.com/mozilla/geckodriver
