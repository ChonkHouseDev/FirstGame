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
    for i in range(100,700,100):
        pygame.draw.rect(screen, BLACK, (i,230,50,50))
    #update scrreen
    pygame.display.flip()