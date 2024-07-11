import pygame

pygame.init()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, p_image: str, x: int, y: int, w: int, h: int):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(p_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ball(GameSprite):
    def __init__(self, dx: int, dy: int, p_image: str, x: int, y: int, w: int, h: int):
        super().__init__(p_image, x, y, w, h)
        self.dx = dx
        self.dy = dy
    def update(self, d, rocket1, rocket2):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.y > 450:
            self.dy *= -1
        if self.rect.y < 0:
            self.dy *= -1
        if self.rect.colliderect(rocket1.rect):
            self.dx *= -1
        if self.rect.colliderect(rocket2.rect):
            self.dx *= -1

        d.blit(self.image, self.rect)
        


class Player(GameSprite):
    def __init__(self, up:str, down: str, x: int, y: int, w: int, h: int, speed: int):
        self.image = pygame.Surface((w, h))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.down = down
        self.up = up
    def update(self, d):
        key = pygame.key.get_pressed()

        if key[self.up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key[self.down] and self.rect.y < 350:
            self.rect.y += self.speed

        d.blit(self.image, self.rect)

