#Snake Game!!

#imports required
import pygame,sys,random,time

#checking for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} Initializing Errors , Exiting....")
    sys.exit(-1)
else:
    print("(+) PyGame Succesfully Initialized!")
    
#Play Surface
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game")
time.sleep(2)

#colors
red = pygame.Color(255,0,0) #gameover
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,42,42) #food

#FPS Controller
fpsController = pygame.time.Clock()

#Important Variables
snakePos = [50,50]
snakeBody = [[50,50],[40,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True
score=0
direction = 'RIGHT'
changeTo = direction

#Game Over Function
def gameOver():
    myFont = pygame.font.SysFont('monaco',70)
    GOsurf = myFont.render('Game Over!',True,red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,15)
    playSurface.blit(GOsurf,GOrect)
    showScoreEOGame()
    pygame.display.flip() #UPDATE FUNCTION!!
    time.sleep(2)
    pygame.quit() #PyGame Exit
    sys.exit()    #System Exit
    
#Score Function for In Game
def showScoreInGame():
    sFont = pygame.font.SysFont('monaco',22)
    Ssurf = sFont.render('SCORE : {0}'.format(score),True,black)
    Srect = Ssurf.get_rect()
    Srect.midtop = (80,10)
    playSurface.blit(Ssurf,Srect)

#Score Function for End of Game
def showScoreEOGame():
    sFont = pygame.font.SysFont('monaco',22)
    Ssurf = sFont.render('SCORE : {0}'.format(score),True,black)
    Srect = Ssurf.get_rect()
    Srect.midtop = (360,120)
    playSurface.blit(Ssurf,Srect)
    
a=1
#Main Logic Of THe Game....
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] or keys[ord('d')]:
                changeTo = 'RIGHT'
            if keys[pygame.K_LEFT] or keys[ord('a')]:
                changeTo = 'LEFT'
            if keys[pygame.K_UP] or keys[ord('w')]:
                changeTo = 'UP'
            if keys[pygame.K_DOWN] or keys[ord('s')]:
                changeTo = 'DOWN'
            if keys[pygame.K_ESCAPE]:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
        
    #Validation Of Directions....
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    
    #Updation of the Position of Snake
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
    
    #Snake Body Mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score+=1
        foodSpawn = False
    else:
        snakeBody.pop()
    
    #Updation od Snake length
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
    
    #Snake And Food Drawing
    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(playSurface,brown,pygame.Rect(foodPos[0],foodPos[1],10,10))

    #FOr Wall Hit GameOVER
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
    
    #FOr Self Hit FameOVER
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
    
    #Updation and speed Control    
    showScoreInGame()
    pygame.display.flip()  
    fpsController.tick(20)                          
