Mini Pan-Tilt Face Tracker
==========================

You will need:
* Pimoroni Pan/Tilt HAT Kit
* A Pi Camera
* A long ribbon cable

You will also need to make sure your Pi is up-to-date:

    curl -sS get.pimoroni.com/uptodate | bash

And install OpenCV and SMBus for Python:

    sudo apt-get install python-smbus python-opencv opencv-data

To run this example, you should fire up your desktop with startx,
open up an LXTerminal window and run:

    ./facetracker.py


Note
----

You can use an Arduino to drive the servos, or drive them directly off your Pi, but I found PanTilt HAT to be the most stable, reliable and satisfying method and thus this code is written with it in mind.
