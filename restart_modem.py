#!/usr/bin/env python
'''Script to restart SIM800 modem if it is turned off. 

This script should be added as a cron job to the RasPi
'''

import os
import serial 
import time
import RPi.GPIO as GPIO

# Necessary in case PATH is different from crontab. 
os.environ['PATH'] = '/opt/someApp/bin:/user/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'

def check_modem():
    try:
        ser = serial.Serial('/dev/serial0', 115200, timeout=0)
        response = False
        ser.write("AT\n")
        response = ser.read()
        if response:
            return True
        else: 
            return False
    except:
        return False 
    
def modem_toggle():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)

if __name__ == "__main__":
    if not check_modem():
       modem_toggle() 
       
