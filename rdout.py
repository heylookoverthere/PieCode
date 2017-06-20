from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

#p=raw_input("?")
if True:
    GPIO.output(17,GPIO.HIGH)
    sleep(.5)
    GPIO.output(17,GPIO.LOW)
    sleep(.25)
    GPIO.output(17,GPIO.HIGH)
    sleep(.5)
    GPIO.output(17,GPIO.LOW)
    sleep(.25)
    GPIO.output(17,GPIO.HIGH)
    sleep(.5)
    GPIO.output(17,GPIO.LOW)
    #sleep(5)
    GPIO.cleanup()
