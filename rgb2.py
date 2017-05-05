import random, time
import RPi.GPIO as GPIO
 
RUNNING = True
GPIO.setmode(GPIO.BCM)
red = 17
green = 18
blue = 27

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
    while RUNNING:
        x=0
        y=0
        z=0
        if True:
            x=random.randint(0,100)
            y=random.randint(0,100)
            z=random.randint(0,100)
            while x==0 and y==0 and z==0:
                x=random.randint(0,100)
                y=random.randint(0,100)
                z=random.randint(0,100)
            print (x,y,z)
            # Slowly ramp up power percentage of each active color
               
            RED.ChangeDutyCycle(x)
            GREEN.ChangeDutyCycle(y)
            BLUE.ChangeDutyCycle(z)
            time.sleep(.5)
        if GPIO.input(23):
            print("later!")
            RUNNING=False
    GPIO.cleanup()
except KeyboardInterrupt:
    RUNNING = False
    print "later!"

finally:
    GPIO.cleanup()
