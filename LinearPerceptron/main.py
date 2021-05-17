import pygame
from Perceptron import *
from functions import *
from Point import *
import random


size = (width, height)
black,gray, blue, white = (10, 10, 10),(100, 100, 100), (1, 159, 255), (255,255,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Neural networks")
clock = pygame.time.Clock()
fps = 30

points = []

for i in range(100):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    breed = 0
    _y = lineFunction(x)
    if y > _y:
        breed = 1
    else:
        breed = -1

    points.append(Point(x, y, breed))


perceptron = Perceptron(3)


run = True
while run:
    screen.fill(black)
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    p1 = Point(-1, lineFunction(-1),0)
    p2 = Point(1, lineFunction(1),0)
    pygame.draw.line(screen, gray, (p1.PixelCoordX(), p1.PixelCoordY()), (p2.PixelCoordX(), p2.PixelCoordY()), 2)

    p1 = Point(-1, perceptron.guessY(-1),0)
    p2 = Point(1, perceptron.guessY(1),0)
    pygame.draw.line(screen, white, (p1.PixelCoordX(), p1.PixelCoordY()), (p2.PixelCoordX(), p2.PixelCoordY()), 2)

    for point in points:
        point.Display(screen)
        desired = point.breed
        perceptron.train(point.GetInputs(), desired)
        guess = perceptron.predict(point.GetInputs())
        if desired == guess:
            pygame.draw.circle(screen, white, (point.PixelCoordX(), point.PixelCoordY()), 8)
        else:
            pygame.draw.circle(screen, blue, (point.PixelCoordX(), point.PixelCoordY()), 8)


    pygame.display.update()
pygame.quit()
