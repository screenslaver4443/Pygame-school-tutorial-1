#Pygame Tutorial 1
#main.py
#Nikolai Pesudovs
#5th August 2022
#A basic pygametutorial

#Imports Pygame
from ast import While
import pygame

#Defining Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 255, 255)

#Window Settings
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Betwix Yall")

#Runs the game
pygame.init()

#Loop to keep game running
while True:
    pygame.display.update()