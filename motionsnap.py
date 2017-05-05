import RPi.GPIO as GPIO
import picamera
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

booboo=picamera.PiCamera()
#booboo.vflip=True

plop=0;

lastmotion=datetime.datetime.now()

try:
    while True:
        boop=(datetime.datetime.now()-lastmotion).total_seconds()
        if (boop>4) and GPIO.input(23):
            print "Motion detected at ",datetime.datetime.now()
            lastmotion=datetime.datetime.now()
            title="mot"+str(boop)
            booboo.capture("/home"+auser+"/pypics/"+title+".jpg")
	
finally:
    GPIO.cleanup();
