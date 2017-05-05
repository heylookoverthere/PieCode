import random, time
import RPi.GPIO as GPIO
 
RUNNING = True
GPIO.setmode(GPIO.BCM)
red = 17
green = 18
blue = 27

GPIO.setup(4, GPIO.OUT)
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
    GPIO.output(4,1);
    while RUNNING:
        x=0
        y=0
        z=0
        if GPIO.input(23) or False:
            x=random.randint(0,1)
            y=random.randint(0,1)
            z=random.randint(0,1)
            while x==0 and y==0 and z==0:
                x=random.randint(0,1)
                y=random.randint(0,1)
                z=random.randint(0,1)
            print (x,y,z)
            # Slowly ramp up power percentage of each active color
            for i in range(0,101):
                color((x*i),(y*i),(z*i), .02)
               
            RED.ChangeDutyCycle(x*100)
            GREEN.ChangeDutyCycle(y*100)
            BLUE.ChangeDutyCycle(z*100)

except KeyboardInterrupt:
    RUNNING = False
    print "\Quitting"

finally:
    GPIO.output(4,0);
    GPIO.cleanup()
