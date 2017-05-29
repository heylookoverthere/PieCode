from email_handler import Class_eMail

import RPi.GPIO as GPIO
from time import sleep
import datetime
import getpass
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

auser=getpass.getuser()

var_To_Email_ID = "heyitserik@gmail.com"


email = Class_eMail()

plop=0;

lastmotion=datetime.datetime.now()

try:
    print str(lastmotion)," will begin in ten minutes"
    sleep(10)
    while True:
        boop=(datetime.datetime.now()-lastmotion).total_seconds()
        if (boop>600) and GPIO.input(23):
            print "Motion detected at ",datetime.datetime.now()
            lastmotion=datetime.datetime.now()
            strang="Motion detected at "+str(lastmotion)
	    var_SUBJECT = "Motion detected in hallway"
            var_EMAIL_BODY = "Might wanna take a look."
            email.send_Text_Mail(var_To_Email_ID, var_SUBJECT, var_EMAIL_BODY)
#            sleep(60)
            print "email sent"
    GPIO.cleanup();
    del email
finally:
    GPIO.cleanup();
    del email
