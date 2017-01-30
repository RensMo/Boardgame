import pygame

class PColor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sx = (x * 0.49) // 2
        self.sy = x * 0.7
        self.colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]
        self.cc = 0
        self.color = self.colors[self.cc]
        self.rect1 = pygame.Rect((x, y), (self.sx, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx, y), (self.sx, self.sy))

    def update(self, x, y):
        self.x = x
        self.y = y
        self.sx = (x * 0.49) // 2
        self.sy = x * 0.07
        self.rect1 = pygame.Rect((x, y), (self.sx, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx, y), (self.sx, self.sy))
        self.color = self.colors[self.cc]

    def draw(self, surface):
        surface.fill(self.color, self.rect1)
        surface.fill(self.color, self.rect2)