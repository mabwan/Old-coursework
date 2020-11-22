import pygame, random, time, csv
from player import Player
from level import Level, Level_01, Level_02,Chest
from ground import Ground,Wall
from enemy import Enemy
pygame.init()
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (17, 199, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 795
height = 100
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PROTOTYPE")
font = pygame.font.Font("assets/font/windows_command_prompt.ttf", 20)
pauseFont  = pygame.font.Font("assets/font/windows_command_prompt.ttf", 100)
def save():
    return
def pause():
    return
def getKey():
  while 1:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
      return event.key
    else:
      pass

def popup(screen, message, width, height,x , y, bgcolor, textColor):
  #Display a popup box in the middle of the screen
  #This popup will only disappear when the user presses the Return key

  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, bgcolor,
                   (x - width/2 +2,
                    y - height/2 +2,
                    600,36), 0)
  pygame.draw.rect(screen, (255,255,255),
                   (x - width/2,
                    y - height/2,
                    604,40), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, textColor),
                (x - width/2 + 10, y - height/2 + 14))
  pygame.display.flip()

def askQuestion(screen, question, width, height, x, y, bgColor=(255,0,0), textColor=(255,255,255)):
  #width, height, x, y, bgColor and textColor are optional arguments
  #When x and y are omitted, use the centre of the screen
  if x==-1:
    x = screen.get_width() / 2
  if y==-1:
    y = screen.get_height() / 2

  pygame.font.init()
  current_string = []
  popup(screen, question + ": " + "".join(current_string), width, height, x, y, bgColor, textColor)
  upperCase=False
  while 1:
    inkey = getKey()
    if inkey == pygame.K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == pygame.K_RETURN:
      break
    elif inkey == pygame.K_LSHIFT or inkey == pygame.K_RSHIFT:
        upperCase=not upperCase #Switch between lowercase and uppercase when the shift key is pressed
    elif inkey <= 255:
      if (inkey>=97 and inkey<=122) and upperCase==True:
        inkey-=32 #Convert to UPPERCASE
      current_string.append(chr(inkey))
    popup(screen, question + ": " + "".join(current_string), width, height, x, y, bgColor, textColor)

  return "".join(current_string)
def main():
    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    player = Player()
    ground = Ground()
    chest = Chest()
    pause = False
    height = 100
    fps = 60
    player.rect.x = 150
    player.rect.y = 420
    hp = player.hp
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    player.level = current_level
    all_sprites_list.add(player)
    player.level = current_level
    # Allowing the user to close the window...
    carryOn = True
    clock = pygame.time.Clock()
    score = player.score
    player.position = 50
    questionList = []
    questionFile = open("questions.txt","r").read().splitlines()
    while carryOn:
        collision_list = pygame.sprite.spritecollide(player,current_level.platform_list,False)
        for collision in collision_list:
            #Hitting a platform sideways
            if player.changeX>0 and (player.rect.x+player.width)<=(collision.rect.x+10):
                player.changeX=0
                player.position = player.position - 5
                player.rect.x = collision.rect.x - player.width
            elif player.changeX<0 and player.rect.x>=(collision.rect.x+collision.width-10):
                player.changeX=0
                player.rect.x = collision.rect.x+collision.width
                player.position = player.position + 5
            else:
                #Falling onto a plaform
                if player.changeY>0:
                    player.rect.y = collision.rect.y - player.height
                    player.changeY = 0
                #Bumping head on a platform
                if player.changeY<0:
                    player.rect.y = collision.rect.y + collision.height
                    player.changeY = 0
        collision_list = pygame.sprite.spritecollide(player,current_level.enemy_list,False)
        for collision in collision_list:
            line = random.choice(questionFile)
            questionList.append(line)
            for line in questionList:
                data = line.split(";")
                question = data[0]
                answerQuestion = data[1]
            if player.changeY>0:
                answer = askQuestion(screen,question, width=500, height=40, x=500, y=100, bgColor=(0,0,0), textColor=(255,255,255)).upper()
                if answer == answerQuestion:
                    current_level.enemy_list.remove(collision)
                    score = score + 1
                    questionList.remove(question+";"+answerQuestion+";")
                else:
                    player.rect.x = player.rect.x -100
                    player.position = player.position - 100
                    hp = hp - 5

            else:
                hp = hp - (5/60)
        if player.rect.x <= ground.rect.x + 70:
            player.rect.x = 71
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    player.moveRight(10)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.goLeft()
            player.position =player.position - 5
        if keys[pygame.K_RIGHT]:
            player.goRight()
            player.position = player.position + 5
        if keys[pygame.K_UP]:
            player.jump(current_level.platform_list)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.changeX < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.changeX > 0:
                player.stop()
        if player.rect.x + ground.rect.x > SCREEN_WIDTH:
            player.changeX = 0
        pauseText = pauseFont.render("PAUSED",1,WHITE)
        if event.type == pygame.K_ESCAPE:
            print("test")
        # End Of Game
        all_sprites_list.update()
        current_level.update()
        for enemy in  current_level.enemy_list:
            collision_list = pygame.sprite.spritecollide(enemy,current_level.platform_list,False)
            for collision in collision_list:
            #Hitting a platform sideways
                if enemy.changeX>0 and (enemy.rect.x+enemy.width)<=(collision.rect.x+10):
                    enemy.changeX=0
                    enemy.rect.x = collision.rect.x - enemy.width
                elif enemy.changeX<0 and enemy.rect.x>=(collision.rect.x+collision.width-10):
                    enemy.changeX=0
                    enemy.rect.x = collision.rect.x+collision.width
                else:
                    #Falling onto a plaform
                    if enemy.changeY>0:
                        enemy.rect.y = collision.rect.y - enemy.height
                        enemy.changeY = 0
                    #Bumping head on a platform
                    if enemy.changeY<0:
                        enemy.rect.y = collision.rect.y + collision.height
                        enemy.changeY = 0

                enemy.moveToPlayer(player)
        for chest in  current_level.chest_list:
                    collision_list = pygame.sprite.spritecollide(chest,current_level.platform_list,False)
                    for collision in collision_list:
                    #Hitting a platform sideways
                        if chest.changeX>0 and (enemy.rect.x+chest.width)<=(collision.rect.x+10):
                            chest.changeX=0
                            chest.rect.x = collision.rect.x - chest.width
                        elif chest.changeX<0 and chest.rect.x>=(collision.rect.x+collision.width-10):
                            chest.changeX=0
                            chest.rect.x = collision.rect.x+collision.width
                        else:
                            #Falling onto a plaform
                            if chest.changeY>0:
                                chest.rect.y = collision.rect.y - chest.height
                                chest.changeY = 0
                            #Bumping head on a platform
                            if chest.changeY<0:
                                chest.rect.y = collision.rect.y + collision.height
                                chest.changeY = 0
                    player_chest_collision_list = pygame.sprite.spritecollide(player,current_level.chest_list,True)
                    for collision in player_chest_collision_list:
                        score = score + 1
        screen.fill(BLUE)
        # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        current_level.draw(screen)
        all_sprites_list.draw(screen)
        scoretext = font.render("Score = "+str(score), 1, WHITE)
        leveltext = font.render("Level = " + str(current_level_no + 1), 0, WHITE)
        healthtext  = font.render("Health = " + str(round(hp,0)), 0, WHITE)
        screen.blit(healthtext, (10,40))
        screen.blit(scoretext, (10,0))
        screen.blit(leveltext, (10,20))
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 974:
            diff = player.rect.right - 974
            player.rect.right = 974
            current_level.shift_world(-diff)
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 50:
            diff = 50 - player.rect.left
            player.rect.left = 50
            current_level.shift_world(diff)
##        if player.position >= current_level.level_limit:
##            screen.blit
##            current_level_no = current_level_no + 1
##            current_level = level_list[current_level_no]
##            player.level = current_level
##            player.rect.x = 50
##            player.position = 50
        # Refresh Screen
        pygame.display.flip()
        # Number of frames per secong e.g. 60
        clock.tick(fps)


main()
pygame.quit()
