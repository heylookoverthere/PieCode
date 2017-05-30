import RPi.GPIO as GPIO
import datetime
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23,GPIO.OUT)

plop=8;

try:
    pwm=GPIO.PWM(23,60)
    while True:
        #pwm=GPIO.PWM(23,60)
        pwm.start(8)
        print "Centering"
        plop=int(input("3-13: "))
       # sleep(2)
       # pwm.stop()
        if(plop==99):
            while True:
                for op in xrange(3,14):
                    pwm.ChangeDutyCycle(op)
                    print "moving to "+str(op)
                    sleep(1)
                for op in xrange(14,3,-1):
                    pwm.ChangeDutyCycle(op)
                    print "moving to "+str(op)
                    sleep(1)
            plop=8
            pwm.ChangeDutyCycle(plop)
	if(plop==98):
            for crop in range(300,1400):
                plep=crop/1000
                pwm.ChangeDutyCycle(plep)
                print "moving to "+str(plep)
                sleep(0.1)
        if(plop<3):
            print "Too low."
            plop=3
        if(plop>14):
            print "Too high."
            plop=14
        sleep(1)
        #pwm.ChangeFrequency(90)
        pwm.ChangeDutyCycle(plop);
        print "moving to "+str(plop)
        sleep(1)
    pwm.stop()     
    GPIO.cleanup();		
finally:
    print "centering..."
    pwm.ChangeDutyCycle(8)
    sleep(1)
    pwm.stop()
    GPIO.output(23,0)
    GPIO.cleanup();

