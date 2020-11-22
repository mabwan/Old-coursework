import pygame
from platform import Platform
from ground import Ground,Wall
from enemy import Enemy
pygame.init()
YELLOW = (255,255,153)
class Teleporter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 32
        self.height = 32
        self.teleporter = [
        pygame.image.load("Assets/sprites/teleporter/l0_teleporter01.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter02.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter03.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter04.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter05.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter06.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter07.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter08.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter09.png")
        ,pygame.image.load("Assets/sprites/teleporter/l0_teleporter10.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter11.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter12.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter13.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter14.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter15.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter16.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter17.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter18.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter19.png")
        ,pygame.image.load("Assets/sprites/teleporter/l0_teleporter20.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter21.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter22.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter23.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter24.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter25.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter26.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter27.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter28.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter29.png")
        ,pygame.image.load("Assets/sprites/teleporter/l0_teleporter30.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter31.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter32.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter33.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter34.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter35.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter36.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter37.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter38.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter39.png")
        ,pygame.image.load("Assets/sprites/teleporter/l0_teleporter40.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter41.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter42.png"),pygame.image.load("Assets/sprites/teleporter/l0_teleporter43.png")]
        self.index = 0
        self.image = self.teleporter[self.index]
        self.rect = self.image.get_rect()
    def update(self):
        self.index += 1
        if self.index >= len(self.teleporter):
            self.index = 0
        self.image = self.teleporter[self.index]
        self.image = pygame.transform.scale(self.teleporter[self.index],(128,128))
class Chest(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = 50
        height = 50
        self.image = pygame.Surface([width, height])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.width=width
        self.height=height
        self.changeX = 0
        self.changeY = 0
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
class Level():
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.chest_list = pygame.sprite.Group()
        self.teleporter_list = pygame.sprite.Group()
        self.player = player
        self.world_shift = 0
        ground = Ground()
        wall = Wall()
        self.platform_list.add(ground)
        self.platform_list.add(wall)

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.chest_list.update()
        self.teleporter_list.update()

    def draw(self, screen):
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.chest_list.draw(screen)
        self.teleporter_list.draw(screen)
    def shift_world(self, shift_x):
        # Keep track of the shift amount
        self.world_shift += shift_x
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        for chest in self.chest_list:
            chest.rect.x += shift_x

class Level_01(Level):
    def __init__(self, player):
        teleporter = Teleporter()
        # Call the parent constructor
        Level.__init__(self, player)
        self.level_limit = 2000
        # Array with width, height, x, and y of platform
        level = [[210, 40, 500, 650],
                 [210, 40, 900, 600],
                 [210, 40, 1200, 550],
                 [210, 40, 1400, 450],
                 [1000,40,2010,795],
                 [1000,40,2010,795]]
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            teleporter.rect.x = 1000
            teleporter.rect.y =620
            self.teleporter_list.add(teleporter)
        # X and Y coordinates for generating enemies
        enemy_list=[]
        enemy_level = [[230,420],[500,420],[800,300]]
        for n in enemy_level:
            enemy = Enemy()
            enemy.rect.x = n[0]
            enemy.rect.y = n[1]
            self.enemy_list.add(enemy)
        #X and Y for the score chests
        chest_list=[]
        chest_level = [[300,100],[550,300]]
        for n in chest_level:
            chest = Chest()
            chest.rect.x = n[0]
            chest.rect.y = n[1]
            self.chest_list.add(chest)

# Create platforms for the level
class Level_02(Level):
    def __init__(self, player):
        teleporter = Teleporter()
        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = 1500

        # Array with type of platform, and x, y location of the platform.
        level = [[210, 70, 450, 770],
                 [210, 70, 850, 520],
                 [210, 70, 1000, 420],
                 [210, 70, 1120, 580],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        teleporter.rect.x = self.level_limit
        teleporter.rect.y = 50
        self.teleporter_list.add(teleporter)
