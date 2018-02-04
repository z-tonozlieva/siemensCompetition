import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
stepPin = 11
dir = 13
GPIO.setup(stepPin, GPIO.OUT)
GPIO.setup(dir, GPIO.LOW)

try:
    while True:
        GPIO.output(stepPin, GPIO.LOW)
        sleep(0.00001)
        GPIO.output(stepPin, GPIO.HIGH)
        sleep(0.01)
except KeyboardInterrupt:
    print("Stop")
GPIO.cleanup()