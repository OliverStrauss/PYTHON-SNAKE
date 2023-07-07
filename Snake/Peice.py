import pygame


class pee():
   xpos = 0
   ypos = 0
   size = 0


   def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.size = 40

   def moveCheck(pos,isdown):
       if pos>800 or pos<0 :
           return 0 
       
       if isdown:
            return -0.1
       else:
           return -.1




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
            self.ypos -= self.moveCheck(self.ypos,True)
        elif (down):
            self.ypos += 0.1
        elif (left):
            self.xpos -= 0.1
        elif (right):
            self.xpos += 0.1
