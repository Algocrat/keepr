from __future__ import print_function
from flask import Flask, request
from flask_restful import Resource, Api
import RPi.GPIO as GPIO
import time
import math
import xbox

# Instantiate the controller
joy = xbox.Joystick()
GPIO.setmode(GPIO.BOARD)

#execute code
def movemotor(dirpin, steppin, enablepin, direction, pulses):  # param must match uri identifier

        GPIO.setwarnings(False)
        GPIO.setup(dirpin, GPIO.OUT)
        GPIO.setup(steppin, GPIO.OUT)
        GPIO.setup(enablepin, GPIO.OUT)

        FastSpeed = 0.0004 #Change this depends on your stepper motor
        LowSpeed = 0.0004
        Speed = FastSpeed

        GPIO.output(enablepin, GPIO.HIGH)
        
        if direction == 1:
            for i in range (pulses):
                GPIO.output(dirpin, 0)
                GPIO.output(steppin, 0)
                time.sleep(LowSpeed)
                GPIO.output(steppin, 1)
                time.sleep(LowSpeed)
                return str(direction)+' direction for '+str(pulses)+' pulses.'
        elif direction == 0:
            for i in range (pulses):
                GPIO.output(dirpin, 1)
                GPIO.output(steppin, 0)
                time.sleep(LowSpeed)
                GPIO.output(steppin, 1)
                time.sleep(LowSpeed)
                return str(direction)+' direction for '+str(pulses)+' pulses.'



# Show various axis and button states until Back button is pressed
print("Xbox controller sample: Press Back button to exit")
while not joy.Back():
    if joy.leftX()>0:
        msg = movemotor(24, 26, 32, 1, 100)
        print(msg)
    elif joy.leftX()<0:
        msg = movemotor(24, 26, 32, 0, 100)
        print(msg)

    if joy.leftY()>0:
        msg = movemotor(33, 35, 37, 0, 100)
        print(msg)
    elif joy.leftY()<0:
        msg = movemotor(33, 35, 37, 1, 100)
        print(msg)

    if joy.rightX()>0:
        msg = movemotor(23, 29, 31, 1, 100)
        print(msg)
    elif joy.rightX()<0: 
        msg = movemotor(23, 29, 31, 0, 100)       
        print(msg)

    if joy.rightY()>0:
	msg = movemotor(36, 38, 40, 1, 100)
        print(msg)
    elif joy.rightY()<0:        
	msg = movemotor(36, 38, 40, 0, 100)
        print(msg)

    if joy.rightTrigger():
        msg = movemotor(11, 13, 15, 0, 100)
        print(msg)
    elif joy.leftTrigger():
        msg = movemotor(11, 13, 15, 1, 100)
        print(msg)

    if joy.rightBumper():
        msg = movemotor(8, 10, 12, 1, 100)
        print(msg)
    elif joy.leftBumper():
        msg = movemotor(8, 10, 12, 0, 100)
        print(msg)

joy.close()





