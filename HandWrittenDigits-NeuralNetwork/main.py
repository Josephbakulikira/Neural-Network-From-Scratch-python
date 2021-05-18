import pygame
import idx2numpy
import numpy as np
import time
from Network import *
from Matrix import *
from constants import *


#pygame configurations
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HandWritten digits Neural Network")
clock = pygame.time.Clock()
fps = 60

# --- Get THe data ---
training_images = 'data/train-images.idx3-ubyte'
training_labels = 'data/train-labels.idx1-ubyte'
testImages = 'data/t10k-images.idx3-ubyte'
testLabels = 'data/t10k-labels.idx1-ubyte'

train_images = idx2numpy.convert_from_file(training_images)
train_labels = idx2numpy.convert_from_file(training_labels)
test_images = idx2numpy.convert_from_file(testImages)
test_labels = idx2numpy.convert_from_file(testLabels)

#if it not accurate increase the number of training data , range ( 1000.......120000)
number_of_training_data = 2000
training_data = train_images[:number_of_training_data]
testing_data = test_images[:200]


#preparing the data
train_data_images = [[] for i in range(len(training_data))]
for i in range(len(training_data)):
    for x in range(28):
        for y in range(28):
            train_data_images[i].append(train_images[i][x][y]/255)

test_data_images = [[] for i in range(len(testing_data))]
for i in range(len(testing_data)):
    for x in range(28):
        for y in range(28):
            test_data_images[i].append(test_images[i][x][y]/255)

#setup
pixelSize = 20

Yoffset = (height//2) - (28 * pixelSize//2)
Xoffset = (width //2) - (28 * pixelSize//2)

neuralNetwork = NeuralNetwork(784, 64, 10)
trained = False
training = False

def train():
    global trained
    for i in range(number_of_training_data):
        inputs = train_data_images[i]
        # normalize the data (0 -- 1)
        outputs = train_labels[i]

        # one hot encoding
        targets = [0 for i in range(10)]
        targets[outputs] = 1

        #train the model
        neuralNetwork.Train(inputs, targets)

    trained = True
    print("Finish training the model")
train()

test1 = test_data_images[24]
testss = test_images[24]
prediction = neuralNetwork.FeedForward(test1)
print(prediction)
run = True
while run:
    screen.fill(backgroundColor)
    clock.tick(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    for x in range(28):
        for y in range(28):
            _x = x * pixelSize
            _y = y * pixelSize
            val = testss[y, x]
            color = (val, val, val)
            pygame.draw.rect(screen, color, pygame.Rect(_x + Xoffset, _y + Yoffset, pixelSize, pixelSize))

    pygame.display.update()

pygame.quit()
