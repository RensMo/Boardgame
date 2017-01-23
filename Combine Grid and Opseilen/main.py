import pygame
from pygame.locals import *

from Button import *
from Menu import *
from Player import *
from Tile import *

class Game:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.size = (self.width, self.height)
        self.caption = "Opseilen"

        self.S0 = [1, 0]

        pygame.init()

        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption(self.caption)

        grid_width = 8
        grid_height = 12
        self.entry_tile = build_square_matrix(grid_width, grid_height)

        self.P1 = Player("Rens", self.entry_tile)

    def draw(self):
        if self.S0[0] == 1:
            self.M1.draw(self.screen)
        if self.S0[1] == 1:
            # Create background colour and back button
            self.screen.fill((pygame.Color("Light Blue")))
            self.B1.draw(self.screen)

            # Draw grid
            self.entry_tile.Draw(self.screen)

            # Update Player
            self.P1.Update()
            self.P1.Draw(self.screen)

        pygame.display.update()

    def process_events(self):
        keys = pygame.key.get_pressed()

        self.B1 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I4)
        self.M1 = Menu(self.width, self.height, I0)

        for event in pygame.event.get():
            if event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                self.width = event.dict['size'][0]
                self.height = event.dict['size'][1]
            if event.type == pygame.QUIT:
                return True
            if keys[pygame.K_LCTRL] and keys[pygame.K_w]:
                return True
            if event.type == pygame.MOUSEBUTTONUP:
                if self.B1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1:
                    self.S0 = [1, 0]
                if self.M1.B1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    self.S0 = [0, 1]
                if self.M1.B4.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    return True

        return False

    def game_loop(self):
        while not self.process_events():
            self.draw()

def run():
    game = Game()
    game.game_loop()

run()

pygame.quit()