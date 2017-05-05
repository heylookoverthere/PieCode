#So save a list of the beeps in each letter. Just short or long. 
#Ok so if gap between presses is longer than M, it's a new letter. Longer than N, it's a new word. Longer than Z, it's a new sentence.
#you should end up with a list of strings like 01 110 01010 010101. 011   

import RPi.GPIO as GPIO
import datetime
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

plop=0;

try:
    GPIO.output(18,1)
    while True:
        if GPIO.input(25):
            print "Merp at ",datetime.datetime.now()
            GPIO.output(24,1)
            if(galf):
                galf=False
                if plop==1:
                    plop=0;
                else:
                    plop=1;
            GPIO.output(18,plop)
	else:
            #print "No Merp"
            galf=True
            GPIO.output(24,0)
        sleep(0.1)
		
finally:
    GPIO.output(18,0)
    GPIO.cleanup();
