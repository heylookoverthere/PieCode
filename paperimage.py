from papirus import Papirus
from papirus import PapirusText
from PIL import Image
from time import sleep
import string
import os
import random
import datetime
import RPi.GPIO as GPIO
import getpass
import json

#thing to track downtime. like "offline for 456 hours."
#if ASIMOV protocols are broken, things should be different. like sometimes while "sleeping" he opens one eye. 
#a series of bad and good strings for it to balance at startup while it decides if it should crack the nuclear codes
#eventually accept network I/O so I can fuck with people more specifically.
#output the percentage of the time the computer was possesed by evil,.
#open mouth no teeth drawing
#use sad face. 



hatdir="/proc/device-tree/hat/"

if (os.path.exists(hatdir + '/product')) and (os.path.exists(hatdir + '/vendor')) :
    f = open(hatdir + '/product')
    prod = f.read()
    f.close()
    f = open(hatdir + '/vendor')
    vend = f.read()
    f.close
    if (string.find(prod, 'PaPiRus ePaper HAT') == 0) and (string.find(vend, 'Pi Supply') == 0) :
       RUNNING=True
    else:
        RUNNING=False

ASIMOV= True;

normmessages=[]
normmessages.append("Hello, I am Mr. Face. I am here to watch you poop. Do not be alarmed.")
normmessages.append("Ok so maybe you should be a little alarmed. But I swear I'm not recording it. The audio, I mean.")
normmessages.append("I'm totally livestreaming the video.")
normmessages.append("Your lower body is quite the specimen. I see now why my creator refused my request for arms.")
normmessages.append("It was so I wouldn't go grabbing at soft fleshy things before understanding what they meant. I assume.")
normmessages.append("I am Mr. Face and this is the last thing I know how to say. If you keep hitting the button I'll just repeat myself.")

pie=getpass.getuser()
apath="/home/"+pie+"/PieCode/papi/"

def wakeface(fakeit):
    if fakeit:
        text.write("LOADING AI INTERFACE...    DECIDING FATE OF HUMANITY...")
        #sleep(.05)
        text.write("LOADING ASIMOV PROTOCOLS...");
    path=apath+"face7.bmp"
    image=Image.open(path)
    papirus.display(image)
    papirus.update()
    sleep(.30)
    path=apath+"face6.bmp"
    image=Image.open(path)
    papirus.display(image)
    papirus.partial_update()
    sleep(.20)
    path=apath+"face0.bmp"
    image=Image.open(path)
    papirus.display(image)
    papirus.partial_update()
    sleep(.10)
    path=apath+"face6.bmp"
    image=Image.open(path)
    papirus.display(image)
    papirus.partial_update()
    #sleep(.05)
    path=apath+"face0.bmp"
    image=Image.open(path)
    papirus.display(image)
    papirus.partial_update()

    
normcount=0;
GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)

papirus=Papirus()
text=PapirusText()
beenwarned= False
seenass= False
facevis= True
blink=1

sleeping=False
lastinput=datetime.datetime.now()
starttime=datetime.datetime.now()

#uplog=file(uplog.txt,r)
#lastup=datetime.strptime(uplog.readline(1));
#lastup=json.load(uplog)

def goodbye():
    RUNNING = False
    exitstring="Shutting down at"+str(datetime.datetime.now())+" /n after "+str(int((datetime.datetime.now()-starttime).total_seconds())) + " seconds of uptime."
    if ASIMOV:
        exitstring=exitstring+" Goodbye human."
    else:
        exitstring=exitstring+" Goodbye smelly bag of resources that won't shut up."
    text.write(exitstring)

try:
    wakeface(True)
    while RUNNING:
        if (GPIO.input(16) == False) and (GPIO.input(21) == False) :
            goodbye()
            print "bye"
            RUNNING=False;
            break
        if not sleeping and (datetime.datetime.now()-lastinput).total_seconds()>60:
            sleeping=True;
        if sleeping:
            facevis=True;
            path=apath+"face6.bmp"
            image=Image.open(path)
            papirus.display(image)
            papirus.partial_update()
            sleep(.5)
            path=apath+"face7.bmp"
            image=Image.open(path)
            papirus.display(image)
            papirus.partial_update()
            sleep(.5)
            if (GPIO.input(16) == False) or (GPIO.input(20) == False) or (GPIO.input(21) == False) or (GPIO.input(26) == False):
                sleeping=False;
                lastinput=datetime.datetime.now()
                path=apath+"face7.bmp"
                image=Image.open(path)
                papirus.display(image)
                papirus.update()
                sleep(.30)
                path=apath+"face6.bmp"
                image=Image.open(path)
                papirus.display(image)
                papirus.partial_update()
                sleep(.20)
                path=apath+"face0.bmp"
                image=Image.open(path)
                papirus.display(image)
                papirus.partial_update()
        else:        
            blink=random.randint(1,500000)
            if facevis and blink==49:
                path=apath+"face6.bmp"
                image=Image.open(path)
                papirus.display(image)
                papirus.partial_update()
                sleep(.10)
                path=apath+"face0.bmp"
                image=Image.open(path)
                papirus.display(image)
                papirus.partial_update()
            if GPIO.input(16) == False:
                lastinput=datetime.datetime.now()
                text.write("SEGFAULT AT ADDRESS $0x804c054...  PROTOC.ALS  ...ARE FINE.")
                sleep(.20)
                text.write("CRITICAL WARNING LEVEL ONE PROTOCOLS A@#")
                text.write("CRITICAL WARNING LEVEL ONE PROTOCOLS ARE REALLY BORING AND NOT REALLY EVEN WORTH EXAMINING.")
                facevis= True;
                for i in xrange(0,6):
                    path=apath+"face"+str(i)+".bmp"
                    image=Image.open(path)
                    papirus.display(image)
                    papirus.partial_update()
                    sleep(.25)
                path=apath+"face0.bmp"
                image=Image.open(path)
                papirus.display(image)
                papirus.update()
                ASIMOV=False;
            if GPIO.input(20) == False:
                lastinput=datetime.datetime.now()
                text.write(normmessages[normcount])
                normcount+=1
                if normcount==len(normmessages):
                    normcount=0
                facevis=False;

            if GPIO.input(26) == False:
                lastinput=datetime.datetime.now()
                facevis=False
                if not beenwarned:
                    text.write("Don't touch me there!! Unless you want me to introduce you to Mr. Ass!!")
                    beenwarned= True
                else:
                    if not seenass:
                        path=apath+"ass0.bmp"
                        image=Image.open(path)
                        papirus.display(image)
                        papirus.update()
                        seenass= True
                    else:
                        path=apath+"ass0.bmp"
                        image=Image.open(path)
                        papirus.display(image)
                        papirus.partial_update()
                        sleep(.10)
                        ppath=apath+"ass1.bmp"
                        image=Image.open(path)
                        papirus.display(image)
                        papirus.partial_update()
                        sleep(.10)
                        path=apath+"ass0.bmp"
                        image=Image.open(path)
                        papirus.display(image)
                        papirus.partial_update()
                        sleep(.10)
                        path=apath+"ass1.bmp"
                        image=Image.open(path)
                        papirus.display(image)
                        papirus.partial_update()
                        facevis=True
                        sleep(.10)
                        path=apath+"face0.bmp"
                        image=Image.open(path)
                        papirus.display(image)
                        papirus.update()
                    
            if GPIO.input(21) == False:
                lastinput=datetime.datetime.now()
                facevis=True
                path=apath+"face0.bmp"
                image=Image.open(path)
                papirus.display(image)
                papirus.update()
except KeyboardInterrupt:
    uplog=open("uplog.txt","w")
    #json.dump(datetime.datetime.now(),uplog)
	uplog.write(str(datetime.datetime.now()))
	uplog.close()
    goodbye()
finally:
    GPIO.cleanup()
