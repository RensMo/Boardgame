import pygame


class Font:
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 24)

class Text:
    def __init__(self, x, y, sx, sy, I):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.I = I
        self.I = pygame.transform.scale(self.I, (int(sx), int(sy)))
        self.rect = pygame.Rect((x,y), (sx,sy))
        self.screct = pygame.Surface((int(sx), int(sy)))

    def draw(self, surface):
        surface.blit(self.I, (self.rect))

