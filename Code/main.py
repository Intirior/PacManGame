from limits2 import WallLimits
from Pellets import *
from Ghosts import *
from Constants import *
from WallsList import walls
from PacClass import *

MusicFiles['opening_song'].play()

pygame.mixer.music.play(-1)

limit = WallLimits(wallsList = walls , speed = speed)

ghostsList=[ghostClass(x = 315, y = 282,decision= 'up',speed = speed,WallList=walls) for _ in range(4)]

pygame.time.set_timer(pygame.USEREVENT,8000)

pygame.time.set_timer(pygame.USEREVENT+1,180) # the timer to change the pac's image at each time

PAC=pacManClass(x = 320,y = 320,speed = speed,window = win,pacManImage = pacManImage,WallList=walls)

run=True
while run:
    pacRect = pygame.Rect((PAC.x,PAC.y),(22,22)) # create pygame Rect Typeof the pacman's shape

    pygame.time.delay(6)

    win.fill((0, 0, 0))
    win.blit(bg, ((winSize[0] - bg.get_size()[0]) / 2, 0))
    blitPellet(win, dot, Bigdot)
    eatBigPellets((PAC.x, PAC.y))

    pygame.draw.line(win,(255,0,0),(310,253),(340,253),2)

    for i in range(lives):
        win.blit(liveHeart, (100+(i*35), 10))

    if PAC.x<=leftTeleportPos[0]  and leftTeleportPos[1]+10>=PAC.y>=leftTeleportPos[1] and PAC.pacDirection=='LEFT':
        PAC.x=rightTeleportPos[0]

    elif PAC.x>=rightTeleportPos[0] and rightTeleportPos[1]+10>=PAC.y>=rightTeleportPos[1] and PAC.pacDirection=='RIGHT':
        PAC.x=leftTeleportPos[0]


    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            quit()
        if len(ghostsList)<=MaxGhostAmount:
            if event.type==pygame.USEREVENT:
                ghostsList.append(ghostClass(315, 280, 'up',speed,WallList=walls))

        if event.type == pygame.USEREVENT+1:
            PAC.walkCount += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                PAC.pacDirection = 'RIGHT'
                walkCount = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                PAC.pacDirection = 'LEFT'
                walkCount = 2
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                PAC.pacDirection = 'UP'
                walkCount = 4
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                PAC.pacDirection = 'DOWN'
                walkCount = 6

    PAC.move()

    if eatBigPellets((PAC.x, PAC.y))=='Transform':
        MusicFiles['eating_cherry'].play()
        transformation=True

    for ghosT in ghostsList:

        if ghosT.x==315 and ghosT.y==282:
            ghosT.decision='up'

        ghosT.decideAndMove()

        if ghosT.x <= leftTeleportPos[0] and leftTeleportPos[1] + 10 >= ghosT.y >= leftTeleportPos[1] and ghosT.decision == 'left':
            ghosT.x = rightTeleportPos[0]

        elif ghosT.x >= rightTeleportPos[0] and rightTeleportPos[1] + 10 >= ghosT.y >= rightTeleportPos[1] and ghosT.decision == 'right':
            ghosT.x = leftTeleportPos[0]

        if transformation and timer<6000:
            timer+=1
            ghost=blueGhost

            if abs(PAC.x - ghosT.x) <= 10 and abs(PAC.y - ghosT.y) <= 22:
                MusicFiles['eating_ghost'].play()
                ghosT.x=330
                ghosT.y=280
                ghosT.decision='up'

        else:
            if abs(PAC.x - ghosT.x) <= 10 and abs(PAC.y - ghosT.y) <= 22:
                if lives != 1:
                    MusicFiles['pacmandies'].play()
                lives -= 1
                PAC.x = 320
                PAC.y = 320
            ghost = pygame.image.load('D:\pythonP\my_project\PacMan\photos/z orange_0.png').convert_alpha()
            timer = 0
            transformation = False
        win.blit(ghost, (ghosT.x, ghosT.y))

    if eatPellets((PAC.x,PAC.y),win):
        score2+=1

    if lives<=0:
        MusicFiles['gameover'].play()
        print('you lost')
        pygame.time.delay(3100)
        quit()

    if score2==88:
        MusicFiles['youwin'].play()
        print('you won')
        pygame.time.delay(6100)
        quit()

    pygame.display.update()