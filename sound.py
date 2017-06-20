#!/usr/bin/env python
import RPi.GPIO as GPIO
from getch import getch
from time import sleep

IrPin  = 23
LedPin = 17

Led_status = 1

def setup():
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(IrPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.output(LedPin, GPIO.LOW) # Set LedPin high(+3.3V) to off led

def swLed(ev=None):
	global Led_status
	print "thing"
        Led_status = not Led_status
	GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
        if Led_status == 1:
	     print 'led on...'
        else:
	     print '...led off'

def loop():
        GPIO.output(LedPin,GPIO.HIGH)
        sleep(1)
        #GPIO.add_event_detect(IrPin, GPIO.FALLING, callback=swLed) # wait for falling
        while True:
            if(GPIO.input(IrPin)):
                GPIO.output(LedPin,GPIO.HIGH)
            else:
                GPIO.output(LedPin,GPIO.LOW)
def destroy():
	GPIO.output(LedPin, GPIO.LOW)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

