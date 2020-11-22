#PY ENEMY
import pygame
from platform import Platform
WHITE = (255,255,255)
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 795
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets\Sprites\prototypeEnemy.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.changeX = 0
        self.changeY = 0
        self.height = 50
        self.width = 50
    def update(self):
        # Gravity
        self.calcGrav()
        # Left and right
        self.rect.x += self.changeX
        # Up and down
        self.rect.y += self.changeY

    def calcGrav(self):
        # Effect of gravity calculation
        if self.changeY == 0:
            self.changeY = 1
        else:
            self.changeY += 0.35
    def moveToPlayer(self,player):
        #Calculate displacement between player and enemy
        dx = self.rect.x - player.rect.x
        if dx > 0 and dx <= 100:
            self.changeX = -1
        elif dx < 0 and dx >= -100:
            self.changeX = 1