import pygame
from Peice import pee

# Initialize Pygame
pygame.init()

# Set up the display
running = True
global width
global height
width = 400
height = 400



window = pygame.display.set_mode((width, height))
snake_speed = 1


pygame.display.set_caption("Snake")
background_color = (46, 153, 37)  # White color
snake_color = (0, 0, 0)  # White color


class snake():
    
    def moveSnake(snake_list):
        for p in snake_list:
            p.move(up,down,left,right)
        
            


    def printSnake(snake_list):
        for p in snake_list:
            pygame.draw.rect(window,snake_color,p.getRect())


head = pee(width/2, height/2)
snake_list =[head]
while running:
    left = False
    right = False
    up = False
    down = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dx = 0
    dy = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        up = True  
    elif keys[pygame.K_s]:
        down= True
    elif keys[pygame.K_a]:
        left = True
    elif keys[pygame.K_d]:
        right = True
   
    window.fill(background_color)
    snake.moveSnake(snake_list)
    snake.printSnake(snake_list)

    pygame.display.update()
    # Quit Pygame
pygame.quit()
