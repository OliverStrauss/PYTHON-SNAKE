xpos = 0
ypos = 0
size = 0
import pygame


class pee():

    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.size = 20

    def getX(self):
        return xpos

    def getY(self):
        return ypos

    def getSize(self):
        return size

    def getRect(self):
        return pygame.Rect(self.xpos, ypos, size, size)

    def move(self, up, down, left, right):
        if (up):
            self.ypos += 1
        elif (down):
            self.ypos += 1
        elif (left):
            self.xpos += 1
        elif (right):
            self.xpos += 1
