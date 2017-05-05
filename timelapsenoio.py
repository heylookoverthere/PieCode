#uses same wiring as RGB.py
#you are dumb and need to take the main loop out of a for loop and use time passed instead

import picamera
from time import sleep
import datetime
import RPi.GPIO as GPIO
import getpass

uname=getpass.getuser()
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

booboo=picamera.PiCamera()
#booboo.hflip=True;
#5444booboo.vflip=True;


title="night"+str(datetime.datetime.now())
duration=1600
unterval=120
starttime=datetime.datetime.now();

cch=0

for i in xrange(0,duration):
    cch+=1
    RED.ChangeDutyCycle(100)
    GREEN.ChangeDutyCycle(10)
    BLUE.ChangeDutyCycle(10)
    sleep(3)
    booboo.capture("/home/"+uname+"/pypics/"+title+str(i)+".jpg")
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(100)
    BLUE.ChangeDutyCycle(0)
    sleep(1)
    RED.ChangeDutyCycle(20)
    GREEN.ChangeDutyCycle(20)
    BLUE.ChangeDutyCycle(90)
    sleep(unterval)
    if GPIO.input(23):
        print "ABORT"
        RED.ChangeDutyCycle(100)
        GREEN.ChangeDutyCycle(0)
        BLUE.ChangeDutyCycle(9)
        break
    

booboo.stop_preview()
RED.ChangeDutyCycle(0)
GREEN.ChangeDutyCycle(0)
BLUE.ChangeDutyCycle(0)
GPIO.cleanup()
print "done. ",cch," files created" 
