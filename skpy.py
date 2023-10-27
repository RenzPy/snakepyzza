import pygame
import time

score = 0


# DEFINING COLORS
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# WINDOW SIZE
window_x = 720
window_y = 480

# INITIALISE GAME WINDOW
pygame.display.set_caption("𝘚𝘯𝘢𝘬𝘦𝘗𝘺𝘻𝘻𝘢 - 𝘳𝘦𝘯𝘻𝘱𝘺") # window title
game_window = pygame.display.set_mode((window_x, window_y))

# DISPLAY SCORE FUNCTION
def show_score(choice, color, font, size):
   
    # creating font object score_font 
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
     
    # create a rectangular object for the 
    # text surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)

# GAME OVER
def game_over():
# creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
     
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
     
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 2 seconds we will quit the 
    # program
    time.sleep(2)
     
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()