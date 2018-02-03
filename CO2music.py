import time
import json
import pygame

with open('5s res sensor_id=BMS-L1O14S33&start=2017-03-20T00_00_00&end=2017-03-20T23_59_59.json') as json_data:
    d = json.load(json_data)
    data = d['id']
    name = d['name']
    values = d['values']
    print(id)

    max = 0.0
    min = 999.0
    sum = 0.0
    count = 0

    firstPart = False
    secondPart = False
    thirdPart = False


def checkifComplete(channel):
    while channel.get_busy():  # Check if Channel is busy
        pygame.time.wait(800)  # wait in ms


channel.stop()

music_file1 = "sounds/bass.wav"
music_file2 = "sounds/drums.wav"
music_file3 = "sounds/guitar.wav"

freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 2048  # number of samples (experiment to get right sound)
pygame.mixer.init(freq, bitsize, channels, buffer)

pygame.mixer.init()  # Initialize Mixer

# Create sound object for each Audio
myAudio1 = pygame.mixer.Sound(music_file1)
myAudio2 = pygame.mixer.Sound(music_file2)
myAudio3 = pygame.mixer.Sound(music_file3)

# Create a Channel for each Audio
myChannel1 = pygame.mixer.Channel(1)
myChannel2 = pygame.mixer.Channel(2)
myChannel3 = pygame.mixer.Channel(3)

for value in values:
    if (max < float(value['value'])): max = float(value['value'])
    if (min > float(value['value'])): min = float(value['value'])
    sum += float(value['value'])
    count += 1
    if float(value['value']) <= 450.0:
        if firstPart == False:
            firstPart = True
            myChannel1.play(myAudio1)
        myChannel2.stop()
        secondPart = False
        myChannel3.stop()
        thirdPart = False
    elif (float(value['value']) > 450.0) and (float(value['value']) < 600.0) :
        if (secondPart == False) :
            secondPart = True
            myChannel2.play(myAudio2)
        myChannel3.stop()
        thirdPart = False
    else:
        if thirdPart == False :
            thirdPart = True
            myChannel3.play(myAudio3)

    print(value['value'])
    time.sleep(10)

print("---------")
print(name)
print(d['type'])
print("max", max)
print("min", min)
print("average", float(sum / count))
