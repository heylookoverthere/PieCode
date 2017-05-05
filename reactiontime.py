import random, time
from time import sleep
import datetime
import RPi.GPIO as GPIO
 
RUNNING = True
GPIO.setmode(GPIO.BCM)
red = 18
green = 17
blue = 27

GPIO.setup(4, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(23, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
 
Freq = 100 #Hz

RED = GPIO.PWM(red, Freq)
RED.start(0)
GREEN = GPIO.PWM(green, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(blue, Freq)
BLUE.start(0)
 
# Define a simple function to turn on the LED colors
def color(R, G, B, on_time):
    # Color brightness range is 0-100%
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)
    time.sleep(on_time)
 
    # Turn all LEDs off after on_time seconds
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)
 
try:
    results=[];
    result=0;
    GPIO.output(22,1)
    for i in xrange(0,3):
        RED.ChangeDutyCycle(0)
        GREEN.ChangeDutyCycle(0)
        BLUE.ChangeDutyCycle(0)
	delay=random.randint(2,12)
        x=0
        y=100
        z=0
	print "get ready..."
	sleep(delay)
	ontime=datetime.datetime.now()
	waiting=True
	GPIO.output(4,1)
	while waiting:
            if GPIO.input(23) or ((datetime.datetime.now()-ontime).total_seconds())>59:
		result=datetime.datetime.now()-ontime
                GPIO.output(4,0);
	        results.append(result.total_seconds())
	        if(result.total_seconds()<59):
                    print "result ",i+1,":",result.total_seconds()
		    if(result.total_seconds()>3):
			print "...seriously?"
                else:
		    print "No reaction detected at all. Moving on."
                if result.total_seconds()>0.35:
                    x=100
                    y=25
                    z=0
                if result.total_seconds()>0.55:
	            x=100
		    y=0
		    z=0
		if result.total_seconds()<0.2:
		    x=100
		    y=100
		    z=100

                RED.ChangeDutyCycle(x)
                GREEN.ChangeDutyCycle(y)
                BLUE.ChangeDutyCycle(z)
                waiting=False
		sleep(1)
    avg=(results[0]+results[1]+results[2])/3
    print "Average response time  was ",avg," seconds."
except KeyboardInterrupt:
    RUNNING = False

finally:
    GPIO.cleanup()
