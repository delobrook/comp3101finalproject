import pygame

pygame.init()

screen = pygame.display.set_mode((1300,700))

pygame.display.set_caption("Optimal Page Replacement Algorithm")

#images
table=pygame.image.load('First table.PNG')
tablex=50
tabley=350

#font
font= pygame.font.Font('freesansbold.ttf',15)
fontx=100
fonty=320

titleE= pygame.font.Font('freesansbold.ttf',24)
titlex=0
titley=0

explanation=[]
explanation.append("WELCOME! OPTIMAL PAGE REPLACEMENT (press right arrow key to enter string data into Main Memory")
explanation.append("Welcome to virtual Main memory. Press right arrow key to enter string data into memory")
explanation.append("7 in Main memory. 2 Free pages in Memory, Press right arrow key")
explanation.append("7 and 0 in Memory. 1 free page in memory. Press right arrow key ")
explanation.append("All frames are full in RAM. 7 being used for the longest of time based on data list")
explanation.append("String data 7 replaced because it is being used for longest optimal time")
explanation.append("0 string data remains as it already exists in main memory: PAGE HIT count = 1")
explanation.append("1 no longer exists in preentered memory. So it is replaced.Can't replace 0 or 2 because they still are going to be used.")
explanation.append("0 remains same: PAGE HIT count =2 ")
explanation.append("0 no longer exists in long term string data thus replaced.")
explanation.append("7 replaces the string data thats been using the longest time. PAGE HIT count=2 PAGE FAULTS= 7")
explanation.append("Simulation End.")

def explanations():
    e=titleE.render(explanation[count],True,(0,0,0))
    screen.blit(e,(titlex,titley))


def numbers(x,y):
    nums= font.render("7     0     1     2     0     3     0     4     7    ",True,(0,0,0))
    screen.blit(nums,(x,y))

#colors
red=(230,30,30)
blue=(30,30,230)
black=(0,0,0)



sevenx=100
seveny=320
zerox=130
zeroy=320
onex=160
oney=320
twox=190
twoy=320
zex=220
zey=320
treex=220
treey=320
zrox=280
zroy=320
fourx=310
foury=320
lastx=340
lasty=320


firstboxx=80
firstboxy=370
secondboxx=80
secondboxy=400
thirdboxx=80
thirdboxy=430

def firststep():
    screen.blit(table,(tablex,tabley))
    numbers(fontx,fonty)
    explanations()

def secondstep():
    seven=font.render("7",True,(0,0,0))
    screen.blit(seven,(sevenx,seveny))

def thirdstep():
    zero = font.render("0", True, (0, 0, 0))
    screen.blit(zero, (zerox, zeroy))

def fourthstep():
    one = font.render("1", True, (0, 0, 0))
    screen.blit(one, (onex, oney))

def fifthstep():
    two = font.render("2", True, (0, 0, 0))
    screen.blit(two, (twox, twoy))

def sixthstep():
    ze = font.render("0", True, (0, 0, 0))
    screen.blit(ze, (zex, zey))

def seventhstep():
    tree = font.render("3", True, (0, 0, 0))
    screen.blit(tree, (treex, treey))

def eightstep():
    zro = font.render("0", True, (0, 0, 0))
    screen.blit(zro, (zrox, zroy))

def ninthstep():
    four=font.render("4",True,(0,0,0))
    screen.blit(four,(fourx,foury))

def tenthstep():
    last = font.render("7", True, (0, 0, 0))
    screen.blit(last, (lastx, lasty))


count=0
running=True
while running:
    screen.fill((255, 255, 255))
    firststep()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                count+=1
            if event.key == pygame.K_LEFT:
                count-=1

    if count==1:
        firststep()

    elif count==2:

        secondstep()


        if seveny>=firstboxy and sevenx<=firstboxx:
            seveny=firstboxy
            sevenx=firstboxx
            table = pygame.image.load('2nd Table .png')
            screen.blit(table, (tablex, tabley))
        else:
            seveny += 0.1
            sevenx -= 0.1

    elif count==3:

        thirdstep()


        if zeroy >= secondboxy and zerox <= secondboxx:
            zeroy = secondboxy
            zerox = secondboxx
            table = pygame.image.load('3rd Table.png')
            screen.blit(table, (tablex, tabley))
        else:
            zeroy += 0.1
            zerox -= 0.1
    elif count == 4:

        fourthstep()


        if oney >= thirdboxy and onex <= thirdboxx:
            oney = thirdboxy
            onex = thirdboxx
            table = pygame.image.load('4th Table .png')
            screen.blit(table, (tablex, tabley))
        else:
            oney += 0.2
            onex -= 0.2

    elif count == 5:
        fifthstep()

        if twoy >= firstboxy and twox <= firstboxx:
                twoy = firstboxy
                twox = firstboxx
                table = pygame.image.load('5th table.png')
                screen.blit(table, (tablex, tabley))
        else:
                twoy += 0.1
                twox -= 0.2

    elif count ==6:
        sixthstep()

        if zey >= secondboxy and zex <= secondboxx:
            zey = secondboxy
            zex = secondboxx
            table = pygame.image.load('6th Table .png')
            screen.blit(table, (tablex, tabley))
        else:
            zey += 0.1
            zex -= 0.2

    elif count == 7:

        seventhstep()

        if treey >= thirdboxy and treex <= thirdboxx:
            treey = thirdboxy
            treex = thirdboxx
            table = pygame.image.load('7th table.png')
            screen.blit(table, (tablex, tabley))
        else:
            treey += 0.1
            treex -= 0.1

    elif count == 8:

        eightstep()

        if zroy >= secondboxy and zrox <= secondboxx:
            zroy = secondboxy
            zrox = secondboxx
            table = pygame.image.load('8th table.png')
            screen.blit(table, (tablex, tabley))
        else:
            zroy += 0.1
            zrox -= 0.2

    elif count == 9:

        ninthstep()

        if foury >= secondboxy and fourx <= secondboxx:
            foury = secondboxy
            fourx = secondboxx
            table = pygame.image.load('9th table.png')
            screen.blit(table, (tablex, tabley))
        else:
            foury += 0.1
            fourx -= 0.3

    elif count == 10:

        tenthstep()

        if lasty >= firstboxy and lastx <= firstboxx:
            lasty = firstboxy
            lastx = firstboxx
            table = pygame.image.load('last.png')
            screen.blit(table, (tablex, tabley))
        else:
            lasty += 0.1
            lastx -= 0.5

    else:
        count=1
    pygame.display.update()