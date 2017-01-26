import random

import pygame
from pygame.locals import *

from Button import *
from Menu import *
from Player import *
from Tile import *
from Text import *
from Image import *
from Dice import *
from IText import *
from PColor import *

class Game:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.size = (self.width, self.height)
        self.caption = "Old versions"
        self.S0 = [1, 0, 0, 0]
        self.help_pages = 2
        self.help_pagenr = 0
        self.play_pages = 3
        self.play_pagenr = 0
        self.players = 0

        pygame.init()

        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()

        self.entry_tile = build_matrix()

        self.P1 = Player("", self.entry_tile)
        self.D1 = Dice(self.width * 0.5, self.height * 0.5, self.width * 0.1, self.width * 0.1, ID1)
        self.T1_1 = IText(self.width * 0.031, self.height * 0.145, "#1", 40, 0)
        self.T1_2 = IText(self.width * 0.095, self.height * 0.145, "", 40, 390)
        self.T2_1 = IText(self.width * 0.031, self.height * 0.245, "#2", 40, 0)
        self.T2_2 = IText(self.width * 0.095, self.height * 0.245, "", 40, 390)
        self.T3_1 = IText(self.width * 0.031, self.height * 0.345, "#3", 40, 0)
        self.T3_2 = IText(self.width * 0.095, self.height * 0.345, "", 40, 390)
        self.T4_1 = IText(self.width * 0.031, self.height * 0.445, "#4", 40, 0)
        self.T4_2 = IText(self.width * 0.095, self.height * 0.445, "", 40, 390)
        self.P1C = PColor(self.width * 0.55, self.height * 0.2)

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
                self.Next2.draw(self.screen)
            if self.play_pagenr == 1:
                self.Pbg2.draw(self.screen)
                if self.players == 2:
                    self.T1_1.draw(self.screen)
                    self.T1_2.draw(self.screen)
                    self.T2_1.draw(self.screen)
                    self.T2_2.draw(self.screen)
                    self.P1C.update(self.width * 0.55, self.height * 0.2)
                    self.P1C.draw(self.screen)
                if self.players == 3:
                    self.T1_1.draw(self.screen)
                    self.T1_2.draw(self.screen)
                    self.T2_1.draw(self.screen)
                    self.T2_2.draw(self.screen)
                    self.T3_1.draw(self.screen)
                    self.T3_2.draw(self.screen)
                if self.players == 4:
                    self.T1_1.draw(self.screen)
                    self.T1_2.draw(self.screen)
                    self.T2_1.draw(self.screen)
                    self.T2_2.draw(self.screen)
                    self.T3_1.draw(self.screen)
                    self.T3_2.draw(self.screen)
                    self.T4_1.draw(self.screen)
                    self.T4_2.draw(self.screen)
                self.B1.draw(self.screen)
                self.Next2.draw(self.screen)
                self.Prev2.draw(self.screen)
            if self.play_pagenr == 2:
                self.Pbg3.draw(self.screen)
                self.B1.draw(self.screen)
                # Draw grid
                self.entry_tile.Draw(self.screen, self.width * 0.028, self.height * 0.05, self.width * 0.2197, self.height * 0.9)
                # Update Player
                self.P1.Update()
                self.P1.Draw(self.screen, self.width * 0.028, self.height * 0.05, self.width * 0.2197, self.height *0.9)
                self.CD_L.draw(self.screen)
                self.TD_L.draw(self.screen)
                self.AR_L.draw(self.screen)
                self.AR_R.draw(self.screen)
                self.AR_U.draw(self.screen)
                self.D1.update(self.screen_rect)
                self.D1.draw(self.screen, self.width * 0.1, self.width * 0.1)
                self.D1.vel(self.width, self.height)
                self.Next2.draw(self.screen)
                self.Prev2.draw(self.screen)
            elif self.play_pagenr == 3:
                self.Pbg3.draw(self.screen)
                self.B1.draw(self.screen)
                # Draw grid
                self.entry_tile.Draw(self.screen, self.width * 0.028, self.height * 0.05, self.width * 0.2197, self.height * 0.9)
                # Update Player
                self.P1.Update()
                self.P1.Draw(self.screen, self.width * 0.028, self.height * 0.05, self.width * 0.2197, self.height *0.9)
                self.CD_L.draw(self.screen)
                self.TD_L.draw(self.screen)
                self.AR_L.draw(self.screen)
                self.AR_R.draw(self.screen)
                self.AR_U.draw(self.screen)
                self.D1.update(self.screen_rect)
                self.D1.draw(self.screen, self.width * 0.1, self.width * 0.1)
                self.D1.vel(self.width, self.height)
                self.Q.draw(self.screen)
        # Help
        if self.S0[2] == 1:
            self.Helpbg.draw(self.screen)
            if self.help_pagenr == 0:
                self.Text1.draw(self.screen)
                self.Next1.draw(self.screen)
            if self.help_pagenr == 1:
                self.Text2.draw(self.screen)
                self.Next1.draw(self.screen)
                self.Prev1.draw(self.screen)
            elif self.help_pagenr == 2:
                self.Text3.draw(self.screen)
                self.Prev1.draw(self.screen)
            self.B2.draw(self.screen)
        # Settings
        if self.S0[3] == 1:
            self.screen.fill((pygame.Color("Yellow")))
            self.B3.draw(self.screen)


        pygame.display.update()



    def process_events(self):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        self.M1 = Menu(self.width, self.height, BG0)
        self.Pbg1 = Backg(self.width, self.height, BG1)
        self.Pbg2 = Backg(self.width, self.height, BG2)
        self.Pbg3 = Backg(self.width, self.height, BG4)
        self.Helpbg = Backg(self.width, self.height, BG3)
        self.Q = Backg(self.width, self.height, I19)
        self.B1 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.B2 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.B3 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.Next1 = Button(self.width * 0.88, self.height * 0.90, self.width * 0.1, self.height * 0.07, I6)
        self.Next2 = Button(self.width * 0.88, self.height * 0.90, self.width * 0.1, self.height * 0.07, I6)
        self.Prev1 = Button(self.width * 0.77, self.height * 0.90, self.width * 0.1, self.height * 0.07, I7)
        self.Prev2 = Button(self.width * 0.77, self.height * 0.90, self.width * 0.1, self.height * 0.07, I7)
        self.PL2 = Button(self.width * 0.425, self.height * 0.22, self.width * 0.15, self.height * 0.15, I9)
        self.PL3 = Button(self.width * 0.425, self.height * 0.43, self.width * 0.15, self.height * 0.16, I10)
        self.PL4 = Button(self.width * 0.425, self.height * 0.64, self.width * 0.15, self.height * 0.17, I11)
        self.Text1 = Textbg(self.width * 0.02, self.height * 0.15, self.width * 0.95, self.height * 0.7, HELP1)
        self.Text2 = Textbg(self.width * 0.02, self.height * 0.15, self.width * 0.95, self.height * 0.7, HELP2)
        self.Text3 = Textbg(self.width * 0.02, self.height * 0.15, self.width * 0.95, self.height * 0.7, HELP3)
        self.CD = Textbg(self.width * 0.77, self.height * 0.455, self.width * 0.19, self.height * 0.05, I12)
        self.CD_L = Textbg(self.width * 0.77, self.height * 0.455, self.width * 0.19, self.height * 0.05, I13)
        self.TD = Textbg(self.width * 0.77, self.height * 0.755, self.width * 0.19, self.height * 0.05, I14)
        self.TD_L = Textbg(self.width * 0.77, self.height * 0.755, self.width * 0.19, self.height * 0.05, I15)
        self.AR_L = Button(self.width * 0.76, self.height * 0.88, self.width * 0.065, self.height * 0.085, I16)
        self.AR_R = Button(self.width * 0.90, self.height * 0.88, self.width * 0.065, self.height * 0.085, I17)
        self.AR_U = Button(self.width * 0.83, self.height * 0.82, self.width * 0.065, self.height * 0.085, I18)

        self.screen_rect = self.screen.get_rect()
        self.T1_1.update(events, self.width * 0.031, self.height * 0.145, 40, 0)
        self.T1_2.update(events, self.width * 0.095, self.height * 0.145, 40, 390)
        self.T2_1.update(events, self.width * 0.031, self.height * 0.245, 40, 0)
        self.T2_2.update(events, self.width * 0.095, self.height * 0.245, 40, 390)
        self.T3_1.update(events, self.width * 0.031, self.height * 0.345, 40, 0)
        self.T3_2.update(events, self.width * 0.095, self.height * 0.345, 40, 390)
        self.T4_1.update(events, self.width * 0.031, self.height * 0.445, 40, 0)
        self.T4_2.update(events, self.width * 0.095, self.height * 0.445, 40, 390)

        for event in events:
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
                    self.play_pagenr = int(0)
                    self.help_pagenr = int(0)
            if keys[pygame.K_r]:
                self.D1 = Dice(self.width * 0.5, self.height * 0.5, self.width * 0.1, self.width * 0.1, ID1)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.D1.rc == 0:
                    self.D1.check_click(event.pos)
                if self.T1_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T1_2.focus = 1
                if not self.T1_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T1_2.focus = 0
                if self.T2_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T2_2.focus = 1
                if not self.T2_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T2_2.focus = 0
                if self.T3_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T3_2.focus = 1
                if not self.T3_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T3_2.focus = 0
                if self.T4_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T4_2.focus = 1
                if not self.T4_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T4_2.focus = 0
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.D1.click = False
                if self.D1.rc == 1:
                    self.D1.rc = 2
                if self.Next2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1 and self.play_pagenr != 3:
                    if self.play_pagenr < self.play_pages:
                        self.play_pagenr += 1
                        if self.play_pagenr == 2:
                            self.P1.Name = self.T1_2
                            print(self.P1.Name)
                if self.Prev2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1 and self.play_pagenr != 3:
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
                if self.PL2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 0:
                    if self.play_pagenr < self.help_pages:
                        self.play_pagenr += 1
                        self.players = 2
                if self.PL3.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 0:
                    if self.play_pagenr < self.help_pages:
                        self.play_pagenr += 1
                        self.players = 3
                if self.PL4.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 0:
                    if self.play_pagenr < self.help_pages:
                        self.play_pagenr += 1
                        self.players = 4
                if self.P1C.rect1.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P1C.cc > 0:
                        self.P1C.cc -= 1
                if self.P1C.rect2.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P1C.cc < 3:
                        self.P1C.cc += 1

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
