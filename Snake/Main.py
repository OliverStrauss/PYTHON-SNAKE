import pygame
import random
from Peice import pee
import sys

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
    def __init__(self):
        self.fxpos = random.randint(1, 19) * 40
        self.fypos = random.randint(1, 19) * 40
        self.eaten = False

    def getfx(self):
        return self.fxpos

    def seteaten(self):
        print("I have been eaten T_T")
        self.eaten = True

    def getfy(self):
        return self.fypos

    def printfood(self):
        if not self.eaten:
            red = (240, 5, 5)
            pygame.draw.rect(window, red, pygame.Rect(self.fxpos, self.fypos, 40, 40))
        if self.eaten:
            self.respawn()

    def respawn(self):
        self.__init__()

    def __repr__(self):
        return f"{self.fxpos} {self.fypos}"


class Snake():
    def __init__(self):
        self.head = pee(width / 2, height / 2)
        self.old_placements = []
        self.body = []

    def moveSnake(self):
        self.head.move(directions)
        self.old_placements.append(self.head.get_pos())
        self.check_size()
        counter = 0
        for piece in self.body:
            piece.set_pos(self.old_placements[counter])
            counter += 1
            if self.head.get_pos() == piece.get_pos():
                pygame.quit()
    
    def check_size(self):
        print(self.old_placements)
        if len(self.old_placements) > len(self.body) + 1:
            self.old_placements.pop(0)

    def printSnake(self):
        pygame.draw.rect(window, snake_color, self.head.getRect())
        for piece in self.body:
            pygame.draw.rect(window, snake_color, piece.getRect())

    def add_piece(self):
        self.body.append(pee(0, 0))


snake = Snake()


def change_direction(direction_index):
    global directions

    for direction in directions:
        index = directions.index(direction)
        if index != direction_index:
            directions[index] = False

    directions[direction_index] = True


apple = food()
while running:
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
            if event.key == pygame.K_SPACE:
                print(snake.head)
                print(apple)

    dx = 0
    dy = 0

    keys = pygame.key.get_pressed()

    window.fill(background_color)
    dist = 40

    if (snake.head.xpos == apple.getfx() and snake.head.ypos == apple.getfy()):
        apple.seteaten()
        snake.add_piece()

    apple.printfood()

    snake.moveSnake()
    snake.printSnake()

    pygame.display.update()
    clock.tick(7)
    # Quit Pygame
pygame.quit()
