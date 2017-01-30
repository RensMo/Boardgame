import pygame
from Image import *

class Button:
    def __init__(self, x, y, sx, sy, I):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.I = I
        self.I = pygame.transform.scale(self.I, (int(sx), int(sy)))
        self.rect = pygame.Rect((x, y), (sx, sy))
        self.srect = pygame.Surface((int(sx), int(sy)))


    def draw(self, surface):
        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            surface.blit(self.I, (self.rect))
        elif self.rect.collidepoint(pygame.mouse.get_pos()):
            self.I = pygame.transform.scale(self.I, (int(self.sx * 1.02), int(self.sy * 1.02)))
            self.rect = pygame.Rect((int(self.x - (self.sx * 1.02 - self.sx)), int(self.y - (self.sy * 1.02 - self.sy))), (int(self.sx), int(self.sy)))
            self.srect = pygame.Surface((int(self.sx * 1.02), int(self.sy * 1.04)))
            self.srect.fill(pygame.Color("Black"))
            self.srect.set_alpha(68)
            surface.blit(self.srect, (int(self.x), int(self.y)))
            surface.blit(self.I, (self.rect))
 
class Button2:
    def __init__(self, x, y, sx, sy, I):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.I = I
        self.I = pygame.transform.scale(self.I, (int(sx), int(sy)))
        self.rect = pygame.Rect((x, y), (sx, sy))




def draw(self, surface):
    if not self.rect.collidepoint(pygame.mouse.get_pos()):
            surface.blit(self.I, (self.rect))
    elif self.rect.collidepoint(pygame.mouse.get_pos()):
        self.I = pygame.transform.scale(self.I, (int(self.sx * 1.05), int(self.sy * 1.05)))
        self.rect = pygame.Rect((int(self.x - (self.sx * 1.025 - self.sx)), int(self.y - (self.sy * 1.025 - self.sy))), (int(self.sx), int(self.sy)))
        surface.blit(self.I, (self.rect))



