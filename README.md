# MeterReader
A remote meter reader that snaps a picture of the meter and sends it to an email address you specify.
![Finished Build of The Meter Reader](Photos/00-Finished-Meter-Reader.jpg)
![Finished Meter Reader with top seperated from body of the irrigation valve cover](Photos/06-Top-Seperated.jpg)
![Underside of the Meter Reader Showing the Camera and LED](Photos/09-Underside.jpg)

# Why It Exists
Recently my office needed a way to record water meter dials at the end of each month so we could send them to a 3rd party billing service. The water meters were inaccessible without a lot of effort, so we needed a way to read the meters remotely. The reader needed to be able to snap a picture of the meter dial in the dark and be suspended high enough to be able to keep the photo in focus. An irrigation valve cover was perfect for this as it had the holes at the bottom to clear the waterpipes going in and out of the meter. It also allowed for enough height for the installed camera, and was cheap ;).

After testing a number of LED lights, the best for the job ended up being an infrared LED. It was bright enough in photos (using a Pi NoIR Camera) and didn't lens flare against the plastic cover of the meter. The Pi NoIR Camera perfectly picked up the light from the LED and was able to take incredibly clear and detailed photos of the meter.

Connected via WiFi, the Raspberry Pi will check the current day and time with a cronjob and if the Day is the last day of the current Month, at 01:00 the cronjob will fire [meterread.py](https://github.com/EncyclopediaRed/MeterReader/blob/master/meterread.py).

# Materials List
* Irrigation Valve Cover
* Raspberry Pi Model B
* Infrared LED
* Jumper Wires
* 330 ohm Resistor
* Pi NoIR Camera v2
* Raspberry Pi Camera Cable
* Heat Shrink Tubing
* Solder & Soldering Iron

# Building
![Electronics Mockup Sketch](Water%20Meter%20Sketch.png)
![Electronics Actual Build](Photos/02-Pi-Wire-and-Cables.jpg)

# Resources
The meterread.py code is really just a hodgpodge of bits of scripts from similiar projects. I've included any references to any of the code and help I found below.
* http://picamera.readthedocs.io/
  * Pi Camera Docs - A Python Interface for the Raspberry Pi Camera
* https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
  * Getting Started With Pi Camera
* https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
  * Pi Camera Module Documentation
* https://www.raspberrypi.org/forums/viewtopic.php?t=60660&p=454138
  * How to see a live feed on the camera to help adjust the focus (which is manually done)
* http://code.activestate.com/recipes/473810-send-an-html-email-with-embedded-image-and-plain-t/
  * (email section)
* https://wiki.debian.org/TimeZoneChanges
  * (Changing time on the Pi)
* https://www.raspberrypi.org/documentation/linux/usage/cron.md
  * (Setting cron job up on Pi)
* http://raspberrypituts.com/raspberry-pi-simple-cron-jobs-explanation/ 
  * (more cron help)
* [https://www.remote.it ](https://www.remote.it/)
  * (connecting to the Raspberry Pi remotely without port forwarding)
