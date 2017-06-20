'''
modemToggle.py

Description:
    This program turns on the Itead RPI GSM Shield by toggling the GPIO 17 pin.

mru: Ivraj Seerha 6/16/17
'''
import RPi.GPIO as GPIO
import time

def modemToggle():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(17, GPIO.LOW)

if __name__ == "__main__":
    modemToggle()

