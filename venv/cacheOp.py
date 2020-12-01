import pygame

#initialize pygame
pygame.init()
#create screen
screen= pygame.display.set_mode((1366,768))


# title and caption
pygame.display.set_caption("Final project")
addressCount=0
#This outlines all image references and their coordiantes
#cache
cacheimg=pygame.image.load('cache.png')
cacheimgx=700
cacheimgy=70
cacheimg2=pygame.image.load('Record-found-1.png')
cacheimg3=pygame.image.load('Record-found-2.png')
cacheimg4=pygame.image.load('Record-not-found.png')
mainMemoryArrow=pygame.image.load('main-mem-arrow.png')
mainMemoryArrowY=450
mainMemoryArrowX=400
addressImgX=800
addressImgY=490
addressImg1=pygame.image.load('0.png')
addressImg2=pygame.image.load('4.png')

mainmemImg=pygame.image.load('mainmem.png')
mainmemImgx=100
mainmemImgy=200
#up arrow img
upArrowImg=pygame.image.load('arrow-up.png')
upArrowImgx=800
upArrowImgy=370

#fonts
font= pygame.font.Font('freesansbold.ttf',14)
fontx=25
fonty=0

#Physical memory address
addressTextFont= pygame.font.Font('freesansbold.ttf',30)
addressTextFontx=800
addressTextFonty=490

cacheLabelFont= pygame.font.Font('freesansbold.ttf',30)
cacheLabelX=770
cacheLabelY=30

mainMemLabelFont= pygame.font.Font('freesansbold.ttf',30)
mainMemLabelX=130
mainMemLabelY=170

physicalAddressFont= pygame.font.Font('freesansbold.ttf',30)
physicalAddressFontX=700
physicalAddressFontY=450

#guideTxt
guideTxt=[]
guideTxt.append("After obtaining the physical Address, the cache is checked to identify whether the data is already present")
guideTxt.append("If the data from this physical address is stored within the cache, this results in a cache hit")
guideTxt.append("The data is then supplied from the cache storage")
guideTxt.append("If this physical address value was not stored, a cache miss occurs and then main memory has to be accessed directly")

stepCounterTxt=[]
addressList=[]
addressList.append("0")
addressList.append("3")

def addLabels():
    #add text above cache image
    labelCache=cacheLabelFont.render("Cache",True,(0,0,0))
    screen.blit(labelCache,(cacheLabelX,cacheLabelY))
    #add text above mainmemory image
    labelMainMem=mainMemLabelFont.render("Main Memory",True,(0,0,0))
    screen.blit(labelMainMem,(mainMemLabelX,mainMemLabelY))
    #Add text to show current physical address
    labelPAddress=physicalAddressFont.render("Physical Address",True,(0,0,0))
    screen.blit(labelPAddress,(physicalAddressFontX,physicalAddressFontY))


def explanation(stepCounter,x,y):
    if stepCounter > 3:
        stepCounter=0
    explanation= font.render(guideTxt[stepCounter],True,(0,0,0))
    screen.blit(explanation,(x,y))

def addressGuide(stepCounter,x,y):
    addressGuideText= addressTextFont.render(addressList[stepCounter],True,(0,0,100))
    screen.blit(addressGuideText,(x,y))

def draw1():
    screen.blit(cacheimg, (cacheimgx, cacheimgy))
    screen.blit(mainmemImg, (mainmemImgx, mainmemImgy))
    screen.blit(upArrowImg, (upArrowImgx, upArrowImgy))
    screen.blit(addressImg1,(addressImgX,addressImgY))


def draw2():
    screen.blit(cacheimg2, (cacheimgx, cacheimgy))

def draw3():
    screen.blit(cacheimg3, (cacheimgx, cacheimgy))


def draw4():
    screen.blit(cacheimg4, (cacheimgx, cacheimgy))
    addressText= addressTextFont.render("3",True,(0,0,100))
    screen.blit(addressImg2,(addressImgX,addressImgY))
    screen.blit(mainMemoryArrow,(mainMemoryArrowX,mainMemoryArrowY))

stepCounter=0
running=True
while running:
    if stepCounter > 3:
        stepCounter=0
    screen.fill((255, 255, 255))
    draw1()
    addLabels()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                stepCounter+=1
            if event.key == pygame.K_LEFT:
                stepCounter-=1
    explanation(stepCounter,fontx,fonty)
    if stepCounter==0:
       draw1()
    elif stepCounter is 1:
        draw2()
    elif stepCounter is 2:
        draw3()
        addressCount+=1
    elif stepCounter is 3:
        draw4()
    else:
        stepCounter=0


    pygame.display.update()