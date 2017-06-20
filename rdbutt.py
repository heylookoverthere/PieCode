from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23,GPIO.OUT)

inv_short=.01
inv_long=.025
delay=1

onetime=datetime.now()
twotime=datetime.now()
threetime=datetime.now()
fourtime=datetime.now() 

def signalone():
    GPIO.output(17,GPIO.HIGH)
    sleep(inv_long)
    GPIO.output(17,GPIO.LOW)
    sleep(inv_short)
    GPIO.output(17,GPIO.HIGH)
    sleep(inv_long)
    GPIO.output(17,GPIO.LOW)
    sleep(inv_short)
    GPIO.output(17,GPIO.HIGH)
    sleep(inv_long)
    GPIO.output(17,GPIO.LOW)
    sleep(inv_long)	

def signaltwo():
    GPIO.output(17,GPIO.HIGH)
    sleep(inv_short)
    GPIO.output(17,GPIO.LOW)
    sleep(inv_short)
    GPIO.output(17,GPIO.HIGH)
    sleep(inv_short)
    GPIO.output(17,GPIO.LOW)
    sleep(inv_short)
    GPIO.output(17,GPIO.HIGH)
    sleep(inv_short)
    GPIO.output(17,GPIO.LOW)
    sleep(inv_long)

def signalthree():
    GPIO.output(17,GPIO.HIGH)
    sleep(inv_short)
    GPIO.output(17,GPIO.LOW)
    sleep(inv_long)

def signalfour():
    GPIO.output(17,GPIO.HIGH)
    sleep(inv_long)
    GPIO.output(17,GPIO.LOW)
    sleep(inv_long)
#p=raw_input("?")
try:
    GPIO.output(23,1)
    print "ready."
    while(True):
        oneflag=(datetime.now()-onetime).total_seconds()
        twoflag=(datetime.now()-twotime).total_seconds()
        threeflag=(datetime.now()-threetime).total_seconds()
        fourflag=(datetime.now()-fourtime).total_seconds()
        if GPIO.input(27) and oneflag>delay:
	    print "sending signal one"
	    GPIO.output(23,1)
	    signalone()
            onetime=datetime.now()
            print "done"
	    GPIO.output(23,0)
	elif GPIO.input(18) and twoflag>delay:
            print "sending signal two"
	    GPIO.output(23,1)
	    signaltwo()
            twotime=datetime.now()
            print "done"
	    GPIO.output(23,0)
        elif GPIO.input(22)and threeflag>delay:
            print "sending signal three"
            GPIO.output(23,1)
            signalthree()
            threetime=datetime.now()
            print "done"
            GPIO.output(23,0)
        elif GPIO.input(24) and fourflag>delay:
            print "sending signal four"
            GPIO.output(23,1)
            signalfour()
            fourtime=datetime.now()
            print "done"
            GPIO.output(23,0)
    GPIO.output(23,0)
    GPIO.cleanup()
	
finally:
    GPIO.output(23,0)
    GPIO.cleanup()
