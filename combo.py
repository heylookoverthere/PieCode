import RPi.GPIO as GPIO
import datetime
import time
import smbus
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #button 3
GPIO.setup(23,GPIO.OUT) #Servo
GPIO.setup(15,GPIO.OUT) #buzzer
GPIO.setup(24,GPIO.OUT) #relay
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)#button 1
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #button 2
GPIO.output(24,GPIO.LOW)
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

SONGTWO =	[
	["c5",4],["eb5",4],["d5",4],["c5",4],["f5",4],["eb5",4]
	]

SONGOFF =	[
	["c5",32],["d4",16]
	]

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
	p = GPIO.PWM(15, 440)
	p.start(0.5)
	for t in SONGTWO:
		playTone(p,t)

# Define some device parameters for LCD
I2C_ADDR  = 0x27# I2C device address, if any error, change this address to 0x3f
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
LCD_BACKLIGHT_OFF = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

bus = smbus.SMBus(1)

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)
		
#---------------

lcd_init()
plop=8;
pwm=GPIO.PWM(23,60)
pwm.start(8)
rlay=False
try:
	lcd_string("Welcome.",LCD_LINE_1)
	sleep(2)
	lcd_string("Red = Servo      ",LCD_LINE_1)
        lcd_string("Blue = Song      ",LCD_LINE_2)
	while(True):
		if GPIO.input(27) and GPIO.input(17):
		    lcd_string("Pick one!           ",LCD_LINE_1)
		    lcd_string("",LCD_LINE_2)
		    continue
                elif(GPIO.input(25)):
                    rlay=not rlay
                    if(not rlay):
                        print "relay off"
                        lcd_string("Relay off           ",LCD_LINE_1)
			lcd_string("                    ",LCD_LINE_2)
		        GPIO.output(24,GPIO.LOW)
		    else:
		        print "relay on"
                        lcd_string("Relay on            ",LCD_LINE_1)
			lcd_string("                    ",LCD_LINE_2)
		        GPIO.output(24,GPIO.HIGH)
                    sleep(1)
	            lcd_string("Red = Servo      ",LCD_LINE_1)
                    lcd_string("Blue = Song      ",LCD_LINE_2)
		elif(GPIO.input(27)):
                        pwm.ChangeDutyCycle(8)
			print "Centering"
			lcd_string("Centering           ",LCD_LINE_1)
			lcd_string("                    ",LCD_LINE_2)
			plop=9#int(input("3-13: "))
			if(plop==99):
				ploop=0
				while ploop<1:
					for op in xrange(3,14):
						pwm.ChangeDutyCycle(op)
						print "moving to "+str(op)
						lcd_string("Moving to pos:   ",LCD_LINE_1)
						kop=str(op)+"                "
						lcd_string(kop,LCD_LINE_2)
						sleep(1)
					for op in xrange(14,3,-1):
						pwm.ChangeDutyCycle(op)
						print "moving to "+str(op)
						lcd_string("Moving to pos:    ",LCD_LINE_1)
						kop=str(op)+"                "
						lcd_string(kop,LCD_LINE_2)
						sleep(1)
					ploop=ploop+1
			else:
                                op=8
                                bail=True
                                while(bail):
                                    if GPIO.input(25):
                                        #pwm.ChangeDutyCycle(8)
                                        #sleep(1)
                                        #pwm.stop()
                                        lcd_string("Red = Servo      ",LCD_LINE_1)
                                        lcd_string("Blue = Song      ",LCD_LINE_2)
                                        bail=False
                                        #continue
                                    elif GPIO.input(27):
                                        op-=1
                                        if op<3:
                                            op=3
                                        pwm.ChangeDutyCycle(op)
				        print "moving to "+str(op)
				        lcd_string("Moving to pos:   ",LCD_LINE_1)
				        kop=str(op)+"                "
				        lcd_string(kop,LCD_LINE_2)
                                    elif GPIO.input(17):
                                        op+=1
                                        if op>14:
                                           op=14
                                        pwm.ChangeDutyCycle(op)
				        print "moving to "+str(op)
				        lcd_string("Moving to pos:   ",LCD_LINE_1)
				        kop=str(op)+"                "
				        lcd_string(kop,LCD_LINE_2)
			#pwm.stop()     
			lcd_string("Red = Servo       ",LCD_LINE_1)
			lcd_string("Blue = Song       ",LCD_LINE_2)
			#GPIO.cleanup();
			continue
		elif(GPIO.input(17)):
			lcd_string("Playing Song...      ",LCD_LINE_1)
			lcd_string("                    ",LCD_LINE_2)
			runsong();
			GPIO.output(15, GPIO.HIGH)
			lcd_string("Song completed:     ",LCD_LINE_1)
			lcd_string("                    ",LCD_LINE_2)
			sleep(2)
			lcd_string("Red = Servo         ",LCD_LINE_1)
			lcd_string("Blue = Song         ",LCD_LINE_2)
			continue
finally:
    print "centering..."
    lcd_string("Centering servo:     ",LCD_LINE_1)
    lcd_string("                    ",LCD_LINE_2)
    pwm.ChangeDutyCycle(8)
    sleep(1)
    p = GPIO.PWM(15, 440)
    p.start(0.5)
    for t in SONGOFF:
        playTone(p,t)
    lcd_string("Goodbye.",LCD_LINE_1)
    lcd_string("                    ",LCD_LINE_2)
    pwm.stop()
    sleep(1)
    lcd_byte(0x01, LCD_CMD)
    GPIO.output(23,0)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(24,GPIO.LOW)
    GPIO.cleanup();

