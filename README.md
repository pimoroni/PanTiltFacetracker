Mini Pan-Tilt Face Tracker
==========================

You will need:
* Adafruit Mini Pan-Tilt Kit with Servos
* Adafruit 16-Channel Servo Driver
* A Pi Camera
* A long ribbon cable
* Some sort of power supply for your servos

You will also need to make sure your Pi is up-to-date:

    curl -sS get.pimoroni.com/uptodate | bash

And install OpenCV and SMBus for Python:

    sudo apt-get install python-smbus python-opencv opencv-data

To run this example, you should fire up your desktop with startx,
open up an LXTerminal window and run:

    ./facetracker.py


Note
----

You can use an Arduino to drive the servos, or drive them directly off your Pi, but I found the Servo Driver to be the most stable, reliable and satisfying method and thus this code is written with it in mind.


Adafruit Library Files
----------------------

You should install the following Adafruit Python library:

    sudo pip install adafruit-gpio
    sudo pip install adafruit-pca9685


The following files, retained in the repository for historical reasons, come from https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code and fall under the below copyright conditions.

* Adafruit_I2C.py
* Adafruit_PWM_Servo_Driver.py

Copyright (c) 2012-2013 Limor Fried, Kevin Townsend and Mikey Sklar for Adafruit Industries. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. * Neither the name of the nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
