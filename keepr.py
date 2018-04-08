from flask import Flask, request
from flask_restful import Resource, Api
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #read the pin as board instead of BCM pin


app = Flask(__name__)
api = Api(app)  # api is a collection of objects, where each object contains a specific functionality (GET, POST, etc)


class basemotor(Resource):
    '''
    Note: direction = 1 moves motor clockwise, and 0 will move counter-clockwise.
    
    Note: Base motor rotatates a complete circle - 360 degrees on 1600 pulses.
    
    curl http://192.168.86.199:80/basemotor/1/1600
    
    curl http://192.168.86.199:80/basemotor/0/1600
    '''
    def get(self, direction, pulses):  # param must match uri identifier
        LinearActuatorDir = 33
        LinearActuatorStepPin = 35
        LinearActuatorEnable = 36

        GPIO.setwarnings(False)
        GPIO.setup(LinearActuatorDir, GPIO.OUT)
        GPIO.setup(LinearActuatorStepPin, GPIO.OUT)
        GPIO.setup(LinearActuatorEnable, GPIO.OUT)

        FastSpeed = 0.0004 #Change this depends on your stepper motor
        LowSpeed = 0.0004
        Speed = FastSpeed

        GPIO.output(LinearActuatorEnable, GPIO.HIGH)
        
        if direction == 1:
            for i in range (pulses):
                GPIO.output(LinearActuatorDir, 0)
                GPIO.output(LinearActuatorStepPin, 0)
                time.sleep(LowSpeed)
                GPIO.output(LinearActuatorStepPin, 1)
                time.sleep(LowSpeed)
                print ("Moving in direction 1")
        elif direction == 0:
            for i in range (pulses):
                GPIO.output(LinearActuatorDir, 1)
                GPIO.output(LinearActuatorStepPin, 0)
                time.sleep(LowSpeed)
                GPIO.output(LinearActuatorStepPin, 1)
                time.sleep(LowSpeed)
                print ("Moving in direction 0")

        return 'basemotor ran in '+str(direction)+' direction for '+str(pulses)+' pulses.'



api.add_resource(basemotor, '/basemotor/<int:direction>/<int:pulses>')  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
