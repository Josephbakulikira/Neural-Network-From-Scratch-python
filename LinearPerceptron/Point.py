import pygame
from functions import *

class Point:
    def __init__(self, x, y, breed):
        self.x = x
        self.y = y
        self.bias = 1
        self.breed = breed
        self.color = (255, 255, 255)
        self.size = 10
        if self.breed == 1:
            self.color = (255, 1, 54)
        else:
            self.color = (1, 159, 255)
    def GetInputs(self):
        return [self.x, self.y, self.bias]

    def PixelCoordX(self):
        return translate(self.x, -1, 1, 0, width)
    def PixelCoordY(self):
        return translate(self.y, -1, 1, height, 0)

    def Display(self, screen):
        if self.breed == 1:
            x = self.PixelCoordX()
            y = self.PixelCoordY()
            pts = [ (x-self.size, y+self.size), (x, y - self.size), (x+self.size, y+self.size)]
            pygame.draw.polygon(screen, self.color, pts, 0)
        else:
            pygame.draw.circle(screen, self.color, (self.PixelCoordX(), self.PixelCoordY()), self.size)
