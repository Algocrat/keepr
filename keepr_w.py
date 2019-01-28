from flask import Flask, request
from flask_restful import Resource, Api
import RPi.GPIO as GPIO
import time
import math

# Instantiate the controller
joy = xbox.Joystick()
GPIO.setmode(GPIO.BOARD)

app = Flask(__name__)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)


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




class basemotor(Resource):
    '''
    Note: direction = 1 moves motor clockwise, and 0 will move counter-clockwise.
    
    Note: Base motor rotatates a complete circle - 360 degrees on 1600 pulses.
    
    curl http://192.168.86.199:80/basemotor/1/1600
    
    curl http://192.168.86.199:80/basemotor/0/1600
    '''
    def get(self, direction, pulses):  # param must match uri identifier
        LinearActuatorDir = 24
        LinearActuatorStep = 26
        LinearActuatorEnable = 32
		
        msg = movemotor(LinearActuatorDir, LinearActuatorStep, LinearActuatorEnable, direction, pulses)
        return 'basemotor ran in '+str(direction)+' direction for '+str(pulses)+' pulses.'

class shouldermotor(Resource):
    '''
    Note: direction = 1 moves motor clockwise, and 0 will move counter-clockwise.
    
    Note: shoulder motor rotatates a complete circle - 360 degrees on 1600 pulses.
    
    curl http://192.168.86.199:80/shouldermotor/1/1600
    
    curl http://192.168.86.199:80/shouldermotor/0/1600
    '''
    def get(self, direction, pulses):  # param must match uri identifier
        LinearActuatorDir = 33
        LinearActuatorStep = 35
        LinearActuatorEnable = 37

        msg = movemotor(LinearActuatorDir, LinearActuatorStep, LinearActuatorEnable, direction, pulses)

        return 'shouldermotor ran in '+str(direction)+' direction for '+str(pulses)+' pulses.'


class armmotor(Resource):
    '''
    Note: direction = 1 moves motor clockwise, and 0 will move counter-clockwise.
    
    Note: arm motor rotatates a complete circle - 360 degrees on 1600 pulses.
    
    curl http://192.168.86.199:80/armmotor/1/1600
    
    curl http://192.168.86.199:80/armmotor/0/1600
    '''
    def get(self, direction, pulses):  # param must match uri identifier
        LinearActuatorDir = 36
        LinearActuatorStep = 38
        LinearActuatorEnable = 40
        msg = movemotor(LinearActuatorDir, LinearActuatorStep, LinearActuatorEnable, direction, pulses)

        return 'armmotor ran in '+str(direction)+' direction for '+str(pulses)+' pulses.'

class forearmmotor(Resource):
    '''
    Note: direction = 1 moves motor clockwise, and 0 will move counter-clockwise.
    
    Note: forearm motor rotatates a complete circle - 360 degrees on 1600 pulses.
    
    curl http://192.168.86.199:80/forearmmotor/1/1600
    
    curl http://192.168.86.199:80/forearmmotor/0/1600
    '''
    def get(self, direction, pulses):  # param must match uri identifier
        LinearActuatorDir = 23
        LinearActuatorStep = 29
        LinearActuatorEnable = 31

        msg = movemotor(LinearActuatorDir, LinearActuatorStep, LinearActuatorEnable, direction, pulses)

        return 'forearmmotor ran in '+str(direction)+' direction for '+str(pulses)+' pulses.'

class wristmotor(Resource):
    '''
    Note: direction = 1 moves motor clockwise, and 0 will move counter-clockwise.
    
    Note: wrist motor rotatates a complete circle - 360 degrees on 1600 pulses.
    
    curl http://192.168.86.199:80/wristmotor/1/1600
    
    curl http://192.168.86.199:80/wristmotor/0/1600
    '''
    def get(self, direction, pulses):  # param must match uri identifier
        LinearActuatorDir = 11
        LinearActuatorStep = 13
        LinearActuatorEnable = 15
        msg = movemotor(LinearActuatorDir, LinearActuatorStep, LinearActuatorEnable, direction, pulses)
        return 'wristmotor ran in '+str(direction)+' direction for '+str(pulses)+' pulses.'

class forewristmotor(Resource):
    '''
    Note: direction = 1 moves motor clockwise, and 0 will move counter-clockwise.
    
    Note: forewrist motor rotatates a complete circle - 360 degrees on 1600 pulses.
    
    curl http://192.168.86.199:80/forewristmotor/1/1600
    
    curl http://192.168.86.199:80/forewristmotor/0/1600
    '''
    def get(self, direction, pulses):  # param must match uri identifier
        LinearActuatorDir = 8
        LinearActuatorStep = 10
        LinearActuatorEnable = 12

        msg = movemotor(LinearActuatorDir, LinearActuatorStep, LinearActuatorEnable, direction, pulses)

        return 'forewristmotor ran in '+str(direction)+' direction for '+str(pulses)+' pulses.'

class grippermotor(Resource):
    '''
    Note: direction = 1 moves motor clockwise, and 0 will move counter-clockwise.
    
    Note: gripper motor rotatates a complete circle - 360 degrees on 1600 degrees.
    
    curl http://192.168.86.199:80/grippermotor/1
    
    curl http://192.168.86.199:80/grippermotor/0
    '''
    def get(self, direction):  # param must match uri identifier
        if direction == 1:
            pwm.ChangeDutyCycle(2.5)
        elif direction == 0:
            pwm.ChangeDutyCycle(12.5)

        return 'grippermotor ran in '+str(direction)+' direction.'


api.add_resource(grippermotor, '/grippermotor/<int:direction>')  

api.add_resource(forewristmotor, '/forewristmotor/<int:direction>/<int:pulses>')  

api.add_resource(wristmotor, '/wristmotor/<int:direction>/<int:pulses>')  

api.add_resource(forearmmotor, '/forearmmotor/<int:direction>/<int:pulses>')  

api.add_resource(armmotor, '/armmotor/<int:direction>/<int:pulses>')  

api.add_resource(shouldermotor, '/shouldermotor/<int:direction>/<int:pulses>')  

api.add_resource(basemotor, '/basemotor/<int:direction>/<int:pulses>')  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


