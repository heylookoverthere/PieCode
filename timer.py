#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from datetime import datetime
from time import sleep

BuzzerPin = 15    # pin10

SPEED = 1 

# List of tone-names with frequency
TONES = {"c6":1047,
	"b5":988,
	"a5":880,
	"g5":784,
	"f5":698,
	"e5":659,
	"eb5":622,
	"d5":587,
	"c5":523,
	"b4":494,
	"a4":440,
	"ab4":415,
	"g4":392,
	"f4":349,
	"e4":330,
	"d4":294,
	"c4":262}


# Song is a list of tones with name and 1/duration. 16 means 1/16
SONG =	[
	["e5",16],["eb5",16],
	["e5",16],["eb5",16],["e5",16],["b4",16],["d5",16],["c5",16],
	["a4",8],["p",16],["c4",16],["e4",16],["a4",16],
	["b4",8],["p",16],["e4",16],["ab4",16],["b4",16],
	["c5",8],["p",16],["e4",16],["e5",16],["eb5",16],
	["e5",16],["eb5",16],["e5",16],["b4",16],["d5",16],["c5",16],
	["a4",8],["p",16],["c4",16],["e4",16],["a4",16],
	["b4",8],["p",16],["e4",16],["c5",16],["b4",16],["a4",4]
	]

def setup():
	GPIO.setmode(GPIO.BCM) # Numbers GPIOs by physical location
	GPIO.setup(BuzzerPin, GPIO.OUT)

def playTone(p,tone):
        # calculate duration based on speed and tone-length
	duration = (1./(tone[1]*0.25*SPEED))

	if tone[0] == "p": # p => pause
		time.sleep(duration)
	else: # let's rock
		frequency = TONES[tone[0]]
		p.ChangeFrequency(frequency)
		p.start(0.5)
		time.sleep(duration)
		p.stop()

def runsong():
	p = GPIO.PWM(BuzzerPin, 440)
	p.start(0.5)
	for t in SONG:
		playTone(p,t)

def destroy():
	GPIO.output(BuzzerPin, GPIO.HIGH)
	GPIO.cleanup()                     # Release resource

setup()
try:
    while True:
        merp=raw_input("Start timer? <y/n>")
        if merp=="y":
            perside=int(raw_input("how long in minutes?"))*60
            print "start burger!",str(datetime.now())
	    p = GPIO.PWM(BuzzerPin, 440)
	    p.start(0.5)
            playTone(p,["c6",8])
           
            flips=0     
	    sleep(perside)
	    playTone(p,["c6",8])
            print "flip burger ",str(datetime.now()) 
            sleep(perside)
            playTone(p,["c5",16])
            print "flip burger! ",str(datetime.now())           
        elif merp=="n":
	    p = GPIO.PWM(BuzzerPin, 440)
	    p.start(0.5)
	    playTone(p,["d4",8])
        else:
           p = GPIO.PWM(BuzzerPin,440)
           p.start(0.5)
           playTone(p,["e4",16])
           playTone(p,["d4",32])
           playTone(p,["d4",32])
finally:
    destroy()