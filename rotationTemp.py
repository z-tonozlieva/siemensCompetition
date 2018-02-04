import RPi.GPIO as GPIO
from time import sleep
import json

with open('AHU06 Heating Coil.json') as json_data:
    d = json.load(json_data)
    name = d['name']
    values = d['values']
        
GPIO.setmode(GPIO.BOARD)
stepPin = 11
dir = 13
GPIO.setup(stepPin, GPIO.OUT)
GPIO.setup(dir, GPIO.LOW)

try:
    while True:
        for value in values:
            print(value['value'])
            if (float(value['value']) < 500.0) :
                GPIO.output(stepPin, GPIO.LOW)
                sleep(0.0005)
            else :
                GPIO.output(stepPin, GPIO.HIGH)
                sleep(0.01)
except KeyboardInterrupt:
    print("Stop")
GPIO.cleanup()