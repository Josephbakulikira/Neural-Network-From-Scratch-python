import pygame
import math

width, height = 800, 800

screen = pygame.display.set_mode((width, height))


run = True
while run:
    screen.fill((5, 10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


    pygame.display.update()

pygame.quit()
