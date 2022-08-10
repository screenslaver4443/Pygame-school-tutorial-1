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

# Defining Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 255, 255)

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
            print("User clicked the mouse")
    ##### Game logic #####

    ##### Drawing code #####
    screen.fill(WHITE)  # Reset the screen

    # pygame.draw.line(screen, TEAL, [0, 0], [100, 100], 5)  # Early Line
    # for i in range(0, 5):  # five parralel lines
    #     pygame.draw.line(screen, RED, [0, (i*10)], [100, (100+(i*10))])

    # for i in range(0, 4):  # 4 +'s
    #     pygame.draw.line(screen, RED, [(i*10), 100], (i*10+10, 100))
    #     pygame.draw.line(screen, RED, [(i*10+5), 95], (i*10+5, 105))

    for i in range(0,4):
        pygame.draw.rect(screen, BLACK, [20+(i*10), 20+(i*10), (250-(i*10)), (250-(i*10))], 2)    
    pygame.display.flip()  # Update the screen with changes

    clock.tick(60)  # Limit to 60 frames per second
pygame.quit()
