# IMPORTING LIBRARIES
import pygame
import time
import random

# SNAKEPYZZA PIZZA EATING SNAKE GAME
# FOLLOWING TUTORIAL https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
# README.md FOR MORE INFORMATION
# RENZPY PROJECT 2023

snake_speed = 15

# WINDOW SIZE
window_x = 720
window_y = 480

# DEFINING COLORS
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# INITIALISE GAME
pygame.init()

# INITIALISE GAME WINDOW
pygame.display.set_caption("𝘚𝘯𝘢𝘬𝘦𝘗𝘺𝘻𝘻𝘢 - 𝘳𝘦𝘯𝘻𝘱𝘺") # window title
game_window = pygame.display.set_mode((window_x,window_y))

# FPS controller
fps = pygame.time.Clock()
