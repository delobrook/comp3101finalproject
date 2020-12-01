import pygame

pygame.init()

display_width=800
display_height=600

black=(0,0,0)
white =(255,255,255)
red=(255,0,0)

gameDisplay=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("A bit Racey")
clock=pygame.time.Clock()

getimg1= pygame.image.load('1_put_page1')
getimg2= pygame.image.load('2_put_page2')
getimg3= pygame.image.load('3_get_page1')
getimg4= pygame.image.load('4_put_page3')
getimg5= pygame.image.load('5_get.page2')
getimg6= pygame.image.load('6_put_page4')
getimg7= pygame.image.load('7_get_page1')
getimg8= pygame.image.load('8_get_page3')
getimg9= pygame.image.load('9_get_page4')

def get1(x,y):
    gameDisplay.blit(getimg,(x,y))

x=(display_width*0.45)
y=(display_heigth *0.8)

crashed=False
while not crashed:
    for event in pyga,e.event.get():
        if event.type==pygame.Quit:
            crashed=True

    
    gameDisplay.fill(white)
    get1(x,y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
    

    
    #pygame in c:\users\mat\appdata\roaming\python\python39\site-packages (2.0.0)
