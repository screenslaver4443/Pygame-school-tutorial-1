# Pygame Tutorial 1
# main.py
# Nikolai Pesudovs
# 5th August 2022
# A basic pygametutorial

# Imports Pygame
from ast import While
import pygame

# Imports Random
import random
# Imports math
import math 

# Defining Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 255, 255)
YELLOW = (255, 255, 0)

# Window Settings
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Betwix Yall")

# Runs the game
pygame.init()

# Loop to keep game running
done = False  # Variable for closing game
clock = pygame.time.Clock()  # FPS counter
while not done:  # Main game loop
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Closes Game
            print("User asked to quit")
            done = True
        if event.type == pygame.KEYDOWN:  # logs when person clicks key
            print('User pressed a key')
        if event.type == pygame.KEYUP:
            print('User let go of a key')
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            print("User clicked the mouse at", mousepos)
    ##### Game logic #####

    ##### Drawing code #####
    screen.fill(WHITE)  # Reset the screen

    # pygame.draw.line(screen, TEAL, [0, 0], [100, 100], 5)  # Early Line
    # for i in range(0, 5):  # five parralel lines
    #     pygame.draw.line(screen, RED, [0, (i*10)], [100, (100+(i*10))])

    # for i in range(0, 4):  # 4 +'s
    #     pygame.draw.line(screen, RED, [(i*10), 100], (i*10+10, 100))
    #     pygame.draw.line(screen, RED, [(i*10+5), 95], (i*10+5, 105))

    # for i in range(0,4): #Draws Rectangle
    #     pygame.draw.rect(screen, BLACK, [20+(i*10), 20+(i*10), (250-(i*20)), (250-(i*20))], 2)    
    
    ##Easy Olympic rings##
    # pygame.draw.ellipse(screen, BLUE, [100, 100, 200, 200], 10) #Blue Ring
    # pygame.draw.ellipse(screen, BLACK, [310, 100, 200, 200], 10) #Black Ring
    # pygame.draw.ellipse(screen, RED, [520, 100, 200, 200], 10) #Red Ring
    # pygame.draw.ellipse(screen, YELLOW, [205, 200, 200, 200], 10) #Yellow Ring
    # pygame.draw.ellipse(screen, GREEN, [415, 200, 200, 200], 10) #Green Ring
    
    # ## Pacman ##
    # pygame.draw.arc(screen, YELLOW, [100, 100, 400, 400], math.radians(35), math.radians(325), 10)
    # pygame.draw.line(screen, YELLOW, [462, 190], [300, 300], 10)
    # pygame.draw.line(screen, YELLOW, [462, 415], [300, 300], 10)
    
    # ## Crazy Shape ##
    # pygame.draw.polygon(screen, BLACK, [(0,600), (230, 80), (100, 23), (420, 69), (89, 400)], 100 )
    
    # ## arrow ##
    # pygame.draw.polygon(screen, BLACK, [(0,400), (200, 200), (400, 400), (200, 100), (0, 400)], 10 )
    
    pygame.display.flip()  # Update the screen with changes

    clock.tick(60)  # Limit to 60 frames per second
pygame.quit()
