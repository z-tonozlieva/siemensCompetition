import pygame
pygame.mixer.init()
pygame.mixer.music.load("s1.wav")
pygame.mixer.music.set_pos(0.9)
pygame.mixer.music.play(-1)
while pygame.mixer.music.get_busy() == True:
    continue