import RPi.GPIO as GPIO
import datetime
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

plop=1;

try:
    GPIO.output(18,1)
    while True:
		if(galf):
			galf=False
			plop=0
		else:
			galf=True
			plop=1
		GPIO.output(18,plop)
		sleep(0.5)

		
finally:
    GPIO.output(18,0)
    GPIO.cleanup();
