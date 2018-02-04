import time
import json
import pygame

with open('5s res sensor_id=BMS-L1O14S33&start=2017-03-20T00_00_00&end=2017-03-20T23_59_59.json') as json_data:
    d = json.load(json_data)
    data = d['id']
    name = d['name']
    values = d['values']

    firstPart = False
    secondPart = False
    thirdPart = False

def checkifComplete(channel):
    while channel.get_busy():  #Check if Channel is busy
        pygame.time.wait(800)  #  wait in ms
    channel.stop()             #Stop channel

if __name__ == "__main__":
    music_file1 = "1-Morning-Edvard-Grieg.wav"
    music_file2 = "2-Erik-Satie-Gymnop_die-No_1.wav"
    music_file3 = "3-Camille-Saint-Sa_ns-Danse-Macabre.wav"
    music_file4 = "4-Richard-Wagner-Ride-Of-The-Valkyries.wav"
    music_file5 = "5-Mozart-The-Marriage-of-Figaro.wav"
    music_file6 = "6-Grieg-In-the-Hall-of-the-Mountain-King.wav"

# set up the mixer
freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 3  # 1 is mono, 2 is stereo
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
    if float(value['value']) <= 450.0:
        myChannel2.stop()
        secondPart = False
        myChannel3.stop()
        thirdPart = False
        if firstPart == False:
            firstPart = True
            myChannel1.play(myAudio1)
            checkifComplete(myChannel1)

    elif (float(value['value']) > 450.0) and (float(value['value']) < 600.0) :
        myChannel3.stop()
        thirdPart = False
        if (secondPart == False) :
            secondPart = True
            myChannel2.play(myAudio2)
            checkifComplete(myChannel2)

    else:
        if thirdPart == False :
            thirdPart = True
            myChannel3.play(myAudio3)
            checkifComplete(myChannel3)

    print(value['value'])
    time.sleep(5)

print("---------")
print(name)
