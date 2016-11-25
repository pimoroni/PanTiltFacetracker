Mini Pan-Tilt Face Tracker
==========================

You will need:
* Pimoroni Pan/Tilt HAT Kit
* A Pi Camera

The 15cm ribbon cable supplied with the Pi Camera should be long enough if you're mounting the Pan/Tilt HAT on the Pi.

If you're using a Black HAT Hack3r you may need 30cm.

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
