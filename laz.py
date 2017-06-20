from datetime import datetime
import matplotlib.pyplot as pyplot
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)

p=raw_input("?")
if p=="y":
    GPIO.output(23,1)
    sleep(3)
    print("high")
    GPIO.output(23,0)
    sleep(3)
    GPIO.output(23,0)
    GPIO.cleanup()
