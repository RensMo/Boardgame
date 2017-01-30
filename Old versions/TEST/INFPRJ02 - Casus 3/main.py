import random

import pygame
from pygame.locals import *

from Button import *
from Dice import *
from Menu import *
from Player import *
from Tile import *


class Game:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.size = (self.width, self.height)
        self.caption = "Old versions"

        self.S0 = [1, 0, 0, 0]

        pygame.init()

        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()

        grid_width = 8
        grid_height = 15
        self.entry_tile = build_square_matrix(grid_width, grid_height)

        self.P1 = Player("Rens", self.entry_tile)
        self.D1 = Dice(self.width * 0.5, self.height * 0.5, self.width * 0.1, self.width * 0.1)

    def draw(self):
        if self.S0[0] == 1:
            self.M1.draw(self.screen)
        if self.S0[1] == 1:
            self.screen.fill((pygame.Color("Light Green")))
            self.B1.draw(self.screen)
            # Draw grid
            self.entry_tile.Draw(self.screen, self.width * 0.028, self.height * 0.05)

            # Update Player
            self.P1.Update()
            self.P1.Draw(self.screen, self.width * 0.028, self.height * 0.05)
            self.D1.update(self.screen_rect)
            self.D1.draw(self.screen)
            self.D1.vel(self.width, self.height)
        if self.S0[2] == 1:
            self.screen.fill((pygame.Color("Light Blue")))
            self.B2.draw(self.screen)
            self.H1.draw(self.screen)
            self.H2.draw(self.screen)
        if self.S0[3] == 1:
            self.screen.fill((pygame.Color("Yellow")))
            self.B3.draw(self.screen)

        pygame.display.update()

    def process_events(self):
        keys = pygame.key.get_pressed()

        self.B1 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.B2 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.B3 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.H1 = Button(self.width * 0.88, self.height * 0.84, self.width * 0.1, self.height * 0.07, I6)
        self.H2 = Button(self.width * 0.77, self.height * 0.84, self.width * 0.1, self.height * 0.07, I7)
        self.M1 = Menu(self.width, self.height, I0)
        self.screen_rect = self.screen.get_rect()

        for event in pygame.event.get():
            if event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                self.width = event.dict['size'][0]
                self.height = event.dict['size'][1]
            if event.type == pygame.QUIT:
                return True
            if keys[pygame.K_LCTRL] and keys[pygame.K_w]:
                return True
            if keys[pygame.K_LALT] and keys[pygame.K_F4]:
                return True
            if keys[pygame.K_ESCAPE]:
                if self.S0[1] == 1 or self.S0[2] == 1 or self.S0[3] == 1:
                    self.S0 = [1, 0, 0, 0]
            if keys[pygame.K_r]:
                self.D1
                self.D1 = Dice(self.width * 0.5, self.height * 0.5, self.width * 0.1, self.width * 0.1)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.D1.rc == 0:
                self.D1.check_click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.D1.click = False
                if self.D1.rc == 1:
                    self.D1.rc = 2
                if self.D1.rc == 3 and self.D1.vcc < 30:
                    self.D1.rc = 0
                    self.D1.vcc = 0
                if self.B1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1:
                    self.S0 = [1, 0, 0, 0]
                if self.B2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[2] == 1:
                    self.S0 = [1, 0, 0, 0]
                if self.H1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[2] == 1:
                    self.S0 = [1, 0, 0, 0]
                if self.H2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[2] == 1:
                    self.S0 = [1, 0, 0, 0]
                if self.B3.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    self.S0 = [1, 0, 0, 0]
                if self.M1.B1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    self.S0 = [0, 1, 0, 0]
                if self.M1.B2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    self.S0 = [0, 0, 1, 0]
                if self.M1.B3.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    self.S0 = [0, 0, 0, 1]
                if self.M1.B4.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    return True

        return False

    def game_loop(self):
        while not self.process_events():
            self.draw()
            self.clock.tick(60)

def run():
    game = Game()
    game.game_loop()

run()

pygame.quit()
