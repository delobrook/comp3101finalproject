import pygame




#initialize pygame
pygame.init()
#create screen
screen= pygame.display.set_mode((1366,768))


# title and caption
pygame.display.set_caption("Final project")

#images
#page table
pagetable=pygame.image.load('pagetable.PNG')
pagetablex=300
pagetabley=435


tlb=pygame.image.load('TLB.PNG')
tlbx=700
tlby=100

virtualaddress=pygame.image.load('virtualaddress.PNG')
virtualaddressx=100
virtualaddressy=215

arrowpagetable=pygame.image.load('arrow.PNG')
arrowpagetablex=235
arrowpagetabley=600


arrows=pygame.image.load('arrows.PNG')
arrowsx=670
arrowsy=100

tlbhit=pygame.image.load('tlbhit.PNG')
tlbhitx=850
tlbhity=325

tlbmiss=pygame.image.load('tlbmiss.PNG')
tlbmissx=630
tlbmissy=315


add=pygame.image.load('add.PNG')
addx= 835
addy= 400
#fonts
font= pygame.font.Font('freesansbold.ttf',15)
fontx=25
fonty=0

#colors
red=(230,30,30)
blue=(30,30,230)
black=(0,0,0)
#explanations
explanations=[]
explanations.append("WELCOME! Virtualization of VM to physical address.(press right arrow key to go to first step)")
explanations.append("The virtual address consists of the page number and the offset")
explanations.append("The page pointer(number) is taken and the processor does a simultaneous check of all the Translation Lookaside Buffer's entries to determine, if they match the page number.")
explanations.append("if the page# is in the TLB,it is a TLB hit and the corresponding Frame number and offset are joined together to get the physical address")
explanations.append(" Otherwise its a TLB miss")
explanations.append("The processor will then search the page table one entry at a time for the Page # to get the frame#")
explanations.append("The corresponding Frame number and offset are joined together to get the physical address")

#controls animation
step2ani=0
step3ani=0
step5ani=0
step6ani=0
def explanation(step,x,y):
    explanation= font.render(explanations[step],True,(0,0,0))
    screen.blit(explanation,(x,y))
def step0():
    explanation(step, fontx, fonty)


def step1():
    step0()
    screen.blit(pagetable, (pagetablex, pagetabley))
    screen.blit(tlb, (tlbx, tlby))
    screen.blit(virtualaddress, (virtualaddressx, virtualaddressy))


def step2():
    step1()
    global step2ani
    if step2ani>=450:
        step2ani=450
        screen.blit(arrows, (arrowsx, arrowsy))
    step2ani+=0.5
    pygame.draw.line(screen, red,(200,200),(200+step2ani,200),6 )
    pygame.draw.line(screen, red, (202, 215), (202, 200), 6)
    screen.blit(add, (addx, addy))
def step3():
    step2()
    global step3ani
    if step3ani >= 428:
        step3ani = 428
        pygame.draw.line(screen, black, (843, 325), (843, 400), 2)
        pygame.draw.line(screen, blue, (885, 380), (885, 400), 2)
    step3ani += 0.5
    pygame.draw.line(screen, blue, (457, 380), (457+step3ani, 380), 2)
    pygame.draw.line(screen, blue, (457, 255), (457, 380), 2)

    screen.blit(tlbhit,(tlbhitx,tlbhity))
def step4():
    step3()
    screen.blit(tlbmiss,(tlbmissx,tlbmissy))
def step5():
    step4()
    global step5ani
    global  arrowpagetabley
    if step5ani >= 262:
        step5ani = 262
    step5ani += 0.5
    if arrowpagetabley <= 500:
        arrowpagetabley = 600
    else:
        arrowpagetabley -= 0.1
    pygame.draw.line(screen, red, (205, 253), (205, 253+step5ani), 6)
    pygame.draw.line(screen, red, (203, 515), (250, 515), 10)
    screen.blit(arrowpagetable,(arrowpagetablex,arrowpagetabley))

def step6():
    step5()
    global step6ani
    if step6ani >= 335:
        step6ani = 335
    step6ani += 0.5
    pygame.draw.line(screen, black, (500, 419), (500+step6ani, 419), 2)
    pygame.draw.line(screen, black, (500, 419), (500, 500), 2)
    pygame.draw.line(screen, black, (450, 500), (500, 500), 2)

step=0
running=True
while running:
    screen.fill((255, 255, 255))
    step0()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                step+=1
            if event.key == pygame.K_LEFT:
                step-=1
    if step==0:
       step0()
    elif step is 1:
        step1()
    elif step is 2:
        step2()
    elif step is 3:
        step3()
    elif step is 4:
        step4()
    elif step is 5:
        step5()
    elif step is 6:
        step6()
    elif step is 7:
        import cacheOp
    pygame.display.update()

