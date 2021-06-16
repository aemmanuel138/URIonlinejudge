#FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('oceueoinferno.mp3')
pygame.mixer.music.play()
pygame.event.wait()