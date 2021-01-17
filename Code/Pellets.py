import pygame
from PelletsList import pellets,bigDots

pygame.font.init()

score=0
font=pygame.font.SysFont('Ariel',40)

def blitPellet(win,dot,bigDot):
    for i in pellets:
        win.blit(dot,i)
    for i in bigDots :
        win.blit(bigDot,i)

def eatPellets(pacPos,win):
    global score

    text = font.render(f"score {score*10}", 1, (255, 255, 255))

    win.blit(text, (510, 10))
    for i in pellets:
        if pacPos[0]<i[0]<pacPos[0]+22 and pacPos[1]<i[1]<pacPos[1]+22:
            score+=1
            pellets.remove(i)
            return True

def eatBigPellets(pacPos):
    for i in bigDots:
        if pacPos[0]<i[0]<pacPos[0]+22 and pacPos[1]<i[1]<pacPos[1]+22:
            bigDots.remove(i)
            return 'Transform'