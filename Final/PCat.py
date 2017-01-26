import pygame
from Image import *

class PCat:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.cats = [IC1, IC2, IC3, IC4]
        self.cc = 0
        self.I = self.cats[self.cc]
        self.I = pygame.transform.scale(self.I, (int(self.sx), int(self.sy)))
        self.irect = pygame.Rect((x,y), (self.sx, self.sy))
        self.rect1 = pygame.Rect((x,y), (self.sx * 0.5, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx * 0.5, y), (self.sx * 0.5, self.sy))

    def update(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.I = self.cats[self.cc]
        self.I = pygame.transform.scale(self.I, (int(self.sx), int(self.sy)))

    def draw(self, surface):
        surface.blit(self.I, (self.irect))
