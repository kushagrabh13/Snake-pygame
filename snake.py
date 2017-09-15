import pygame
import time
import random

pygame.init()

back = (255,255,255)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

block_size = 20
FPS = 15
direction = "up"
clock = pygame.time.Clock()

smallfont = pygame.font.Font("comic.ttf",25)
medfont = pygame.font.Font("comic.ttf",50)
largefont = pygame.font.Font("comic.ttf",80)
score = pygame.font.Font("comicbd.ttf",25)

img = pygame.image.load('snakeHead.png')
img2 = pygame.image.load('snakeBody.png')


def Start_Screen():
    
    s_screen = True
    gameDisplay.fill(back)
    while s_screen:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    s_screen = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            pygame.display.update()
            
        Message("Welcome To Snake !!",green,0,-120,"large")
        Message("The Objective Of The Game Is To Eat Apples",black,0,-30,"small")
        Message("The More Apples You Eat , Longer You Get",black,0,10,"small")
        Message("If You Run Into Yourself Or The Edges You Die !!",black,0,50,"small")
        Message("Use Arrow Keys To Navigate the Snake And 'P' To Pause",black,0,90,"small")
        Message("Press 'C' To Play Or 'Q' To Quit",red,0,150,"small")
        Message("Developed By Kushagra Bhatnagar",blue,175,265,"small")

        pygame.display.update()
        clock.tick(15)

def Pause():
    paused = True
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                      paused = False
                    
                if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

            pygame.display.update()

        Message("Paused",red,0,-50,"large")
        Message("Press 'C' To Continue Or 'Q' to Quit",black,0,50,"small")
        pygame.display.update()
        
def Snake(block_size,snakeList):

    if direction=="right":
        head = pygame.transform.rotate(img,270)
        body = pygame.transform.rotate(img2,270)
     
        
    if direction=="left":
        head = pygame.transform.rotate(img,90)
        body = pygame.transform.rotate(img2,90)
        
        
    if direction=="up":
        head = img
        body = img2
        
    if direction=="down":
        head = pygame.transform.rotate(img,180)
        body = pygame.transform.rotate(img2,180)
        
        
    gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    for XY in snakeList[:-1]:
        gameDisplay.blit(body,[XY[0],XY[1]])

def Score(S):
    a = score.render(S,True,blue)
    gameDisplay.blit(a,[display_width-150,5])

def text_object(text,color,size):
    if size =="small":
        textSurface = smallfont.render(text,True,color)

    if size =="med":
         textSurface = medfont.render(text,True,color)

    if size =="large":
        textSurface = largefont.render(text,True,color)
   
    return textSurface,textSurface.get_rect()

def Message(msg,color,x_displace,y_displace,size):
    textSurf,textRect = text_object(msg,color,size)
    textRect.center = (display_width/2) + x_displace , (display_height/2) + y_displace
    gameDisplay.blit(textSurf,textRect)

def GameLoop():
    global direction 
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    apple_x = round(random.randrange(block_size,display_width-block_size)/10.0)*10.0
    apple_y = round(random.randrange(block_size,display_height-block_size)/10.0)*10.0
    lead_x_change = 0
    lead_y_change = 0
    snakeList = []
    snakeLength = 1
    score = 0
    
    while not gameExit :
        while gameOver == True:
            gameDisplay.fill(back)
            Message("Game Over !!",red,0,-50,"large")
            Message("Press 'C' To Play Again Or 'Q' to Quit",black,0,50,"small")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        GameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False
                gameExit = True
                 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_y_change = 0
                    lead_x_change = -block_size
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_y_change = 0
                    lead_x_change = block_size
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_x_change = 0
                    lead_y_change = block_size
                elif event.key == pygame.K_p:
                    Pause()

        if(lead_x <= 0 or lead_x >= display_width or lead_y <= 0 or lead_y >= display_height):
            print("Collision With Wall")
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change
        apple = pygame.image.load('apple.png')
        gameDisplay.fill(white)
        gameDisplay.blit(apple,(apple_x,apple_y))
        apple_thickness = block_size
        
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
            
        for seg in snakeList[:-1]:
            if seg == snakeHead:
                print("Collision With Self")
                gameOver = True
        Score("Score : {}".format(score))
        Snake(block_size,snakeList)
        pygame.display.update()

        
        if lead_x >= apple_x and lead_x <= apple_x + apple_thickness or lead_x + block_size > apple_x and lead_x + block_size < apple_x + apple_thickness:
            if lead_y >= apple_y and lead_y <= apple_y + apple_thickness or lead_y + block_size > apple_y and lead_y + block_size < apple_y + apple_thickness:
                print("Apple Eaten")
                apple_x = round(random.randrange(block_size,display_width-block_size)/10.0)*10.0
                apple_y = round(random.randrange(block_size,display_height-block_size)/10.0)*10.0
                snakeLength += 1
                score += 1
            
        clock.tick(FPS)

    pygame.quit()
    quit()

Start_Screen()
GameLoop()
