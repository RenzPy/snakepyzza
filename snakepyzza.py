import pygame 

# SNAKEPYZZA PIZZA EATING SNAKE GAME
# FOLLOWING TUTORIAL https://www.edureka.co/blog/snake-game-with-pygame/#building
# README.md FOR MORE INFORMATION
# RENZPY PROJECT 2023



# CREATING GAME WINDOW
pygame.init()
dis = pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('𝘚𝘯𝘢𝘬𝘦𝘗𝘺𝘻𝘻𝘢 - 𝘳𝘦𝘯𝘻𝘱𝘺 ')
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event) #prints out all the actions that take place on the screen


    
pygame.quit
quit()