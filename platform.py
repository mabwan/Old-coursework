import pygame

pygame.init()
RED = (252, 10, 10)
GREEN = (46, 132, 31)
BLUE = (17, 199, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Platform(pygame.sprite.Sprite):
    # Platforms the user stands and interacts on
    def __init__(self, width, height):
        # Floor constructor
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.width=width
        self.height=height
