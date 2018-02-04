import RPi.GPIO as GPIO
from time import sleep
import json

with open('AHU06 Heating Coil.json') as json_data:
    t = json.load(json_data)
    name = t['name']
    values = t['values']
        
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
                sleep(4)
            else :
                GPIO.output(stepPin, GPIO.HIGH)
                sleep(4)
except KeyboardInterrupt:
    print("Stop")
GPIO.cleanup()