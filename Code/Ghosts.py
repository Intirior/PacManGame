import random
from limits2 import WallLimits

class ghostClass(WallLimits):
    ghostDirection = ['right', 'left', 'up', 'down']
    def __init__(self,x,y,decision,speed,WallList):
        super().__init__(WallList, speed)
        self.x=x
        self.y=y
        self.decision=decision
        self.speed=speed



    def decideAndMove(self):
        if self.decision == 'right' and self.RightMovment(self.x,self.y):
            self.x += self.speed
        elif self.decision == 'left' and self.LeftMovment(self.x,self.y):
            self.x -= self.speed
        elif self.decision == 'down'and self.DownMovement(self.x,self.y):
            self.y += self.speed
        elif self.decision == 'up' and self.UpMovement(self.x,self.y):
            self.y -= self.speed
        else:
            self.decision = random.choice(self.ghostDirection)