#uses same wiring as RGB.py

import picamera
from time import sleep
import datetime
import RPi.GPIO as GPIO
import sys
import getpass

booboo=picamera.PiCamera()
booboo.vflip=True

auser=getpass.getuser()
title="home/"+auser+"/pypics/REC"+str(datetime.datetime.now())
length=int(raw_input("How long in seconds?"))

fulltitle=title+".h264"

starttime=datetime.datetime.now();

booboo.start_preview()

booboo.start_recording(fulltitle,format='h264')
sleep(length)
booboo.stop_recording()

booboo.stop_preview()


print "done. "
output=fulltitle+ " "+title+".mp4"
sys.exit(output)
