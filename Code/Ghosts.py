import random
from Constants import ghostDirection


class ghostClass:
    def __init__(self,x,y,decision,speed,WallListClass):
        self.x=x
        self.y=y
        self.decision=decision
        self.speed=speed
        self.WallListSelf = WallListClass

    def decideAndMove(self):
        if self.decision == 'right' and self.WallListSelf.RightMovment(self.x,self.y):
            self.x += self.speed
        elif self.decision == 'left' and self.WallListSelf.LeftMovment(self.x,self.y):
            self.x -= self.speed
        elif self.decision == 'down'and self.WallListSelf.DownMovement(self.x,self.y):
            self.y += self.speed
        elif self.decision == 'up' and self.WallListSelf.UpMovement(self.x,self.y):
            self.y -= self.speed
        else:
            self.decision = random.choice(ghostDirection)