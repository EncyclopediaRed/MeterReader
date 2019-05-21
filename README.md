# MeterReader
A Python script for a Raspberry Pi with a camera and an LED light that turns on the LED light, snaps a pic of the meter, saves it to disk, and sends it to the property manager via email.

1. Connected via WiFi, the Raspberry Pi will check the current day and time with a cronjob and if the Day is the last day of the current Month, at 01:00 the cronjob will fire meterread.py. 

2. Once snapped and saved, the photo will be emailed to the Property Manager using an exsiting Gmail email address.

Resources:
- http://picamera.readthedocs.io/
- https://www.raspberrypi.org/documentation/usage/camera/python/README.md
- https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
- https://www.raspberrypi.org/forums/viewtopic.php?t=60660&p=454138
- http://code.activestate.com/recipes/473810-send-an-html-email-with-embedded-image-and-plain-t/ (email section)
- https://wiki.debian.org/TimeZoneChanges (Changing time on the Pi)
- https://www.raspberrypi.org/documentation/linux/usage/cron.md (Setting cron job up on Pi)
- http://raspberrypituts.com/raspberry-pi-simple-cron-jobs-explanation/ (more cron help)
- https://www.remot3.it (connecting to the Raspberry Pi remotely without port forwarding)