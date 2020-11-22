import pygame
from platform import Platform
from level import Level, Level_01, Level_02

pygame.init()
# Colours
RED = (252, 10, 10)
GREEN = (46, 132, 31)
BLUE = (17, 199, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Screen Dimensions
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 795


class Player(pygame.sprite.Sprite):
    # This class is the sprite that the player controls
    def __init__(self):
        # Constructor
        # Call the parent
        super().__init__()
        # Create sprite aesthetic
        self.image = pygame.image.load("Assets\Sprites\prototype.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (80, 160))
        # Reference to rect
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 420
        # Velocity
        self.changeX = 0
        self.changeY = 0
        self.height = 160
        self.width = 80
        # List of sprites that interact with
        self.level = None
        self.score = 0
        self.hp = 100
    def update(self):
        level = Level(self)
        # Player motion
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
    def jump(self, platform_list):
         # Check for obstruction
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.changeY = -10
        # Increase vertical acceleration
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.changeY = -10

    def goLeft(self):
        # Called when the user hits the left arrow
        self.changeX = -6

    def goRight(self):
        # Called when the user hits the right arrow
        self.changeX = 6

    def stop(self):
        # Called when the user lets off the keyboard
        self.changeX = 0

    def shift_world(self, shift_x):
        # When the user moves adjacent to the map, the screen needs to scroll alongside
        # Keep track of the shift amount
        self.world_shift += shift_x
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
