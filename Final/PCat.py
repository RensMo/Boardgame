import pygame

class PCat:
    def __init__(self, x, y, I):
        self.x = x
        self.y = y
        self.sx = x * 0.49
        self.sy = x * 0.05
        self.cats = []
        self.cc = 0
        self.I = self.cats[self.cc]
        self.I = pygame.transform.scale(self.I, (int(self.sx), int(self.sy)))
        self.rect = pygame.Rect((x, y), (self.sx, self.sy))
        self.rect1 = pygame.Rect((x, y), (self.sx * 0.5, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx, y), (self.sx * 0.5, self.sy))

    def update(self, x, y):
        self.x = x
        self.y = y
        self.sx = x * 0.49
        self.sy = x * 0.05
        self.rect = pygame.Rect((x, y), (self.sx, self.sy))
        self.rect1 = pygame.Rect((x, y), (self.sx * 0.5, self.sy))
        self.rect2 = pygame.Rect((self.x + self.sx, y), (self.sx * 0.5, self.sy))
        self.I = self.cats[self.cc]

    def draw(self, surface):
        surface.blit(self.I, (self.rect))