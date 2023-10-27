# IMPORTING LIBRARIES
import pygame
import time
import random
import skpy

# SNAKEPYZZA PIZZA EATING SNAKE GAME
# FOLLOWING TUTORIAL https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
# README.md FOR MORE INFORMATION
# RENZPY PROJECT 2023


# INITIAL SCORE
score = 0
# FPS controller
fps = pygame.time.Clock()

# INITIALISE GAME
pygame.init()

# WINDOW SIZE
window_x = 720
window_y = 480

# INITIALISE GAME WINDOW
pygame.display.set_caption("𝘚𝘯𝘢𝘬𝘦𝘗𝘺𝘻𝘻𝘢 - 𝘳𝘦𝘯𝘻𝘱𝘺") # window title
game_window = pygame.display.set_mode((window_x, window_y))

# DEFINING COLORS
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# SNAKE RELATED
snake_speed = 15
direction = 'RIGHT' # SETTING DEFAULT SNAKE POSITION
change_to = direction # TO THE RIGHT
snake_position = [100, 50]
snake_body = [  [100, 50], # DEFINING FIRST 4 BLOCKS OF SNAKE BODY
                [90, 50],
                [80, 50],
                [70,50]
            ]

# FRUIT RELATED
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

