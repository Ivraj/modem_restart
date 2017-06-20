'''
readPin.py

Description: 
	This program reads the specified Raspi Pin. 

mru: Ivraj Seerha 6/16/17
'''
import sys

pin = int(sys.argv[1]) 

import RPi.GPIO as GPIO

def readPin():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    if GPIO.input(pin):
	print(str(pin)+' is high')
    else:
	print(str(pin)+' is low')

if __name__ == "__main__":
    readPin()
