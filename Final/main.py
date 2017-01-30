import random

import pygame
from pygame.locals import *

from Button import *
from Menu import *
from Player import *
from Tile import *
from Image import *
from Dice import *
from IText import *
from PColor import *
from PCat import *
from Settings import *

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
        self.settings_pages = 1
        self.settings_pagenr = 0
        self.players = 0
        self.turn = 0
        self.action = 0

        self.steps = 0
        self.stepcount = 0
        self.stepdirection = None
        self.turn_end = False

        pygame.init()

        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()

        self.entry_tile = build_matrix()

        self.tile_width = 0.028
        self.tile_height = 0.05
        self.grid_pos_x = 0.2197
        self.grid_pos_y = 0.9

        self.P1 = Player("", self.entry_tile)
        self.P2 = Player("", self.entry_tile.Right.Right)
        self.P3 = Player("", self.entry_tile.Right.Right.Right.Right)
        self.P4 = Player("", self.entry_tile.Right.Right.Right.Right.Right.Right)

        self.D1 = Dice(self.width * 0.81, self.height * 0.53, self.width * 0.1, self.width * 0.1, ID1)
        self.T1_1 = IText(self.width * 0.031, self.height * 0.145, "#1", int(self.width * 0.03), 0, 0)
        self.T1_2 = IText(self.width * 0.095, self.height * 0.145, "", int(self.width * 0.03), self.width * 0.3, 1)
        self.T2_1 = IText(self.width * 0.031, self.height * 0.245, "#2", int(self.width * 0.03), 0, 0)
        self.T2_2 = IText(self.width * 0.095, self.height * 0.245, "", int(self.width * 0.03), self.width * 0.3, 1)
        self.T3_1 = IText(self.width * 0.031, self.height * 0.345, "#3", int(self.width * 0.03), 0, 0)
        self.T3_2 = IText(self.width * 0.095, self.height * 0.345, "", int(self.width * 0.03), self.width * 0.3, 1)
        self.T4_1 = IText(self.width * 0.031, self.height * 0.445, "#4", int(self.width * 0.03), 0, 0)
        self.T4_2 = IText(self.width * 0.095, self.height * 0.445, "", int(self.width * 0.03), self.width * 0.3, 1)
        self.P1C = PColor(self.width * 0.55, self.height * 0.2)
        self.P2C = PColor(self.width * 0.55, self.height * 0.2)
        self.P3C = PColor(self.width * 0.55, self.height * 0.2)
        self.P4C = PColor(self.width * 0.55, self.height * 0.2)
        self.P1CA = PCat(self.width * 0.67, self.height * 0.145, self.width * 0.18, self.height * 0.05)
        self.P2CA = PCat(self.width * 0.67, self.height * 0.245, self.width * 0.18, self.height * 0.05)
        self.P3CA = PCat(self.width * 0.67, self.height * 0.345, self.width * 0.18, self.height * 0.05)
        self.P4CA = PCat(self.width * 0.67, self.height * 0.445, self.width * 0.18, self.height * 0.05)
        self.TO1 = Toggle1(self.width * 0.572, self.height * 0.381, self.width * 0.068, self.height * 0.05)
        self.TO2 = Toggle1(self.width * 0.572, self.height * 0.442, self.width * 0.068, self.height * 0.05)
        self.TO3 = Toggle2(self.width * 0.572, self.height * 0.61, self.width * 0.068, self.height * 0.05)
        self.RES = Resolution(self.width * 0.54, self.height * 0.553, self.width * 0.1, self.height * 0.05)

    def draw(self):
        # Menu
        if self.S0[0] == 1:
            self.M1.draw(self.screen)
        # Play
        elif self.S0[1] == 1:
            # Choose Players
            if self.play_pagenr == 0:
                self.Pbg1.draw(self.screen)
                self.B1.draw(self.screen)
                self.PL2.draw(self.screen)
                self.PL3.draw(self.screen)
                self.PL4.draw(self.screen)
                self.Next2.draw(self.screen)
            # Pick player settings
            elif self.play_pagenr == 1:
                self.Pbg2.draw(self.screen)
                if self.players >= 2:
                    self.T1_1.draw(self.screen)
                    self.T1_2.draw(self.screen)
                    self.T2_1.draw(self.screen)
                    self.T2_2.draw(self.screen)
                    self.P1C.update(self.width * 0.43, self.height * 0.145)
                    self.P1C.draw(self.screen)
                    self.P2C.update(self.width * 0.43, self.height * 0.245)
                    self.P2C.draw(self.screen)
                    self.CA1_L.draw(self.screen)
                    self.CA1_R.draw(self.screen)
                    self.CA2_L.draw(self.screen)
                    self.CA2_R.draw(self.screen)
                    self.P1CA.update(self.width * 0.67, self.height * 0.145, self.width * 0.18, self.height * 0.05)
                    self.P1CA.draw(self.screen)
                    self.P2CA.update(self.width * 0.67, self.height * 0.245, self.width * 0.18, self.height * 0.05)
                    self.P2CA.draw(self.screen)
                    if self.players >= 3:
                        self.T3_1.draw(self.screen)
                        self.T3_2.draw(self.screen)
                        self.P3C.update(self.width * 0.43, self.height * 0.345)
                        self.P3C.draw(self.screen)
                        self.CA3_L.draw(self.screen)
                        self.CA3_R.draw(self.screen)
                        self.P3CA.update(self.width * 0.67, self.height * 0.345, self.width * 0.18, self.height * 0.05)
                        self.P3CA.draw(self.screen)
                        if self.players == 4:
                            self.T4_1.draw(self.screen)
                            self.T4_2.draw(self.screen)
                            self.P4C.update(self.width * 0.43, self.height * 0.445)
                            self.P4C.draw(self.screen)
                            self.CA4_L.draw(self.screen)
                            self.CA4_R.draw(self.screen)
                            self.P4CA.update(self.width * 0.67, self.height * 0.445, self.width * 0.18, self.height * 0.05)
                            self.P4CA.draw(self.screen)
                self.B1.draw(self.screen)
                self.Next2.draw(self.screen)
                self.Prev2.draw(self.screen)
            # Boardgame
            elif self.play_pagenr == 2 or self.play_pagenr == 3:
                # Draw everything on the board
                self.Pbg3.draw(self.screen)
                self.B1.draw(self.screen)
                self.entry_tile.Draw(self.screen, self.width * self.tile_width, self.height * self.tile_height,
                                     self.width * self.grid_pos_x, self.height * self.grid_pos_y)
                self.TD_L.draw(self.screen)             # throw dice text
                self.CD_L.draw(self.screen)             # choose direction text
                self.AR_L.draw(self.screen)             # direction buttons
                self.AR_R.draw(self.screen)
                self.AR_U.draw(self.screen)
                self.D1.update(self.screen_rect)        # Dice
                self.D1.draw(self.screen, self.width * 0.1, self.width * 0.1)
                self.D1.vel(self.width, self.height)
                self.Next2.draw(self.screen)            # Next and previous button
                self.Prev2.draw(self.screen)

                # At turn 0, place players
                if self.turn == 0:
                    def getstart(category):
                        to_right = 0
                        if category == "Entertainment":
                            to_right = 0
                        elif category == "Geography":
                            to_right = 1
                        elif category == "History":
                            to_right = 2
                        elif category == "Sport":
                            to_right = 3
                        start = self.entry_tile
                        for i in range(to_right):
                            start = start.Right
                        return start

                    if self.players >= 2:
                        self.P1.Tile = getstart(self.P1.StartCat)
                        self.P2.Tile = getstart(self.P2.StartCat)
                        if self.players >= 3:
                            self.P3.Tile = getstart(self.P3.StartCat)
                            if self.players == 4:
                                self.P4.Tile = getstart(self.P4.StartCat)

                # Turns
                elif 1 >= self.turn:
                    players_array = [None, self.P1, self.P2, self.P3, self.P4]
                    currentplayer = players_array[self.turn]

                    # Player throws the dice
                    if self.action == 0:
                        if self.D1.rcI > 0 and self.D1.DiceRolled == 1:
                            steps_array = [1, 1, 2, 2, 3, 3]
                            self.steps = steps_array[self.D1.rcI]
                            self.action += 2

                    # Player gets question
                    #elif self.action == 1:
                        #if answer_right == True:
                        #    self.action += 1
                        #elif answer_right == False:
                        #    self.action += 2

                    # Player chooses moving position
                    elif self.action == 2:
                        if self.stepcount <= self.steps and self.stepdirection != None:
                            #print(self.stepdirection)
                            currentplayer.Tile = getattr(currentplayer.Tile, self.stepdirection)
                            self.stepcount += 1
                        if self.stepcount == self.steps:
                            self.action += 1

                    elif self.action == 3:
                        self.turn_end = True

                # Prepare for next turn:
                # First players turn.
                if self.turn == 0:
                    self.turn = 1

                # Next players turn
                if self.turn_end == True:
                    self.action = 0
                    self.steps = 0
                    self.stepcount = 0
                    self.stepdirection = None
                    self.turn_end = False
                    if self.turn == self.players:
                        self.turn = 1
                    else:
                        self.turn += 1


                # Update and draw Players
                self.P1.Update()
                self.P1.Draw(self.screen, self.width * self.tile_width, self.height * self.tile_height,
                             self.width * self.grid_pos_x, self.height * self.grid_pos_y)
                p1name = IText(self.width * 0.75, self.height * 0.20, "#1 " + self.P1.Name, int(self.width * 0.03), 0, 0, self.P1.Colour)
                p1name.draw(self.screen)
                self.P2.Update()
                self.P2.Draw(self.screen, self.width * self.tile_width, self.height * self.tile_height,
                             self.width * self.grid_pos_x, self.height * self.grid_pos_y)
                p2name = IText(self.width * 0.75, self.height * 0.255, "#2 " + self.P2.Name, int(self.width * 0.03), 0, 0,
                               self.P2.Colour)
                p2name.draw(self.screen)
                if self.players >= 3:
                    self.P3.Update()
                    self.P3.Draw(self.screen, self.width * self.tile_width, self.height * self.tile_height,
                                 self.width * self.grid_pos_x, self.height * self.grid_pos_y)
                    p3name = IText(self.width * 0.75, self.height * 0.310, "#3 " + self.P3.Name, int(self.width * 0.03),
                                   0, 0, self.P3.Colour)
                    p3name.draw(self.screen)
                    if self.players == 4:
                        self.P4.Update()
                        self.P4.Draw(self.screen, self.width * self.tile_width, self.height * self.tile_height,
                                     self.width * self.grid_pos_x, self.height * self.grid_pos_y)
                        p4name = IText(self.width * 0.75, self.height * 0.365, "#4 " + self.P4.Name, int(self.width * 0.03),
                                   0, 0, self.P4.Colour)
                        p4name.draw(self.screen)

                # Questions screen
                if self.play_pagenr == 3:
                    self.Q.draw(self.screen)
        # Help
        elif self.S0[2] == 1:
            self.Helpbg.draw(self.screen)
            if self.help_pagenr == 0:
                self.Text1.draw(self.screen)
                self.Next1.draw(self.screen)
            elif self.help_pagenr == 1:
                self.Text2.draw(self.screen)
                self.Next1.draw(self.screen)
                self.Prev1.draw(self.screen)
            elif self.help_pagenr == 2:
                self.Text3.draw(self.screen)
                self.Prev1.draw(self.screen)
            self.B2.draw(self.screen)
        # Settings
        elif self.S0[3] == 1:
            if self.settings_pagenr == 0:
                self.M1.draw(self.screen)
                self.Sbg.draw(self.screen)
                self.Cross1.draw(self.screen)
                self.Credits.draw(self.screen)
                self.TO1.update(self.width * 0.572, self.height * 0.381, self.width * 0.068, self.height * 0.05)
                self.TO1.draw(self.screen)
                self.TO2.update(self.width * 0.572, self.height * 0.442, self.width * 0.068, self.height * 0.05)
                self.TO2.draw(self.screen)
                self.TO3.update(self.width * 0.572, self.height * 0.61, self.width * 0.068, self.height * 0.05)
                self.TO3.draw(self.screen)
                self.RES.update(self.width * 0.54, self.height * 0.553, self.width * 0.1, self.height * 0.05)
                self.RES.draw(self.screen)
            elif self.settings_pagenr == 1:
                self.M1.draw(self.screen)
                self.Cbg.draw(self.screen)
                self.Cross2.draw(self.screen)


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
        self.Sbg = Backg(self.width, self.height, BG5)
        self.Cbg = Backg(self.width, self.height, BG6)
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
        self.AR_U = Button(self.width * 0.83, self.height * 0.83, self.width * 0.065, self.height * 0.085, I18)
        self.CA1_L = Textbg(self.width * 0.46, self.height * 0.147, self.width * 0.028, self.height * 0.051, I20)
        self.CA1_R = Textbg(self.width * 0.58, self.height * 0.147, self.width * 0.028, self.height * 0.051, I21)
        self.CA2_L = Textbg(self.width * 0.46, self.height * 0.247, self.width * 0.028, self.height * 0.051, I20)
        self.CA2_R = Textbg(self.width * 0.58, self.height * 0.247, self.width * 0.028, self.height * 0.051, I21)
        self.CA3_L = Textbg(self.width * 0.46, self.height * 0.347, self.width * 0.028, self.height * 0.051, I20)
        self.CA3_R = Textbg(self.width * 0.58, self.height * 0.347, self.width * 0.028, self.height * 0.051, I21)
        self.CA4_L = Textbg(self.width * 0.46, self.height * 0.447, self.width * 0.028, self.height * 0.051, I20)
        self.CA4_R = Textbg(self.width * 0.58, self.height * 0.447, self.width * 0.028, self.height * 0.051, I21)
        self.Cross1 = Button2(self.width * 0.63, self.height * 0.185, self.width * 0.044, self.height * 0.075, S1)
        self.Cross2 = Button2(self.width * 0.63, self.height * 0.0745, self.width * 0.044, self.height * 0.075, S1)
        self.Credits = Button2(self.width * 0.36, self.height * 0.7, self.width * 0.13, self.height * 0.07, S2)


        self.screen_rect = self.screen.get_rect()
        self.T1_1.update(events, self.width * 0.031, self.height * 0.145, int(self.width * 0.03), 0)
        self.T1_2.update(events, self.width * 0.095, self.height * 0.145, int(self.width * 0.03), self.width * 0.3)
        self.T2_1.update(events, self.width * 0.031, self.height * 0.245, int(self.width * 0.03), 0)
        self.T2_2.update(events, self.width * 0.095, self.height * 0.245, int(self.width * 0.03), self.width * 0.3)
        self.T3_1.update(events, self.width * 0.031, self.height * 0.345, int(self.width * 0.03), 0)
        self.T3_2.update(events, self.width * 0.095, self.height * 0.345, int(self.width * 0.03), self.width * 0.3)
        self.T4_1.update(events, self.width * 0.031, self.height * 0.445, int(self.width * 0.03), 0)
        self.T4_2.update(events, self.width * 0.095, self.height * 0.445, int(self.width * 0.03), self.width * 0.3)

        for event in events:
            if event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                self.width = event.dict['size'][0]
                self.height = event.dict['size'][1]
                if self.D1.rc == 0:
                    self.D1 = Dice(self.width * 0.81, self.height * 0.53, self.width * 0.1, self.width * 0.1, ID1)
            elif event.type == pygame.QUIT:
                return True
            elif keys[pygame.K_LCTRL] and keys[pygame.K_w]:
                return True
            elif keys[pygame.K_LALT] and keys[pygame.K_F4]:
                return True
            elif keys[pygame.K_ESCAPE]:
                if self.S0[1] == 1 or self.S0[2] == 1 or self.S0[3] == 1:
                    self.S0 = [1, 0, 0, 0]
                    self.play_pagenr = int(0)
                    self.help_pagenr = int(0)
            elif keys[pygame.K_r]:
                self.D1 = Dice(self.width * 0.81, self.height * 0.53, self.width * 0.1, self.width * 0.1, ID1)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.D1.rc == 0:
                    self.D1.check_click(event.pos)
                if self.T1_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T1_1.focus = 1
                    self.T1_2.focus = 1
                elif not self.T1_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T1_1.focus = 0
                    self.T1_2.focus = 0
                if self.T2_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T2_1.focus = 1
                    self.T2_2.focus = 1
                elif not self.T2_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T2_1.focus = 0
                    self.T2_2.focus = 0
                if self.T3_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T3_1.focus = 1
                    self.T3_2.focus = 1
                elif not self.T3_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T3_1.focus = 0
                    self.T3_2.focus = 0
                if self.T4_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T4_1.focus = 1
                    self.T4_2.focus = 1
                elif not self.T4_2.rect.collidepoint(pygame.mouse.get_pos()):
                    self.T4_1.focus = 0
                    self.T4_2.focus = 0
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.D1.click = False
                if self.D1.rc == 1:
                    self.D1.rc = 2
                if self.Next2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1:  #and self.play_pagenr != 3
                    if self.play_pagenr < self.play_pages:
                        if self.players >= 2 and self.play_pagenr == 1:
                            self.P1.Name = self.T1_2.atext
                            self.P1.Colour = self.P1C.color
                            self.P1.StartCat = self.P1CA.category
                            self.P2.Name = self.T2_2.atext
                            self.P2.Colour = self.P2C.color
                            self.P2.StartCat = self.P2CA.category
                            if self.players >= 3:
                                self.P3.Name = self.T3_2.atext
                                self.P3.Colour = self.P3C.color
                                self.P3.StartCat = self.P3CA.category
                                if self.players == 4:
                                    self.P4.Name = self.T4_2.atext
                                    self.P4.Colour = self.P4C.color
                                    self.P4.StartCat = self.P4CA.category
                        self.play_pagenr += 1
                elif self.Prev2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1: #and self.play_pagenr != 3
                    if self.play_pagenr > 0:
                        self.play_pagenr -= 1
                elif self.Next1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[2] == 1:
                    if self.help_pagenr < self.help_pages:
                        self.help_pagenr += 1
                elif self.Prev1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[2] == 1:
                    if self.help_pagenr > 0:
                        self.help_pagenr -= 1
                elif self.B1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1:
                    self.S0 = [1, 0, 0, 0]
                    self.play_pagenr = int(0)
                elif self.B2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[2] == 1:
                    self.S0 = [1, 0, 0, 0]
                    self.help_pagenr = int(0)
                elif self.Cross1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1 and self.settings_pagenr != 1:
                    self.S0 = [1, 0, 0, 0]
                elif self.M1.B1.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    self.S0 = [0, 1, 0, 0]
                elif self.M1.B2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    self.S0 = [0, 0, 1, 0]
                elif self.M1.B3.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    self.S0 = [0, 0, 0, 1]
                elif self.M1.B4.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[0] == 1:
                    return True
                elif self.PL2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 0:
                    if self.play_pagenr < self.help_pages:
                        self.play_pagenr += 1
                        self.players = 2
                elif self.PL3.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 0:
                    if self.play_pagenr < self.help_pages:
                        self.play_pagenr += 1
                        self.players = 3
                elif self.PL4.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 0:
                    if self.play_pagenr < self.help_pages:
                        self.play_pagenr += 1
                        self.players = 4
                if self.P1C.rect1.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P1C.cc > 0:
                        self.P1C.cc -= 1
                elif self.P1C.rect2.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P1C.cc < 3:
                        self.P1C.cc += 1
                if self.P2C.rect1.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P2C.cc > 0:
                        self.P2C.cc -= 1
                elif self.P2C.rect2.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P2C.cc < 3:
                        self.P2C.cc += 1
                if self.P3C.rect1.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P3C.cc > 0:
                        self.P3C.cc -= 1
                elif self.P3C.rect2.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P3C.cc < 3:
                        self.P3C.cc += 1
                if self.P4C.rect1.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P4C.cc > 0:
                        self.P4C.cc -= 1
                elif self.P4C.rect2.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P4C.cc < 3:
                        self.P4C.cc += 1
                if self.P1CA.rect1.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P1CA.cc > 0:
                        self.P1CA.cc -= 1
                elif self.P1CA.rect2.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P1CA.cc < 3:
                        self.P1CA.cc += 1
                if self.P2CA.rect1.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P2CA.cc > 0:
                        self.P2CA.cc -= 1
                elif self.P2CA.rect2.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P2CA.cc < 3:
                        self.P2CA.cc += 1
                if self.P3CA.rect1.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P3CA.cc > 0:
                        self.P3CA.cc -= 1
                elif self.P3CA.rect2.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P3CA.cc < 3:
                        self.P3CA.cc += 1
                if self.P4CA.rect1.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P4CA.cc > 0:
                        self.P4CA.cc -= 1
                elif self.P4CA.rect2.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    if self.P4CA.cc < 3:
                        self.P4CA.cc += 1

                # SETTINGS toggles for setting options
                if self.TO1.rect1.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.TO1.cc > 0:
                        self.TO1.cc -= 1
                elif self.TO1.rect2.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.TO1.cc < 1:
                        self.TO1.cc += 1
                if self.TO2.rect1.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.TO2.cc > 0:
                        self.TO2.cc -= 1
                elif self.TO2.rect2.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.TO2.cc < 1:
                        self.TO2.cc += 1
                if self.TO3.rect1.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.TO3.cc > 0:
                        self.TO3.cc -= 1
                elif self.TO3.rect2.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.TO3.cc < 1:
                        self.TO3.cc += 1
                if self.RES.rect1.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.RES.cc > 0:
                        self.RES.cc -= 1
                elif self.RES.rect2.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.RES.cc < 2:
                        self.RES.cc += 1
                if self.Credits.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.settings_pagenr < self.settings_pages:
                        self.settings_pagenr += 1
                elif self.Cross2.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 1:
                    self.settings_pagenr = 0

                # Player move with direction pad demo
                elif self.AR_L.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1 and self.play_pagenr == 2:
                    #self.P1.Tile = self.P1.Tile.Left
                    self.stepdirection = "Left"
                elif self.AR_U.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1 and self.play_pagenr == 2:
                    if self.P1.Tile.Up != None:
                        #self.P1.Tile = self.P1.Tile.Up
                        self.stepdirection = "Up"
                elif self.AR_R.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1 and self.play_pagenr == 2:
                    #self.P1.Tile = self.P1.Tile.Right
                    self.stepdirection = "Right"
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3 and self.D1.rect.collidepoint(pygame.mouse.get_pos()) and self.D1.rc == 0:
                self.D1.rc = 4
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
