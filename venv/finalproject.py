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
font= pygame.font.Font('freesansbold.ttf',14)
fontx=25
fonty=0



#explanations
explanations=[]
explanations.append("The virtual address consists of the page number and the offset")
explanations.append("The page pointer(number) is taken and the processor does a simultaneous check of all the Translation Lookaside Buffer's entries to determine, if they match the page number.")
explanations.append("if the page# is in the TLB the corresponding Frame number and offset are joined together to get the physical address")
explanations.append(" Otherwise its a TLB miss")
explanations.append("The processor will then search the page table one entry at a time for the Page # to get the frame#")
explanations.append("The corresponding Frame number and offset are joined together to get the physical address")


def explanation(step,x,y):
    explanation= font.render(explanations[step],True,(0,0,0))
    screen.blit(explanation,(x,y))

def step0():
    screen.blit(pagetable, (pagetablex, pagetabley))
    screen.blit(tlb, (tlbx, tlby))
    screen.blit(virtualaddress, (virtualaddressx, virtualaddressy))

def step1():
    screen.blit(arrows, (arrowsx, arrowsy))
    screen.blit(add, (addx, addy))
def step2():
    step1()
    screen.blit(tlbhit,(tlbhitx,tlbhity))
def step3():
    step2()
    screen.blit(tlbmiss,(tlbmissx,tlbmissy))
def step4():
    step3()
    screen.blit(arrowpagetable,(arrowpagetablex,arrowpagetabley))

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
    explanation(step,fontx,fonty)
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
        if arrowpagetabley <= 500:
            arrowpagetabley=500
        else:
            arrowpagetabley -= 0.1
    else:
        step=0


    pygame.display.update()