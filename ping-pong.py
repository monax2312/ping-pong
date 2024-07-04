import pygame
from random import randint
from classes import *

pygame.init()

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption('пинг понг')


back = (randint(0, 255), randint(0, 255), randint(0, 255))

clock = pygame.time.Clock()

game = True
finish = False


rocket1 = Player(pygame.Surface(), 30, 200, 50, 150)
rocket2 = Player(pygame.Surface(), 520, 200, 50, 150)
ball = Ball('pngwing.com.png', 200, 200, 50, 50)

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if not finish:
        dis.fill(back)


    
    clock.tick(30)
    pygame.display.flip()

