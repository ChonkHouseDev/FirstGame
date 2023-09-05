import randomZ
import pygame
import sys
pygame.init()

white= (255,255,255)
red=(255,0,0)

size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(white)
    for i in range(60):
        x = random.randint(0,800)
        y = random.randint(0,500)
        pygame.draw.circle(screen, red, (x,y),2 )

    pygame.display.flip()
    clock.tick(30)