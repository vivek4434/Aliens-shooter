import pygame 
from pygame.locals import*
from sys import exit
from random import randint
  
pygame.init()
black = (255, 255, 255)
  
screen = pygame.display.set_mode((890, 550), 0, 32)
pygame.display.set_caption("Mihai The Hunter")
  
# Duck position
x_duck = 0
y_duck = randint(0, 450)
  
# Mouse position
x_pos = 0
y_pos = 0
  
# Click position
x_click = 0
y_click = 0
  
# Menu
ok = 0
ok2 = 0
url = "alien2.gif"
  
while ok==0:
    screen.blit(pygame.image.load(url), (0, 0))
    pygame.display.update()
  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                url = "alien2.gif"
            elif event.key == pygame.K_UP:
                url = "alien2.gif"
        elif event.type == MOUSEBUTTONDOWN:
            if url == "./re":
                ok = 1
            else:
                exit()
        elif event.type == QUIT:
            exit()
  
  
z = 0
points = 0
speed = 2
bonus = 0
# backup score
back_score = 0
exit = False
ok = 0
  
while ok==0:
  
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONDOWN:
            x_click, y_click = pygame.mouse.get_pos()
  
    position = (x_pos - 50 , y_pos - 50)
    x_duck += 1
  
    if x_duck * speed > 890 and not exit:
        x_duck = 0
        y_duck = randint(0, 450)
  
        exit = True
  
    # make screen black before adding objects
    screen.fill(black)
    pygame.mouse.set_visible(False)
  
    screen.blit(pygame.image.load("alien2.gif"), (0, 0))
    screen.blit(pygame.image.load("alien2.gif"), (750, 10))
    screen.blit(pygame.font.SysFont("tahoma", 40).render(str(points), True, black), (800, 10))
  
    # target bonus
    if points%12 == 0 and points !=0:
        bonus = 1
        back_score = points
    if x_click in range (160, 210) and y_click in range (50, 100) and bonus == 1:
        points +=10
        bonus = 0
    if points == back_score+2:
        bonus = 0
  
    # target duck
    if x_click in range(x_duck * speed - 20, x_duck * speed + 20) and y_click in range(y_duck - 30, y_duck + 30):
        points += 1
    if points%2 == 0:
        speed += 1
        x_duck = 0
        y_duck = randint(50, 500)
        z = randint(0, 450)
  
    # duck animation
    if z%2 == 0:
        if x_duck%3 == 0 or x_duck%4 == 0 or x_duck%5 == 0:
            screen.blit(pygame.image.load("./res/greenduck2.gif"), (x_duck * speed, y_duck))
        else:
            screen.blit(pygame.image.load("./res/greenduck3.gif"), (x_duck * speed, y_duck))
    else:
        if x_duck%3 == 0 or x_duck%4 == 0 or x_duck%5 == 0:
            screen.blit(pygame.image.load("./res/greenduck_big2.gif"), (x_duck * speed, y_duck))
        else:
            screen.blit(pygame.image.load("./res/greenduck_big3.gif"), (x_duck * speed, y_duck))
  
  
    # bonus animation
    if bonus == 1:
        screen.blit(pygame.image.load("alien2.gif"), (160, 50))
  
    if exit:
        ok = 1
        x_duck = -50
        y_duck = -50
        z = 0
        exit = False
        while z == 0:
            screen.blit(pygame.image.load("alien2.gif"), (400, 300))
            screen.blit(pygame.font.SysFont("arial", 60).render("LOOOSER!", True, (0, 255, 0)), (300, 200))
            screen.blit(pygame.font.SysFont("tahoma", 15).render("[ Click to try again ]", True, black), (340, 520))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    ok = 0
                    z = 1
  
                # copied from above
                points = 0
                speed = 0
                x_duck = 0
                y_duck = randint(0, 450)
                points = 0
                speed = 2
                bonus = 0
                back_score = 0
  
    elif event.type == QUIT:
                    exit()
  
    # set crosshair
    screen.blit(pygame.image.load("alien2.gif").convert(), position)
  
    pygame.display.update()
