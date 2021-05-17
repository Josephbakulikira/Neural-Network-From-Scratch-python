import pygame
from functions import *

class Point:
    def __init__(self, x, y, breed):
        self.x = x
        self.y = y
        self.bias = 1
        self.breed = breed
        self.color = (255, 255, 255)

        if self.breed == 1:
            self.color = (255, 1, 54)
        else:
            self.color = (136, 255, 1)
    def GetInputs(self):
        return [self.x, self.y, self.bias]

    def PixelCoordX(self):
        return translate(self.x, -1, 1, 0, width)
    def PixelCoordY(self):
        return translate(self.y, -1, 1, height, 0)

    def Display(self, screen):
        pygame.draw.circle(screen, self.color, (self.PixelCoordX(), self.PixelCoordY()), 15, 3)
