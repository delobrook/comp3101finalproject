import pygame

pygame.init()


screen = pygame.display.set_mode((700, 400))

pygame.display.set_caption("FIFO Page Replacement Strategy")

# images
img = pygame.image.load('FIFO reference string.png')
numbers1 = 89
numbers2 = 50
img2 = pygame.image.load('FIFO empty memory.png')
boxes1 = 89
boxes2 = 100
boxes1_next = 0.1
img5 = pygame.image.load('one.png')
img6 = pygame.image.load('two.png')
img7 = pygame.image.load('three.png')
img9 = pygame.image.load('zero.png')
img10 = pygame.image.load('seven.png')
seven1 = 103
seven2 = 135
img13 = pygame.image.load('FIFO page fault.png')
faults1 = 90
faults2 = 150

messageStyle = pygame.font.Font('freesansbold.ttf', 15)
messageX = 90
messageY = 290
black = (0, 0, 0)

count = 0

message = ['Main memory is free', 'CPU calls for page from disk', 'Page is not in main memory',
           'Page fault occurs', 'Main memory is full', 'Page is already in main memory', 'Page hit occurs']


def displaymessages():
    text = messageStyle.render(message[count], True, black)


def covermessages():
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(70, 285, 500, 60))


def steps(x, y):
    screen.blit(img10, (x, y))
    screen.blit(img13, (x, y))


while True:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            screen.blit(img, (numbers1, numbers2))
            screen.blit(img2, (boxes1, boxes2))

    pygame.display.update()
