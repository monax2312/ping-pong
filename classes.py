import pygame

pygame.init()

class GameSprite(sprite.Sprite):
    def __init__(self, p_image: str, x: int, y: int, w: int, h: int, speed: int):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ball(GameSprite):
    ...

class Player(GameSprite):
    ...

