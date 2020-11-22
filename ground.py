import pygame
pygame.init()
RED = (252, 10, 10)
GREEN = (46, 132, 31)
BLUE = (17, 199, 255)
WHITE = (255,255,255)
BLACK = (0,0,0)
SCREEN_WIDTH=1024
SCREEN_HEIGHT=795
class Ground(pygame.sprite.Sprite):
    #Ground the user stands and interacts on
    def __init__(self):
       #Floor constructor
        super().__init__()
        self.image = pygame.Surface((2000, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = 745
        self.height=50
        self.width=2000
class Wall(pygame.sprite.Sprite):
    #Invisible wall that prevents the user from passing
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((0,SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.width = 0
        self.height = SCREEN_HEIGHT