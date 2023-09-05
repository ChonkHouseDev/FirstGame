import pygame, sys
pygame.init()

# Definir Colores
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)


size = (800,500)
screen = pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    # background WHITE
    screen.fill(WHITE)
    # -- Zone paint
    ##-------------------------------x-----y-----width-height
    pygame.draw.line(screen, GREEN, [0,100],[100,100],5)
    ##-------------------------------x-----y-----width-height
    pygame.draw.rect(screen, BLACK, (100, 100, 80, 80))
    ##-------------------------------x-----y-----width-height
    pygame.draw.circle(screen, BLACK, (200, 200), 30)
    #update scrreen
    pygame.display.flip()