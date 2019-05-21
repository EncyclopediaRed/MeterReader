import RPi.GPIO as GPIO
import calendar
import datetime
now = datetime.datetime.now()
calendar.monthrange(now.year, now.month)[1]

from time import sleep
from picamera import PiCamera

# Turns on LED light at Pin 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # Hides any warnings
GPIO.setup(18,GPIO.OUT)
print "LED on"
GPIO.output(18,GPIO.HIGH)
sleep(10) # Keeps the light on for 10 seconds while the camera snaps the pic

# Snap a picture and save the resulting image as "image.jpg"
camera = PiCamera()
camera.resolution = (3280, 2464)
camera.vflip = True
camera.hflip = True
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('image.jpg')

# Turn off LED after camera has taken the photo and saved it
print "Picture taken, LED now off"
GPIO.output(18,GPIO.LOW)

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# Define these once; use them twice!
strFrom = 'example@gmail.com'
strTo = 'example@gmail.com'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'APT XXX'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('Apartment #XXX<br><br><img src="cid:image1">', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('image.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('example@gmail.com', 'password')
server.sendmail(strFrom,strTo,msgRoot.as_string())
server.quit()