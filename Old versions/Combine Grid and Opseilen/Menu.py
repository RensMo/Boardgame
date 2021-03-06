import pygame

from Button import *
from Image import *

class Menu:
    def __init__(self, x, y, I):
        self.x = x
        self.y = y
        self.I = I
        self.I = pygame.transform.scale(self.I, (int(x), int(y)))
        self.rect = pygame.Rect((0,0), (x, y))

        self.B1 = Button(self.x * 0.12, self.y * 0.29, self.x * 0.23, self.y * 0.14, I1)
        self.B2 = Button(self.x * 0.12, self.y * 0.44, self.x * 0.23, self.y * 0.14, I2)
        self.B3 = Button(self.x * 0.12, self.y * 0.59, self.x * 0.23, self.y * 0.14, I3)
        self.B4 = Button(self.x * 0.12, self.y * 0.74, self.x * 0.23, self.y * 0.14, I4)

    def draw(self, surface):
        surface.blit(self.I, (self.rect))
        self.B1.draw(surface)
        self.B2.draw(surface)
        self.B3.draw(surface)
        self.B4.draw(surface)

class Backg:
    def __init__(self, x, y, I):
        self.x = x
        self.y = y
        self.I = I
        self.I = pygame.transform.scale(self.I, (int(x), int(y)))
        self.rect = pygame.Rect((0, 0), (x, y))

    def draw(self, surface):
        surface.blit(self.I, (self.rect))

