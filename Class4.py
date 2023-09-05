import pygame
import sys
pygame.init()

#DefinirColores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (720, 480)

screen = pygame.display.set_mode(size)

#Control
clock = pygame.time.Clock()
cord_x = 100
cord_y = 100

# Velocity
speed_x = 3
speed_y = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if cord_x > 400 or cord_x < 0:
        speed_x *= -1
        if cord_y > 400 or cord_y < 0:
            speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y

    #print(cord_x)
    #print(cord_y)
    # background WHITE
    screen.fill(WHITE)
    # -- Zone paint
    pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))
    # update screen
    pygame.display.flip()
    clock.tick(60)
