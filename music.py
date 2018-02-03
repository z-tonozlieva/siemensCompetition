    music_file1 = "sounds/bass.wav"
    music_file2 = "sounds/drums.wav"
    music_file3 = "sounds/guitar.wav"


    #set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get right sound)
    pygame.mixer.init(freq, bitsize, channels, buffer)

    pygame.mixer.init() #Initialize Mixer

    #Create sound object for each Audio
    myAudio1 = pygame.mixer.Sound(music_file1)
    myAudio2 = pygame.mixer.Sound(music_file2)

    #Create a Channel for each Audio
    myChannel1 = pygame.mixer.Channel(1)
    myChannel2 = pygame.mixer.Channel(2)

    #Add Audio to  first channel
    myAudio1.set_volume(0.8) # Reduce volume of first audio to 80%
    print "Playing audio : ", music_file1 
    myChannel1.play(myAudio1)
    checkifComplete(myChannel1) #Check if Audio1 complete

    #Add Audio to second channel
    myAudio2.set_volume(0.6)  
    print "Playing audio : ", music_file2
    myChannel2.play(myAudio2)
    checkifComplete(myChannel2)