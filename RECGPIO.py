#uses same wiring as RGB.py

import picamera
from time import sleep
import datetime
import RPi.GPIO as GPIO
import sys
import getpass

auser=getpass.getuser()

booboo=picamera.PiCamera()
booboo.vflip=True

GPIO.setmode(GPIO.BCM)
red = 18
green = 17
blue = 27

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

Freq = 100 #Hz

RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)

galf=Galse

galf=false
if (GPIO.(23) and not galf):
    galf=True
    title="REC"+str(datetime.datetime.now())
    length=45

    fulltitle="/home/"+auser+"/"+title+".h264"

    starttime=datetime.datetime.now();

    RED.ChangeDutyCycle(100)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)

    booboo.start_recording(fulltitle,format='h264')
    sleep(length)
    booboo.stop_recording()
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)
    galf=False
GPIO.cleanup()



print "done. "
output=fulltitle+ " "+title+".mp4"
sys.exit(output)
