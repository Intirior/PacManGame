class WallLimits:
    def __init__(self,wallsList,speed):
        self.wallsList = wallsList
        self.speed = speed

    def RightMovment(self,x,y):
        for line in self.wallsList:
            for y1 in range(y,y+23):
                if (x+23==line.x and  line.y+line.height > y1 > line.y):
                    return False
        return True

    def LeftMovment(self,x,y):
        for line in self.wallsList:
            for y1 in range(y, y + 23):
                if (x == line.x + line.width and line.y + line.height > y1 > line.y):
                    return False
        return True

    def DownMovement(self,x,y):
        if (y  == 230 and 340 >= x > 300): # the red line at the ghosts' start point
            return 0
        for line in self.wallsList:
            for x1 in range(x, x + 23):
                if (y+22==line.y and  line.x+line.width>x1>line.x):
                    return False
        return True

    def UpMovement(self,x,y):
        for line in self.wallsList:
            for x1 in range(x, x + 23):
                if (y==line.y+line.height and  line.x+line.width>x1>line.x):
                    return False
        return True

