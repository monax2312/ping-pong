import pygame
from random import randint, choice
from classes import *

pygame.init()

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption('пинг понг')


back = (randint(50, 255), randint(50, 255), randint(50, 255))

clock = pygame.time.Clock()

game = True
finish = False

score1 = 0
score2 = 0

font = pygame.font.SysFont('comicsans', 40)


rocket1 = Player(pygame.K_w, pygame.K_s, 30, 200, 50, 150, 7)
rocket2 = Player(pygame.K_UP, pygame.K_DOWN,  720, 200, 50, 150, 7)
ball = Ball(choice([-6, 6]), choice([-6, 6]), 'pngwing.com.png', 400, 200, 50, 50)

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            finish = False
            rocket1.rect.y = 200
            rocket2.rect.y = 200
            ball = Ball(choice([-6, 6]), choice([-6, 6]), 'pngwing.com.png', 400, 200, 50, 50)


    if not finish:
        dis.fill(back)

        rocket1.update(dis)
        rocket2.update(dis)
        ball.update(dis, rocket1, rocket2)

        score_text = f'{score1} / {score2}'
        score_text_b = font.render(score_text, 1, (0,0,0))
        dis.blit(score_text_b, (380, 20))

        if ball.rect.x < 0:
            finish = True
            score2 += 1
        if ball.rect.x > 750:
            finish = True
            score1 += 1
    else:
        text = f'press space to restart'
        text_b = font.render(text, 1, (0,0,0))
        dis.blit(text_b, (280, 240))




    
    clock.tick(30)
    pygame.display.flip()

