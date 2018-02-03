import pygame
pygame.mixer.init()
pygame.mixer.music.load("s1.wav")
pygame.mixer.music.play(4.4)
while pygame.mixer.music.get_busy() == True:
    continue