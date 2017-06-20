'''
checkModem.py

Description:
    This program uses serial to check whether or not the SIM800 modem is on
'''
import serial 
import time

def checkModem():
    print("Checking modem")
    ser = serial.Serial ('/dev/serial0', 115200, timeout=0)
    response = False
    ser.write("AT\n")
    time.sleep(1)
    response= ser.read()
    if response:
        print("Modem is ON")
    else:
        print("Modem is OFF")

if __name__ == "__main__":
    checkModem()
