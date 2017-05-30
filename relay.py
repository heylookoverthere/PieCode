import RPi.GPIO as GPIO
import datetime
import time
from time import sleep
GPIO.setmode(GPIO.BCM)

GPIO.setup(15,GPIO.OUT)
GPIO.output(15,GPIO.LOW)

try:
    while (True):
        print "relay off"
        GPIO.output(15,GPIO.LOW)
        sleep(2)
        print "relay on"
        GPIO.output(15,GPIO.HIGH)
        sleep(2)

finally:
    GPIO.output(15,GPIO.LOW)
    GPIO.cleanup();

