import pygame
from constants import *

class Button:
    def __init__(self, text, position = (width-230, 600) , w = 100, h= 50, border=10, color = (0, 0, 0), borderColor = (0, 0, 0)):
        self.text = text
        self.position = position
        self.w = w
        self.h = h
        self.border = border
        self.temp = color
        self.color = color
        self.borderColor = borderColor
        self.font = 'freesansbold.ttf'
        self.fontSize = 25
        self.textColor = (255, 255, 255)
        self.state = False
        self.action = None

    def HandleMouse(self, HoverColor = (100, 100, 100)):
        m = pygame.mouse.get_pos()
        self.state = False
        if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
            if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                self.color = HoverColor
                if pygame.mouse.get_pressed()[0]:
                    self.color = (200, 200, 200)
                    if self.action == None:
                        self.state = True
            else:
                self.color = self.temp
        else:
            self.color = self.temp


    def Render(self, screen):
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.textColor)
        textRect = text.get_rect()
        textRect.center = (self.position[0]+self.w//2, self.position[1]+self.h//2)
        if self.border > 0:
            pygame.draw.rect(screen, self.borderColor, pygame.Rect(self.position[0] - self.border//2, self.position[1] - self.border//2, self.w + self.border, self.h + self.border))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))

        screen.blit(text, textRect)

class Panel:
    def __init__(self, position = (width-350, 100), w= 345, h= 500, color=(8, 3, 12)):
        self.position = position
        self.w = w
        self.h = h
        self.color = color

    def Render(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))

class ToggleButton:
    def __init__(self, position= ((width-200, 400)), w = 30, h=30, state=False, color=(40, 40, 10), activeColor=(240, 140, 60)):
        self.position = position
        self.w = w
        self.h = h
        self.state = state
        self.temp = (activeColor, color)
        self.activeColor = activeColor
        self.color = color

    def HandleMouse(self, HoverColor = (150, 120, 40)):
        m = pygame.mouse.get_pos()

        if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
            if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                self.color = HoverColor
                self.activeColor = HoverColor
                if pygame.mouse.get_pressed()[0]:
                    self.state = not self.state
                    self.color = (255, 255, 255)
            else:
                self.color = self.temp[1]
                self.activeColor =self.temp[0]
        else:
            self.color = self.temp[1]
            self.activeColor =self.temp[0]

    def Render(self, screen):

        if self.state == True:
            pygame.draw.rect(screen, self.activeColor, pygame.Rect(self.position[0], self.position[1], self.w, self.h))
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))

class TextUI:
    def __init__(self,text, position, fontColor):
        self.position = position
        self.text = text
        self.font = 'freesansbold.ttf'
        self.fontSize = 18
        self.fontColor = fontColor
    def Render(self, screen):
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.fontColor)
        textRect = text.get_rect()
        textRect.center = (self.position[0], self.position[1])
        screen.blit(text, textRect)

class DigitInput:
    def __init__(self,startingValue, position = (width-320, 100), w= 300, h= 600, color=(8, 3, 12)):
        self.position = position
        self.text = str(startingValue)
        self.fontColor = (255, 255, 255)
        self.fontSize = 18
        self.font = 'freesansbold.ttf'
        self.w = w
        self.h = h
        self.color = color
        self.value  = int(self.text)
        self.hoverEnter = False

    def Check(self, backspace,val):

        if self.hoverEnter == True:
            if backspace == True:

                if len(str(self.value)) <= 0 or len(str(self.value))-1 <= 0:
                    self.value = 0
                else:
                    self.value = int(str(self.value)[:-1])

            else:
                if self.text.isdigit():
                    self.value = int(str(self.value) + str(self.text))
                else:
                    for el in self.text:
                        if el.isdigit() != True:
                            self.text = self.text.replace(el, "")
        backspace == False
        self.text = ""




    def updateText(self, val, pressed):
        m = pygame.mouse.get_pos()
        if m[0] >= self.position[0] and m[0] <= self.position[0] + self.w:
            if m[1] >= self.position[1] and m[1] <= self.position[1] + self.h:
                self.hoverEnter = True
                if pressed == True:
                    self.text += val
            else:
                self.hoverEnter = False
                val = ""
        else:
            self.hoverEnter = False
            val = ""


    def Render(self, screen, val, backspace, pressed):
        self.updateText(val, pressed)
        self.Check(backspace, val)
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(str(self.value), True, self.fontColor)
        textRect = text.get_rect()
        textRect.center = (self.position[0]+self.w//2, self.position[1]+self.h//2)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.w, self.h))
        screen.blit(text, textRect)

class Slider:
    def __init__(self,x, y, val, min1, max1, length, h):
        self.value = val
        self.x = x
        self.y = y
        self.h = h
        self.min1 = min1
        self.max1 = max1
        self.length = length
        self.lineColor = (20, 10, 20)
        self.rectradius = 15
        self.temp_radius = self.rectradius
        self.rectColor = (255, 255, 255)
        self.v = 0.4
        self.temp = self.lineColor
    def Calculate(self, val):
        self.v = translate(val, 0, self.length, 0, 1)
        self.value = self.v * 100
    def HandleMouse(self):

        mx, my = pygame.mouse.get_pos()
        if mx >= self.x and mx <= self.x + self.length:
            if my >= self.y and my <= self.y + self.h:
                self.rectradius = 22
                self.Calculate(mx - self.x)
            else:
                self.lineColor = self.temp
                self.rectradius = self.temp_radius
        else:
            self.lineColor = self.temp
            self.rectradius = self.temp_radius

    def Render(self,screen):
        pygame.draw.rect(screen, self.lineColor, pygame.Rect(self.x, self.y, self.length, self.h))
        x = int((self.v * self.length) + self.x)
        pygame.draw.rect(screen, self.rectColor, pygame.Rect(self.x, self.y, int( self.v * self.length), self.h))
        pygame.draw.circle(screen, self.rectColor, (x, self.y), self.rectradius)
