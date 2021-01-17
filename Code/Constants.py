import pygame,os
from pygame import mixer
pygame.init()
pygame.mixer.init()

winSize=(650,600)

win=pygame.display.set_mode(winSize)

#--------------------------------------------------------------------------------------------------
# image files
bg = pygame.image.load('../../PacManGame/photos/z bg.png').convert_alpha()

pacManImage = [pygame.image.load(f'../../PacManGame/photos/z pac{i}.png') for i in range(1, 9)]

dot = pygame.image.load('../../PacManGame/photos/z dot.png').convert_alpha()

Bigdot = pygame.image.load('../../PacManGame/photos/z bigdot.png').convert_alpha()

ghost = pygame.image.load('../../PacManGame/photos/z orange_0.png').convert_alpha()

liveHeart = pygame.image.load('../../PacManGame/photos/z live.png').convert_alpha()

blueGhost = pygame.image.load('../../PacManGame/photos/z cyan_0.png').convert_alpha()

# ---------------------------------------------------------------------------------
# music files
bg_music = mixer.music.load("../../PacManGame/Songs/bg_music.wav")
mixer.music.set_volume(0.1)

MusicFiles = {f"{name[:name.find('.wav')]}":pygame.mixer.Sound(f"../../PacManGame/Sounds/{name}") for name in os.listdir('D:\PycharmProjects\my_project\PacMan\Sounds')}
for file in MusicFiles.values():
    file.set_volume(0.1)

lives=3

pacDirection= ''

ghostDirection=['right','left','up','down']

rightTeleportPos=(528 ,264)
leftTeleportPos=(109 , 264)

timer=0

transformation=False

score2=0

speed = 1