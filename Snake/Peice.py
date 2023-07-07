import pygame


class pee():
    xpos = 0
    ypos = 0
    size = 0

    def __init__(self, x, y):
        self.xpos = int(x)
        self.ypos = int(y)
        self.size = 40

    def moveCheck(self, pos, isdown):
        distance = 40
        if int(pos) > (800 - self.size) or int(pos) < (0):
            print(self, pos, isdown)
            print("you fucking suck")
            pygame.quit()

        return int(-distance) if isdown else int(distance)
    
    def get_pos(self):
        return self.xpos, self.ypos

    def set_pos(self, pos: tuple):
        self.xpos = pos[0]
        self.ypos = pos[1]

    def getSize(self):
        return self.size

    def getRect(self):
        return pygame.Rect(self.xpos, self.ypos, self.size, self.size)

    def move(self, list):
        if list[0]:
            self.ypos += self.moveCheck(self.ypos, True)
        elif list[1]:
            self.ypos += self.moveCheck(self.ypos, False)
        elif list[2]:
            self.xpos += self.moveCheck(self.xpos, True)
        elif list[3]:
            self.xpos += self.moveCheck(self.xpos, False)

    def __repr__(self):
        return f"{self.xpos} {self.ypos} {self.size}"
