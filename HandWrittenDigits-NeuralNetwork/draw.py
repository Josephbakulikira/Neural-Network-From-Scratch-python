import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

brush = pygame.image.load("Brush/brush.png")
brush = pygame.transform.scale(brush, (128, 128))
pygame.display.update()

z = 0
run = True
while run :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            z = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            z = 0



    mx, my = pygame.mouse.get_pos()
    if z == 1:
        screen.blit(brush, (mx - 128//2, my - 128//2))
    pygame.display.flip()

pygame.quit()
