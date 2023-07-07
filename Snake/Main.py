import pygame
import random
from Peice import pee

# Initialize Pygame
pygame.init()

# Set up the display
running = True
global width
global height
width = 800
height = width

window = pygame.display.set_mode((width, height))
snake_speed = 1

pygame.display.set_caption("Snake")
background_color = (46, 153, 37)  # White color
snake_color = (0, 0, 0)  # BAKCKL;S[] color

class food():
    eaten = False
    fxpos =0
    fypos =0
    def __init__(self): 
        self.fxpos = random.randint(0,20)*40
        self.fypos = random.randint(0,20)*40
    
    def getfx(self):
     return self.fxpos
    
    def getfy(self):
        return self.fypos
    
    def printfood(self):
        if self.eaten:
            red =(240, 5, 5)
            pygame.draw.rect(window,red,pygame.Rect(self.fxpos,self.fypos,40,40))



class snake():

    def moveSnake(snake_list):
        for p in snake_list:
            p.move(up, down, left, right)

    def printSnake(snake_list):
        for p in snake_list:
            pygame.draw.rect(window, snake_color, p.getRect())

head = pee(width / 2, height / 2)
snake_list = [head]
while running:
    left = False
    right = False
    up = False
    down = False
    apple = food()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Key press detected for the SPACE key
                print("SPACE key pressed")


    dx = 0
    dy = 0


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        up = True
    elif keys[pygame.K_s]:
        down = True
    elif keys[pygame.K_a]:
        left = True
    elif keys[pygame.K_d]:
        right = True
   
    window.fill(background_color)
    dist = 40
    #if(head.getX == food.getfx or head.getY == food.getfy):

    snake.moveSnake(snake_list)
    snake.printSnake(snake_list)
    
    apple.printfood()

    pygame.display.update()
    # Quit Pygame
pygame.quit()
