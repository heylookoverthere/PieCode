import RPi.GPIO as GPIO
import picamera
from time import sleep
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

booboo=picamera.PiCamera()
#booboo.vflip=True

plop=0;

lastmotion=datetime.datetime.now()

try:
    print str(lastmotion)," will begin in two minutes"
    sleep(120)
    while True:
        boop=(datetime.datetime.now()-lastmotion).total_seconds()
        if (boop>62) and GPIO.input(23):
            print "Motion detected at ",datetime.datetime.now()
            lastmotion=datetime.datetime.now()
            title="motmov"+str(lastmotion)
            fulltitle=title+".h264"
            booboo.start_recording(fulltitle,format='h264')
            sleep(60)
            booboo.stop_recording()
            output=fulltitle+ " "+title+".mp4"
            print "video saved at ",fulltitle
    GPIO.cleanup();
finally:
    GPIO.cleanup();
