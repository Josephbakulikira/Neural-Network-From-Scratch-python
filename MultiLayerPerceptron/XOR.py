import pygame
import os
import random
import math
from Matrix import *
from Network import *

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1000, 1000
size = (width, height)
black, white = (0, 0, 0), (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Neural Network")
clock = pygame.time.Clock()
fps = 60

training_data = [
    {
    "inputs": [0, 1],
    "outputs": [1]
    },
    {
    "inputs": [0, 0],
    "outputs": [0]
    },
    {
    "inputs": [1, 0],
    "outputs": [1]
    },
    {
    "inputs": [1, 1],
    "outputs": [0]
    },
]

resolution = 40
columns = width // resolution
rows = height // resolution

neuralNetwork = NeuralNetwork(2, 2, 1)
# neuralNetwork.learning_rate =
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    for i in range(2000):
        data = training_data[random.randint(0, len(training_data) - 1)]
        neuralNetwork.Train(data["inputs"], data["outputs"])


    for x in range(rows):
        for y in range(columns):
            x1 = x/rows
            x2 = y/columns
            inputs = [x1, x2]
            _y = neuralNetwork.FeedForward(inputs)
            val = int(_y[0] * 255)

            color = (val, val, val )
            pygame.draw.rect(screen, color, pygame.Rect( x*resolution, y * resolution, resolution , resolution))


    pygame.display.update()
    # guess = neuralNetwork.FeedForward([0, 1])
    # print(guess)
pygame.quit()
