import pygame
from limits2 import WallLimits

class pacManClass(WallLimits):
    def __init__(self,x,y,speed,window,pacManImage,WallList):
        super().__init__(WallList,speed)
        self.walkCount=0
        self.x=x
        self.y=y
        self.win=window
        self.pac=pacManImage


    def move(self,pacDirection,pacRect):
        if pacDirection == 'RIGHT' and self.RightMovment(self.x, self.y): # ,pacRect,pacDirection
            self.x += self.speed
            if self.walkCount >= 2:
                self.walkCount = 0
            self.win.blit(self.pac[self.walkCount], (self.x, self.y))

        elif pacDirection == 'LEFT' and self.LeftMovment(self.x, self.y): # ,pacRect,pacDirection
            self.x -= self.speed
            if self.walkCount >= 4:
                self.walkCount = 2
            self.win.blit(self.pac[self.walkCount], (self.x, self.y))

        elif pacDirection == 'UP' and self.UpMovement(self.x, self.y): # ,pacRect,pacDirection
            self.y -= self.speed
            if self.walkCount >= 6:
                self.walkCount = 4
            self.win.blit(self.pac[self.walkCount], (self.x, self.y))

        elif pacDirection == 'DOWN' and self.DownMovement(self.x, self.y): # ,pacRect,pacDirection
            self.y += self.speed
            if self.walkCount >= 8:
                self.walkCount = 6
            self.win.blit(self.pac[self.walkCount], (self.x, self.y))

        else:
            if pacDirection == 'RIGHT':
                self.win.blit(self.pac[0], (self.x, self.y))
            elif pacDirection == "LEFT":
                self.win.blit(self.pac[2], (self.x, self.y))
            elif pacDirection == "UP":
                self.win.blit(self.pac[4], (self.x, self.y))
            elif pacDirection == 'DOWN':
                self.win.blit(self.pac[6], (self.x, self.y))
            else:
                self.win.blit(self.pac[0], (self.x, self.y))