import time
import json
import pygame

with open('5s res sensor_id=BMS-L1O14S33&start=2017-03-20T00_00_00&end=2017-03-20T23_59_59.json') as json_data:
    d = json.load(json_data)
    data = d['id']
    name = d['name']
    type = d['type']
    values = d['values']
    print(name)
    print(type)
    print("---------")

with open('AHU06 Heating Coil.json') as json_data:
    t = json.load(json_data)
    name = t['name']
    temperatures = t['values']

GPIO.setmode(GPIO.BOARD)
stepPin = 11
dir = 13
GPIO.setup(stepPin, GPIO.OUT)
GPIO.setup(dir, GPIO.LOW)

firstPart = False
secondPart = False
thirdPart = False
fourthPart = False
fifthPart = False
sixthPart = False


if __name__ == "__main__":
    music_file1 = "1-Morning-Edvard-Grieg.wav"
    music_file2 = "2-Erik-Satie-Gymnop_die-No_1.wav"
    music_file3 = "3-Camille-Saint-Sa_ns-Danse-Macabre.wav"
    music_file4 = "4-Richard-Wagner-Ride-Of-The-Valkyries.wav"
    music_file5 = "5-Mozart-The-Marriage-of-Figaro.wav"
    music_file6 = "6-Grieg-In-the-Hall-of-the-Mountain-King.wav"

# set up the mixer
freq = 44100
bitsize = -16
channels = 6
buffer = 2048
pygame.mixer.init(freq, bitsize, channels, buffer)

pygame.mixer.init()

# Create sound object for each Audio
myAudio1 = pygame.mixer.Sound(music_file1)
myAudio2 = pygame.mixer.Sound(music_file2)
myAudio3 = pygame.mixer.Sound(music_file3)
myAudio4 = pygame.mixer.Sound(music_file4)
myAudio5 = pygame.mixer.Sound(music_file5)
myAudio6 = pygame.mixer.Sound(music_file6)

# Create a Channel for each Audio
myChannel1 = pygame.mixer.Channel(1)
myChannel2 = pygame.mixer.Channel(2)
myChannel3 = pygame.mixer.Channel(3)
myChannel4 = pygame.mixer.Channel(4)
myChannel5 = pygame.mixer.Channel(5)
myChannel6 = pygame.mixer.Channel(6)

try:
    while True:
        for value in values and temperature in temperatures:
            if (float(temperature['value']) < 500.0):
                GPIO.output(stepPin, GPIO.LOW)
            if (float(temperature['value']) >= 500.0):
                GPIO.output(stepPin, GPIO.HIGH)
            if float(value['value']) <= 400.0:
                myChannel2.stop()
                secondPart = False
                myChannel3.stop()
                thirdPart = False
                myChannel4.stop()
                fourthPart = False
                myChannel5.stop()
                fifthPart = False
                myChannel6.stop()
                sixthPart = False
                if not firstPart or not myChannel1.get_busy():
                    firstPart = True
                    myChannel1.play(myAudio1)

            elif (float(value['value']) > 400.0) and (float(value['value']) <= 500.0):
                myChannel1.stop()
                firstPart = False
                myChannel3.stop()
                thirdPart = False
                myChannel4.stop()
                fourthPart = False
                myChannel5.stop()
                fifthPart = False
                myChannel6.stop()
                sixthPart = False
                if not secondPart or not myChannel2.get_busy():
                    secondPart = True
                    myChannel2.play(myAudio2)

            elif (float(value['value']) > 500.0) and (float(value['value']) <= 600.0):
                myChannel1.stop()
                firstPart = False
                myChannel2.stop()
                secondPart = False
                myChannel4.stop()
                fourthPart = False
                myChannel5.stop()
                fifthPart = False
                myChannel6.stop()
                sixthPart = False
                if not thirdPart or not myChannel3.get_busy():
                    thirdPart = True
                    myChannel3.play(myAudio3)

            elif (float(value['value']) > 600.0) and (float(value['value']) <= 700.0):
                myChannel1.stop()
                firstPart = False
                myChannel2.stop()
                secondPart = False
                myChannel3.stop()
                thirdPart = False
                myChannel5.stop()
                fifthPart = False
                myChannel6.stop()
                sixthPart = False
                if not fourthPart or not myChannel4.get_busy():
                    fourthPart = True
                    myChannel4.play(myAudio4)

            elif (float(value['value']) > 700.0) and (float(value['value']) <= 800.0):
                myChannel1.stop()
                firstPart = False
                myChannel2.stop()
                secondPart = False
                myChannel3.stop()
                thirdPart = False
                myChannel4.stop()
                fourthPart = False
                myChannel6.stop()
                sixthPart = False
                if not fifthPart or not myChannel5.get_busy():
                    fifthPart = True
                    myChannel5.play(myAudio5)

            else:
                myChannel1.stop()
                firstPart = False
                myChannel2.stop()
                secondPart = False
                myChannel3.stop()
                thirdPart = False
                myChannel4.stop()
                fourthPart = False
                myChannel5.stop()
                fifthPart = False
                if not sixthPart or not myChannel6.get_busy():
                    sixthPart = True
                    myChannel6.play(myAudio6)

            print(value['value'])
            time.sleep(5)

except KeyboardInterrupt:
    print("Stop")
GPIO.cleanup()