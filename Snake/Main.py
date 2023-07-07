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
clock = pygame.time.Clock()
snake_speed = 1

pygame.display.set_caption("Snake")
background_color = (46, 153, 37)  # White color
snake_color = (0, 0, 0)  # BAKCKL;S[] color

up = False
down = False
left = False
right = False

directions = [up, down, left, right]

class food():
    eaten = False
    fxpos = 0
    fypos = 0

    def __init__(self):
        self.fxpos = random.randint(0, 20) * 40
        self.fypos = random.randint(0, 20) * 40

    def getfx(self):
        return self.fxpos

    def getfy(self):
        return self.fypos

    def printfood(self):
        if self.eaten:
            red = (240, 5, 5)
            pygame.draw.rect(window, red, pygame.Rect(self.fxpos, self.fypos, 40, 40))


class snake():

    def moveSnake(snake_list):
        for p in snake_list:
            p.move(directions)

    def printSnake(snake_list):
        for p in snake_list:
            pygame.draw.rect(window, snake_color, p.getRect())


head = pee(width / 2, height / 2)
snake_list = [head]


def change_direction(direction_index):
    global directions

    for direction in directions:
        index = directions.index(direction)
        if index != direction_index:
            directions[index] = False

    directions[direction_index] = True


while running:
    apple = food()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_direction(0)
            if event.key == pygame.K_s:
                change_direction(1)
            if event.key == pygame.K_a:
                change_direction(2)
            if event.key == pygame.K_d:
                change_direction(3)

    dx = 0
    dy = 0

    keys = pygame.key.get_pressed()

    window.fill(background_color)
    dist = 40
    # if(head.getX == food.getfx or head.getY == food.getfy):

    apple.printfood()

    snake.moveSnake(snake_list)
    snake.printSnake(snake_list)

    pygame.display.update()
    clock.tick(7)
    # Quit Pygame
pygame.quit()
