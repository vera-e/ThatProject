import pygame, sys, random
from time import *
from pygame import *
from pygame.locals import *
scores=[]
name=[]
def playagain():
    print "Would you like to play again?"
    global playername
    choice=raw_input("Or do you want to see the current high scores: ")
    choice1=choice.lower()
    if choice=='yes' or choice=='y':
        playername=raw_input('Name:  ')
        main_loop(random.randint(3.0,6.0))
    elif choice=='high scores' or choice=='hs':
        highscores()
    elif choice=='no' or choice=='n' or choice=='goodbye' or choice=='bye' or choice=='exit' or choice=='quit':
        pygame.quit()
        sys.exit()       
def highscores():
    pygame.init()
    windowSurface = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Tic-toc!')
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED=(255, 0, 0)
    GREEN=(0,255,0)
    basicFont = pygame.font.SysFont(None, 48)    
    global finaltime
    global scores
    global name
    global playername
    font = pygame.font.Font(None, 35)  # load the default font, size 50
    color = (255, 50, 0)
    if finaltime<=.01:
        finaltime=0.00
        scores.append(str(finaltime))
    else:
        scores.append(str(finaltime+.01))
    name.append(str(playername))            
    for i in range(len(scores)):
        score = scores[i]
        name= name[i]
        nameimage = font.render(name, True, color)
        namerect = nameimage.get_rect()
        namerect.left, namerect.y = 40, 100 + (i*(namerect.height + 20))
        windowSurface.blit(nameimage,namerect)
        scoreimage = font.render(score, True, color)
        scorerect = scoreimage.get_rect()
        scorerect.right, scorerect.y = 480, namerect.y
        windowSurface.blit(scoreimage, scorerect)
        for d in range(namerect.right + 25, scorerect.left-10, 25):
            pygame.draw.rect(scoreimage, color, pygame.Rect(d, scorerect.centery, 5, 5))
    pygame.display.update()
    sleep(7)
    pygame.quit()
    playagain()
def main_loop(timer):
    global playername
    playername=raw_input('Name:  ')
    global finaltime
    pygame.init()
    windowSurface = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Tic-toc!')
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED=(255, 0, 0)
    GREEN=(0,255,0)
    basicFont = pygame.font.SysFont(None, 48)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        timer-=.01
        if timer<=0.0099:
            timernew=0.00
            timer=0.00
            textnew=basicFont.render('0.00', True, WHITE, RED)
            textRectnew = textnew.get_rect()
            textRectnew.centerx = windowSurface.get_rect().centerx
            textRectnew.centery = windowSurface.get_rect().centery
            windowSurface.blit(textnew, textRect)
            pygame.display.update()
            break
        button1,button2,button3=pygame.mouse.get_pressed()
        text = basicFont.render(str(timer), True, WHITE, BLUE)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery
        x,y=pygame.mouse.get_pos()
        if (x > textRect.left) and (x < textRect.right) and (y > textRect.top) and (y < textRect.bottom) and button1==1:
            text=basicFont.render(str(timer), True, WHITE, BLUE)
            finaltime=timer
            break
        sleep(.01)
        windowSurface.blit(text, textRect)
        pygame.display.update()
    pygame.quit()
    playagain()
    return
main_loop(random.randint(3.0,6.0))