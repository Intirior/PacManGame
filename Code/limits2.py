class WallLimits:
    def __init__(self,wallsList,speed):
        self.wallsList = wallsList
        self.speed = speed

    def RightMovment(self,x,y): # ,pacRect
        for _ in range(self.speed):
            for line in self.wallsList:
                for y1 in range(y,y+22):
                    if (x+22==line.x and  line.y+line.height > y1 > line.y):
                        return False
        '''for rect in walls:
            if rect.colliderect(pacRect):
                return False'''
        return True

    def LeftMovment(self,x,y): # ,pacRect
        for i in range(self.speed):
            for line in self.wallsList:
                for y1 in range(y, y + 22):
                    if (x == line.x + line.width and line.y + line.height > y1 > line.y):
                        return False
        '''for rect in walls:
            if rect.colliderect(pacRect):
                return False'''
        return True

    def DownMovement(self,x,y): # ,pacRect
        if (y  == 230 and 340 >= x > 300):
            return 0
        for i in range(self.speed):
            for line in self.wallsList:
                for x1 in range(x, x + 22):
                    if (y+22==line.y and  line.x+line.width>x1>line.x):
                        return False
        '''for rect in walls:
            if rect.colliderect(pacRect):
                return False'''
        return True

    def UpMovement(self,x,y): # ,pacRect
        for i in range(self.speed):
            for line in self.wallsList:
                for x1 in range(x, x + 22):
                    if (y==line.y+line.height and  line.x+line.width>x1>line.x):
                        return False
        '''for rect in walls:
            if rect.colliderect(pacRect):
                return False'''
        return True

