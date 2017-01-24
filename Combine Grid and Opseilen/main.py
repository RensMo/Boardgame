import pygame
from pygame.locals import *

from Button import *
from Menu import *
from Player import *
from Tile import *
from Text import *
from Image import *

class Game:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.size = (self.width, self.height)
        self.caption = "Opseilen"
        self.S0 = [1, 0, 0, 0]
        self.help_pages = 2
        self.help_pagenr = 0
        self.play_pages = 3
        self.play_pagenr = 0

        pygame.init()

        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption(self.caption)

        grid_width = 8
        grid_height = 15
        self.entry_tile = build_square_matrix(grid_width, grid_height)

        self.P1 = Player("Rens", self.entry_tile)

    def draw(self):
        # Menu
        if self.S0[0] == 1:
            self.M1.draw(self.screen)
        # Play
        if self.S0[1] == 1:
            if self.play_pagenr == 0:
                self.Pbg1.draw(self.screen)
                self.B1.draw(self.screen)
                self.PL2.draw(self.screen)
                self.PL3.draw(self.screen)
                self.PL4.draw(self.screen)
            if self.play_pagenr == 1:
                self.Pbg2.draw(self.screen)
                self.B1.draw(self.screen)
            elif self.play_pagenr == 2:
                self.screen.fill((pygame.Color("Light Green")))
                self.B1.draw(self.screen)
                # Draw grid
                self.entry_tile.Draw(self.screen, self.width * 0.028, self.height * 0.05)
                # Update Player
                self.P1.Update()
                self.P1.Draw(self.screen, self.width * 0.028, self.height * 0.05)
            self.Next2.draw(self.screen)
            self.Prev2.draw(self.screen)
        # Help
        if self.S0[2] == 1:
            if self.help_pagenr == 0:
                self.screen.fill((pygame.Color("Light Blue")))
            if self.help_pagenr == 1:
                self.screen.fill((pygame.Color("Purple")))
            elif self.help_pagenr == 2:
                self.screen.fill((pygame.Color("Red")))
            self.B2.draw(self.screen)
            self.Next1.draw(self.screen)
            self.Prev1.draw(self.screen)
            self.Text1.draw(self.screen)
        # Settings
        if self.S0[3] == 1:
            self.screen.fill((pygame.Color("Yellow")))
            self.B3.draw(self.screen)

        pygame.display.update()



    def process_events(self):
        keys = pygame.key.get_pressed()

        self.M1 = Menu(self.width, self.height, I0)
        self.Pbg1 = Backg(self.width, self.height, I12)
        self.Pbg2 = Backg(self.width, self.height, I13)
        self.B1 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.B2 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.B3 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.Next1 = Button(self.width * 0.88, self.height * 0.90, self.width * 0.1, self.height * 0.07, I6)
        self.Next2 = Button(self.width * 0.88, self.height * 0.90, self.width * 0.1, self.height * 0.07, I6)
        self.Prev1 = Button(self.width * 0.77, self.height * 0.90, self.width * 0.1, self.height * 0.07, I7)
        self.Prev2 = Button(self.width * 0.77, self.height * 0.90, self.width * 0.1, self.height * 0.07, I7)
        self.Text1 = Text(self.width * 0.02, self.height * 0.15, self.width * 0.95, self.height * 0.7, I8)
        self.PL2 = Button(self.width * 0.425, self.height * 0.22, self.width * 0.15, self.height * 0.15, I9)
        self.PL3 = Button(self.width * 0.425, self.height * 0.43, self.width * 0.15, self.height * 0.16, I10)
        self.PL4 = Button(self.width * 0.425, self.height * 0.64, self.width * 0.15, self.height * 0.17, I11)

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
            if event.type == pygame.MOUSEBUTTONUP:
                if self.Next2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1:
                    if self.play_pagenr < self.help_pages:
                        self.play_pagenr += 1
                if self.Prev2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1:
                    if self.play_pagenr > 0:
                        self.play_pagenr -= 1
                if self.Next1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[2] == 1:
                    if self.help_pagenr < self.help_pages:
                        self.help_pagenr += 1
                if self.Prev1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[2] == 1:
                    if self.help_pagenr > 0:
                        self.help_pagenr -= 1
                if self.B1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1:
                    self.S0 = [1, 0, 0, 0]
                    self.play_pagenr = int(0)
                if self.B2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[2] == 1:
                    self.S0 = [1, 0, 0, 0]
                    self.help_pagenr = int(0)
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

def run():
    game = Game()
    game.game_loop()

run()

pygame.quit()
