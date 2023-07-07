import pygame


class pee():
    xpos = 0
    ypos = 0
    size = 0

    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.size = 40

    def moveCheck(self, pos, isdown):
        distance = 20
        if int(pos) >= (800 - self.size) or int(pos) <= (0):
            pygame.quit()

        return -distance if isdown else distance

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    def getSize(self):
        return self.size

    def getRect(self):
        return pygame.Rect(self.xpos, self.ypos, self.size, self.size)

    def move(self, up, down, left, right):
        if (up):
            self.ypos += self.moveCheck(self.ypos, True)
        elif (down):
            self.ypos += self.moveCheck(self.ypos, False)
        elif (left):
            self.xpos += self.moveCheck(self.xpos, True)
        elif (right):
            self.xpos += self.moveCheck(self.xpos, False)

    
