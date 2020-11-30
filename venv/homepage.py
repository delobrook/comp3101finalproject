import pygame

#initialize pygame
pygame.init()
#create screen
screen= pygame.display.set_mode((1366,768))

#Font
titlefont= pygame.font.Font('freesansbold.ttf',60)
titlefontx=25
titlefonty=0

instructionfont= pygame.font.Font('freesansbold.ttf',32)
instructionfontx=0
instructionfonty=75

optionfont= pygame.font.Font('freesansbold.ttf',24)
option1fontx=50
option1fonty=150
option2fontx=50
option2fonty=200
option3fontx=50
option3fonty=250
option4fontx=50
option4fonty=300



def title(x,y):
    title= titlefont.render("WELCOME To The Virtual Memory Visualizer",True,(0,0,0))
    screen.blit(title,(x,y))

def instruction(x,y):
    instruction = instructionfont.render("Press The Number Key That Corresponds With An Option You Would Like To View ", True, (0, 0, 0))
    screen.blit(instruction, (x, y))

def option(x,y,r,g,b,str):
    option = optionfont.render(str, True, (r, g, b))
    screen.blit(option,(x,y))

running=True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                import finalproject
            if event.key == pygame.K_2:
                step=1
            if event.key == pygame.K_3:
                step=1
            if event.key == pygame.K_4:
                step=1


    title(titlefontx,titlefonty)
    instruction(instructionfontx,instructionfonty)
    option(option1fontx,option1fonty, 240, 30, 30, "1.    VISUALIZATION OF VIRTUAL ADDRESS TO PHYSICAL ADDRESS TRANSLATION USING TLB AND CACHE")
    option(option2fontx,option2fonty, 30, 240, 30, "2.    VISUALIZATION OF LRU PAGE REPLACEMENT STRATEGY")
    option(option3fontx,option3fonty, 30, 30, 240, "3.    VISUALIZATION OF FIFO PAGE REPLACEMENT STRATEGY")
    option(option4fontx, option4fonty, 128, 0, 128, "4.    VISUALIZATION OF OPT PAGE REPLACEMENT STRATEGY")


    pygame.display.update()
