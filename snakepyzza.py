# IMPORTING LIBRARIES
import pygame
import time
import random

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

# PIZZA RELATED
pizza_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
pizza_spawn = True


# DISPLAY SCORE FUNCTION
def show_score(choice, color, font, size):
   
    # creating font object score_font 
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('PyzzaScore™: ' + str(score), True, color)
     
    # create a rectangular object for the 
    # text surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)


# GAME OVER
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('PyzzaScore™: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)

    # Display a "Press any key to quit" message
    press_key_font = pygame.font.SysFont('times new roman', 30)
    press_key_surface = press_key_font.render('Press any key to quit', True, white)
    press_key_rect = press_key_surface.get_rect()
    press_key_rect.midtop = (window_x / 2, window_y / 2)
    game_window.blit(press_key_surface, press_key_rect)

    pygame.display.flip()

    game_over = True  # Set the game_over flag to True

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                quit()

# Main Function
running = True
while running:
    
    # CLOSE THE GAME ON 'X' WINDOW CLICK
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Set the running flag to False to exit the game loop when 'X' is clicked

        # HANDLING KEY EVENTS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # DISABLE MOVE IN TWO DIRECTIONS IF TWO KEYS ARE PRESSED
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'


    # MOVING SNAKE
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # SNAKE BODY GROWING MECHANISM 
    # PIZZA-SNAKE COLLISION = +10 SCORE
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == pizza_position[0] and snake_position[1] == pizza_position[1]:
        score += 10
        pizza_spawn = False
    else:
        snake_body.pop()
         
    if not pizza_spawn:
        pizza_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
         
    pizza_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(game_window, white, pygame.Rect(
      pizza_position[0], pizza_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
     
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
     
    # displaying score continuously
    show_score(1, white, 'times new roman', 20)
     
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)