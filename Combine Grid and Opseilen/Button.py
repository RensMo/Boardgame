import pygame

class Button:
    def __init__(self, x, y, sx, sy, I):
        self.x = x
        self.y = y
        self.I = I
        self.I = pygame.transform.scale(self.I, (int(sx), int(sy)))
        self.rect = pygame.Rect((x, y), (sx, sy))
        self.srect = pygame.Surface((int(sx), int(sy)))

    def draw(self, surface):
        surface.blit(self.I, (self.rect))
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.srect.fill(pygame.Color("Black"))
            self.srect.set_alpha(68)
            surface.blit(self.srect, (self.x, self.y))
