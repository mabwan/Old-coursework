import pygame
import os
import time
pygame.init()
#Colours
WHITE = (255,255,255)
GREY = (200,200,200)
BLACK = (0,0,0)
#Screen Dimensions
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 795
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Menu")
clock=pygame.time.Clock()
pygame.mouse.set_visible(False)
cursor = pygame.image.load("assets/font/cursor/idle.png").convert_alpha()
font = pygame.font.Font("assets/font/windows_command_prompt.ttf", 40)
class Splash(pygame.sprite.Sprite):
    def __init__(self):
        super(Splash,self).__init__()
        self.splash = []
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_01.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_02.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_03.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_03.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_04.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_05.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_06.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_07.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_08.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_09.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_10.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_11.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_12.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_13.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_14.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_15.png"))
        self.splash.append(pygame.image.load("Assets/Menu/splash/l0_splash_16.png"))
        self.index = 0
        self.image = self.splash[self.index]
        self.rect = pygame.Rect(SCREEN_WIDTH/2 - 300, 30, 640, 320)
    def update(self):
        self.index += 1
        time.sleep(60/1000)
        if self.index >= len(self.splash):
            self.index = 16
        self.image = self.splash[self.index]

class Select:
    hovered = False
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
    def set_rend(self):
        menu_font = pygame.font.Font(None, 40)
        self.rend = font.render(self.text, True, self.get_color())
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
def menu():
    font = pygame.font.Font("assets/font/windows_command_prompt.ttf", 20)
    splash = Splash()
    splashScreen = pygame.sprite.Group(splash)
    fontSelect = pygame.font.Font("assets/font/windows_command_prompt.ttf",20)
    menu=True
    options = [Select("NEW GAME", (SCREEN_WIDTH/2-60, (SCREEN_HEIGHT/2-100))), Select("LOAD GAME", (SCREEN_WIDTH/2-60, (SCREEN_HEIGHT/2 -50))),
           Select("OPTIONS", (SCREEN_WIDTH/2-60, (SCREEN_HEIGHT/2))),Select("QUIT", (SCREEN_WIDTH/2-60, (SCREEN_HEIGHT/2 +50)))]
    menuOption=0
    selected = "NEW GAME"
    while menu:
        pygame.init()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        splashScreen.update()
        screen.fill(BLACK)
        splashScreen.draw(screen)
        optionList=[]
        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
                for x in options:
                    optionList.append(x)
                if option == optionList[0]:
                    menuOption = 0
                elif option == optionList[1]:
                    menuOption = 1
                elif option == optionList[2]:
                    menuOption = 2
                elif option == optionList[3]:
                    menuOption = 3
            else:
                option.hovered = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    menuOption+=1
                    if menuOption==4:
                        menuOption=0
                    if menuOption ==0:
                        option = options[0]
                        selected=="NEW GAME"
                        option.hovered = True
                    elif menuOption==1:
                        option == options[1]
                        selected="LOAD GAME"
                        option.hovered = True
                    elif menuOption==2:
                        selected="OPTIONS"
                        option == options[2]
                        option.hovered = True
                    elif menuOption==3:
                        option == options[3]
                        selected="QUIT"
                        option.hovered = True
                elif event.key==pygame.K_RETURN or event.type==pygame.MOUSEBUTTONUP:
                    if menuOption== 0:
                        import prototype.py
                    elif menuOption == 1:
                        return
                    elif menuOption == 2:
                        return
                    elif menuOption == 3:
                        pygame.quit()
                        quit()
            option.draw()
        screen.blit(cursor,pygame.mouse.get_pos())
        text = font.render("menu (v1.00)", 0, WHITE)
        text1 = font.render("(c) Computer Company 2019. All rights reserved.", 0, WHITE)
        screen.blit(text, ((10),10))
        screen.blit(text1, ((10),25))
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

menu()