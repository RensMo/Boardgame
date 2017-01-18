import pygame
import random

pygame.init()

class Button:
    def __init__(self, x, y, sx, sy, text, tx, ty):
        self.tx = tx
        self.ty = ty
        self.rect = pygame.Rect((int(x), int(y)), (int(sx), int(sy)))
        self.font = pygame.font.Font(None, int(sy * 0.8))
        self.text = self.font.render(text, 1, pygame.Color("Black"))

    def draw(self, surface):
        surface.fill(pygame.Color("Red"), self.rect)
        surface.blit(self.text, (self.tx, self.ty))

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)
        self.caption = "Button Test"
        self.color = pygame.Color("Grey")

        self.b1 = Button(self.width * 0.3, self.height * 0.2, self.width * 0.4, self.height * 0.1, "Change color", (self.width * 0.3) * 1.2, (self.height * 0.2) + 10)
        self.b2 = Button(self.width * 0.3, self.height * 0.6, self.width * 0.4, self.height * 0.1, "Quit", (self.width * 0.3) * 1.5, (self.height * 0.6) + 10)

        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

    def draw(self):
        self.screen.fill(self.color)

        self.b1.draw(self.screen)
        self.b2.draw(self.screen)

        pygame.display.update()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN and self.b1.rect.collidepoint(pygame.mouse.get_pos()):
                self.color = [random.randint(0, 255) for _ in range (3)]
            if event.type == pygame.MOUSEBUTTONDOWN and self.b2.rect.collidepoint(pygame.mouse.get_pos()):
                return True

        return False

    def game_loop(self):
        while not self.process_events():
            self.draw()

def program():
    game = Game()
    game.game_loop()

program()
