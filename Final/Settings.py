import pygame

from Image import *

class Toggle1:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.Is = [S3, S4]
        self.cc = 0
        self.I = self.Is[self.cc]
        self.I = pygame.transform.scale(self.I, (int(self.sx), int(self.sy)))
        self.irect = pygame.Rect((x,y), (self.sx, self.sy))
        self.rect1 = pygame.Rect((x,y), (self.sx * 0.5, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx * 0.5, y), (self.sx * 0.5, self.sy))

    def update(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.I = self.Is[self.cc]
        self.I = pygame.transform.scale(self.I, (int(self.sx), int(self.sy)))
        self.irect = pygame.Rect((x,y), (self.sx, self.sy))
        self.rect1 = pygame.Rect((x,y), (self.sx * 0.5, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx * 0.5, y), (self.sx * 0.5, self.sy))

    def draw(self, surface):
        surface.blit(self.I, (self.irect))

class Toggle2:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.Is = [S3, S4]
        self.cc = 1
        self.I = self.Is[self.cc]
        self.I = pygame.transform.scale(self.I, (int(self.sx), int(self.sy)))
        self.irect = pygame.Rect((x,y), (self.sx, self.sy))
        self.rect1 = pygame.Rect((x,y), (self.sx * 0.5, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx * 0.5, y), (self.sx * 0.5, self.sy))

    def update(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.I = self.Is[self.cc]
        self.I = pygame.transform.scale(self.I, (int(self.sx), int(self.sy)))
        self.irect = pygame.Rect((x,y), (self.sx, self.sy))
        self.rect1 = pygame.Rect((x,y), (self.sx * 0.5, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx * 0.5, y), (self.sx * 0.5, self.sy))

    def draw(self, surface):
        surface.blit(self.I, (self.irect))

class Resolution:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.Is = [S5, S6, S7]
        self.cc = 1
        self.I = self.Is[self.cc]
        self.I = pygame.transform.scale(self.I, (int(self.sx), int(self.sy)))
        self.irect = pygame.Rect((x,y), (self.sx, self.sy))
        self.rect1 = pygame.Rect((x,y), (self.sx * 0.5, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx * 0.5, y), (self.sx * 0.5, self.sy))

    def update(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.I = self.Is[self.cc]
        self.I = pygame.transform.scale(self.I, (int(self.sx), int(self.sy)))
        self.irect = pygame.Rect((x,y), (self.sx, self.sy))
        self.rect1 = pygame.Rect((x,y), (self.sx * 0.5, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx * 0.5, y), (self.sx * 0.5, self.sy))

    def draw(self, surface):
        surface.blit(self.I, (self.irect))