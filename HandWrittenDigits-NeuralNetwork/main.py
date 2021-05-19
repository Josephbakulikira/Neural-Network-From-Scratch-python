import pygame
import idx2numpy
import numpy as np
import time
from Network import *
from Matrix import *
from constants import *
from ui import *
from scipy.interpolate import RegularGridInterpolator
from math import floor
import pickle

#pygame configurations
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HandWritten digits Neural Network")
clock = pygame.time.Clock()

brush1 = pygame.image.load("Brush/brush1.png")
brush2 = pygame.image.load("Brush/brush2.png")
brush = pygame.transform.scale(brush2, (128, 128))

fps = 60

Message = TextUI("Preparing the data and training the model, This might take a couple of minute,", (width//2, 80), (255,255, 255))
Message.Render(screen)
pygame.display.update()


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
number_of_training_data = 100
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
percent = 0

def regrid(data, out_x, out_y):
    m = max(data.shape[0], data.shape[1])
    y = np.linspace(0, 1.0/m, data.shape[0])
    x = np.linspace(0, 1.0/m, data.shape[1])
    interpolating_function = RegularGridInterpolator((y, x), data)

    yv, xv = np.meshgrid(np.linspace(0, 1.0/m, out_y), np.linspace(0, 1.0/m, out_x))

    return interpolating_function((xv, yv))

def trainEpoch():
    for i in range(len(train_data_images)):
        inputs = train_data_images[i]
        outputs = train_labels[i]
        #one hot encoding
        targets = [0 for i in range(10)]
        targets[outputs] = 1
        #train the model
        neuralNetwork.Train(inputs, targets)

    print("epoch training finished")

#trainEpoch()

#save our trained model
filename = 'trainedModel'
#pickle.dump(neuralNetwork, open(filename, 'wb'))

#load the saved trained model
neuralNetwork = pickle.load(open(filename, 'rb'))

def testModel():
    correctGuess = 0
    percentage = 0
    for i in range(len(test_data_images)):
        inputs = test_data_images[i]
        label = test_labels[i]
        #one hot encoding
        targets = [0 for i in range(10)]
        targets[label] = 1
        guess = neuralNetwork.Predict(inputs)
        _max = max(guess)
        classification =guess.index(_max)

        if classification == label:
            correctGuess+= 1

        percentage = correctGuess/len(test_data_images)


    print("test model finished")
    return percentage * 100
percent = testModel()



offset = (width//2 - 280, height//2 - 280)
screen.fill((0, 0, 0))
pygame.draw.rect(screen, (255,255, 255), pygame.Rect(offset[0], offset[1],560, 560))

Message.text = ("Press 'S' or 'SPACE' to Guess the Digits")
Message.fontSize = 25
Message.Render(screen)


#ui parameters
perc = TextUI("Accuracy: 0 ", (width//2, height-150), (74, 55, 212))
perc.fontSize = 30
perc.text = f"Accuracy: {percent} %"
perc.Render(screen)
PredictionText = TextUI("Prediction: ? ", (width//2, 180), (255, 255, 255))
PredictionText.fontSize = 40

ResetButton = Button("Reset", (width - 140,100))
ResetButton.borderColor=  (0, 0, 0)

RunButton = Button("Run", (width//2-60, height - 150))
RunButton.borderColor=  (0, 0, 0)
array2d = []

testArray = np.empty((560, 560))
drawArray = []
#drawArray = test_images[0]
#print(neuralNetwork.Predict(test_data_images[0]))



ad = []
temp = []
run = True
Start = False
z = 0
while run:
    #screen.fill(backgroundColor)

    clock.tick(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_s or event.key == pygame.K_SPACE:
                Start = True


        if event.type == pygame.MOUSEBUTTONDOWN:
            z = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            z = 0

    if ResetButton.state == True:
        drawArray = []
        ad = []
        temp = np.empty((28, 28))
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255,255, 255), pygame.Rect(offset[0], offset[1],560, 560))

        #ui parameters
        PredictionText = TextUI("Prediction: ? ", (width//2, 180), (255, 255, 255))
        Message.Render(screen)
        perc.text = f"Accuracy: {percent}"
        perc.Render(screen)

    if Start == True:
        Start = False
        ad = []
        drawArray = []
        temp = np.empty((28, 28))
        for x in range(width):
            for y in range(height):
                if x >= offset[0] and x < offset[0] + 560:
                    if y >= offset[1] and y < offset[1] + 560:
                        _color = screen.get_at((x,y))
                        average_color = (255 - ( (_color[0] + _color[1] + _color[2])/3) )/ 255
                        testArray[x - offset[0]][y-offset[1]] = average_color
        #reshaping the array from 560 to 28
        ad = regrid( testArray, 28, 28)

        for x in range(28):
            for y in range(28):
                temp[x][y] = ad[y][x]
        for x in range(28):
            for y in range(28):
                drawArray.append(temp[x][y])
        #drawArray = ad
        print('\n')
        _predict = neuralNetwork.Predict(drawArray)
        PredictionText.text = f'Prediction: {_predict.index(max(_predict))}'
        PredictionText.Render(screen)
        print(_predict)

    if len(drawArray) > 0:
        for x in range(28):
            for y in range(28):
                val = int(ad[x][y] * 255)
                pygame.draw.rect(screen, (val, val, val), pygame.Rect(x * 10, y * 10 + 400, 10, 10))


    mx, my = pygame.mouse.get_pos()
    if z == 1:
        # 64 is the half of the size of the brush sprite
        if mx > offset[0] and mx < offset[0] + 560:
            if my > offset[1] and my < offset[1] + 560:
                screen.blit(brush, (mx - 64, my - 64))



    ResetButton.HandleMouse()

    ResetButton.Render(screen)

    pygame.display.update()

pygame.quit()
