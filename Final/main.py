import random

import pygame
import MySQLdb
from pygame.locals import *

from Button import *
from Menu import *
from Player import *
from Tile import *
from Sounds import *
from Image import *
from Dice import *
from IText import *
from PColor import *
from PCat import *
from Settings import *
from Questions import *
from Checkplayers import *
from Addquestions import *
from Highscore import *

class Game:
    def __init__(self):
        self.res = [(800,600),(1280,720),(1366,768)]
        self.resc = 1
        self.size = self.res[self.resc]
        self.width = self.size[0]
        self.height = self.size[1]
        self.caption = "Dice'to'the'Top"
        self.S0 = [1, 0, 0, 0]
        self.help_pages = 2
        self.help_pagenr = 0
        self.play_pages = 4
        self.play_pagenr = 0
        self.settings_pages = 2
        self.settings_pagenr = 0
        self.players = 0
        self.turn = 0
        self.action = 0
        self.sound = pygame.mixer.Sound('Assets/click.wav')
        self.fs = 0

        self.steps = 0
        self.stepcount = 0
        self.stepdirection = None
        self.turn_end = False

        self.blink = False

        self.currentplayer = None

        self.sameposition = False
        self.downplayer = None
        self.stepcount_down = 0

        self.timer = 0

        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()

        self.entry_tile = build_matrix()

        self.tile_width = 0.028
        self.tile_height = 0.05
        self.grid_pos_x = 0.2197
        self.grid_pos_y = 0.9

        ### Playscreen
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
        self.Ques = None

        ### Settingscreen
        self.Addqc = PCat(self.width * 0.232, self.height * 0.318, self.width * 0.18, self.height * 0.044)
        self.TO1 = Toggle1(self.width * 0.572, self.height * 0.343, self.width * 0.068, self.height * 0.05)
        self.TO2 = Toggle1(self.width * 0.572, self.height * 0.403, self.width * 0.068, self.height * 0.05)
        self.TO3 = Toggle2(self.width * 0.572, self.height * 0.57, self.width * 0.068, self.height * 0.05)
        self.RES = Resolution(self.width * 0.54, self.height * 0.513, self.width * 0.1, self.height * 0.05)
        self.Add_Q = IText2(self.width * 0.232, self.height * 0.418, "", int(self.width * 0.022), self.width * 0.54, 1)
        self.Add_AG = IText3(self.width * 0.232, self.height * 0.512, "", int(self.width * 0.028), self.width * 0.35, 1)
        self.Add_AW1 = IText3(self.width * 0.232, self.height * 0.618, "", int(self.width * 0.028), self.width * 0.35, 1)
        self.Add_AW2 = IText3(self.width * 0.232, self.height * 0.721, "", int(self.width * 0.028), self.width * 0.35, 1)


    def draw(self):
        # Menu
        if self.S0[0] == 1:
            self.M1.draw(self.screen)
            self.Highscores.update()
            self.Highscores.draw(self.screen)
        # Play
        elif self.S0[1] == 1:
            # Choose Players
            if self.play_pagenr == 0:
                self.Pbg1.draw(self.screen)
                self.B1.draw(self.screen)
                self.PL2.draw(self.screen)
                self.PL3.draw(self.screen)
                self.PL4.draw(self.screen)
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
            elif self.play_pagenr >= 2:
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

                if self.players >= 2:
                    self.P1.Nametext = IText(self.width * 0.75, self.height * 0.20, "#1 " + self.P1.Name,
                                             int(self.width * 0.03), 0, 0, self.P1.Colour)
                    self.P2.Nametext = IText(self.width * 0.75, self.height * 0.255, "#2 " + self.P2.Name,
                                             int(self.width * 0.03), 0, 0, self.P2.Colour)
                    if self.players >= 3:
                        self.P3.Nametext = IText(self.width * 0.75, self.height * 0.310, "#3 " + self.P3.Name,
                                                 int(self.width * 0.03), 0, 0, self.P3.Colour)
                        if self.players == 4:
                            self.P4.Nametext = IText(self.width * 0.75, self.height * 0.365, "#4 " + self.P4.Name,
                                                     int(self.width * 0.03), 0, 0, self.P4.Colour)

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
                        for rangeright in range(to_right):
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
                elif self.turn >= 1:
                    players_array = [None, self.P1, self.P2, self.P3, self.P4]
                    self.currentplayer = players_array[self.turn]

                    if self.sameposition == False:
                        if self.currentplayer == self.P1:
                            self.P1.Nametext = IText(self.width * 0.75, self.height * 0.20, "#1 " + self.P1.Name,
                                                     int(self.width * 0.03), 0, 0, self.P1.Colour, True)
                        elif self.currentplayer == self.P2:
                            self.P2.Nametext = IText(self.width * 0.75, self.height * 0.255, "#2 " + self.P2.Name,
                                                     int(self.width * 0.03), 0, 0, self.P2.Colour, True)
                        elif self.currentplayer == self.P3:
                            self.P3.Nametext = IText(self.width * 0.75, self.height * 0.310, "#3 " + self.P3.Name,
                                                     int(self.width * 0.03), 0, 0, self.P3.Colour, True)
                        elif self.currentplayer == self.P4:
                            self.P4.Nametext = IText(self.width * 0.75, self.height * 0.365, "#4 " + self.P4.Name,
                                                     int(self.width * 0.03), 0, 0, self.P4.Colour, True)

                    if self.sameposition == True:
                        if self.downplayer == self.P1:
                            self.P1.Nametext = IText(self.width * 0.75, self.height * 0.20, "#1 " + self.P1.Name,
                                                     int(self.width * 0.03), 0, 0, self.P1.Colour, True)
                        elif self.downplayer == self.P2:
                            self.P2.Nametext = IText(self.width * 0.75, self.height * 0.255, "#2 " + self.P2.Name,
                                                     int(self.width * 0.03), 0, 0, self.P2.Colour, True)
                        elif self.downplayer == self.P3:
                            self.P3.Nametext = IText(self.width * 0.75, self.height * 0.310, "#3 " + self.P3.Name,
                                                     int(self.width * 0.03), 0, 0, self.P3.Colour, True)
                        elif self.downplayer == self.P4:
                            self.P4.Nametext = IText(self.width * 0.75, self.height * 0.365, "#4 " + self.P4.Name,
                                                     int(self.width * 0.03), 0, 0, self.P4.Colour, True)

                    # Player throws the dice
                    if self.action == 0:
                        if self.blink == True:
                            self.CD.draw(self.screen) #should be switched with TD...
                            self.blink = False
                        else:
                            self.blink = True

                        if self.D1.rcI > 0 and self.D1.DiceRolled == 1:
                            steps_array = [0, 1, 1, 2, 2, 3, 3]
                            self.steps = steps_array[self.D1.rcI]
                            # Same position player from last turn?, go down!
                            if self.sameposition == True:
                                if self.D1.vcc2 == 0:
                                    if (self.stepcount_down < self.D1.rcI) and (getattr(self.downplayer.Tile, "Down") != None):
                                        self.downplayer.Tile = getattr(self.downplayer.Tile, "Down")
                                        self.stepcount_down += 1
                                    else:
                                        self.sameposition = False
                                        self.downplayer = None
                                        self.turn_end = True
                            else:
                                self.action += 1

                    # Player gets question
                    elif self.action == 1 and self.D1.vcc2 == 0:
                        self.play_pagenr = 3

                    # Player chooses moving position
                    elif self.action == 2:
                        if self.blink == True:
                            self.TD.draw(self.screen) #Should be switched to CD...
                            self.blink = False
                        else:
                            self.blink = True

                        if (self.stepcount < self.steps) and (self.stepdirection != None) and self.D1.vcc2 == 0:
                            if self.currentplayer.Tile.Position.Y == 0 and (self.stepdirection != "Up"):
                                return
                            elif (getattr(self.currentplayer.Tile, self.stepdirection) != None):
                                self.currentplayer.Tile = getattr(self.currentplayer.Tile, self.stepdirection)
                                self.stepcount += 1
                            else:
                                self.turn_end = True

                        if self.stepcount == self.steps:
                            for i in range(1, self.players + 1):
                                if i != self.turn and players_array[i].Tile.Position == self.currentplayer.Tile.Position:
                                    self.sameposition = True
                                    self.downplayer = players_array[i]
                            self.turn_end = True

                # Update and draw Players
                self.P1.Draw(self.screen, self.width * self.tile_width, self.height * self.tile_height, self.width * self.grid_pos_x, self.height * self.grid_pos_y)
                self.P1.Nametext.draw(self.screen)
                self.P2.Draw(self.screen, self.width * self.tile_width, self.height * self.tile_height, self.width * self.grid_pos_x, self.height * self.grid_pos_y)
                self.P2.Nametext.draw(self.screen)
                if self.players >= 3:
                    self.P3.Draw(self.screen, self.width * self.tile_width, self.height * self.tile_height,
                                 self.width * self.grid_pos_x, self.height * self.grid_pos_y)
                    self.P3.Nametext.draw(self.screen)
                    if self.players == 4:
                        self.P4.Draw(self.screen, self.width * self.tile_width, self.height * self.tile_height,
                                     self.width * self.grid_pos_x, self.height * self.grid_pos_y)
                        self.P4.Nametext.draw(self.screen)

                # Update and draw Dice
                self.D1.update(self.screen_rect)  # Dice
                self.D1.draw(self.screen, self.width * 0.1, self.width * 0.1)
                self.D1.vel(self.width, self.height)

                # Questions
                if self.play_pagenr == 3:
                    if self.Ques == None:
                        pygame.time.wait(1500)
                        self.Ques = Questions(self.width * 0.307, self.height * 0.295, int(self.width * 0.023),
                                              self.currentplayer.Tile.Category)
                    self.Q.draw(self.screen)
                    self.Ques.update(self.width * 0.307, self.height * 0.295, int(self.width * 0.023))
                    self.Ques.draw(self.screen, self.width, self.height)

                    if self.Ques.answer_correct != None:
                        self.timer += 1
                        if self.timer == 20:
                            if self.Ques.answer_correct == True:
                                self.play_pagenr = 2
                                self.action += 1
                            if self.Ques.answer_correct == False:
                                self.play_pagenr = 2
                                self.turn_end = True
                            self.timer = 0

                # Win screen
                if self.play_pagenr == 4:
                    #print(self.currentplayer.Name, "won.")
                    self.Wonbg.draw(self.screen)
                    self.Cross3.draw(self.screen)
                    self.Wintext = IText(self.width * 0.33, self.height * 0.47, self.currentplayer.Name + " won!", int(self.width * 0.03), 0, 0)
                    self.Wintext.draw(self.screen)

                    # Prepare for next turn:
                    # First player turn.
                    if self.turn == 0:
                        self.turn = 1

                    # Next players turn
                    if self.turn_end == True:
                        if self.currentplayer.Tile.Category == "Finish":  # Check if player reached the end.
                            self.play_pagenr = 4
                        self.action = 0
                        self.steps = 0
                        self.stepcount = 0
                        self.stepdirection = None
                        self.Ques = None
                        self.turn_end = False

                        self.D1 = Dice(self.width * 0.81, self.height * 0.53, self.width * 0.1, self.width * 0.1, ID1)
                        if self.sameposition == False:
                            if self.turn == self.players:
                                self.turn = 1
                            else:
                                self.turn += 1

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
                self.TO1.update(self.width * 0.572, self.height * 0.343, self.width * 0.068, self.height * 0.05)
                self.TO1.draw(self.screen)
                self.TO2.update(self.width * 0.572, self.height * 0.403, self.width * 0.068, self.height * 0.05)
                self.TO2.draw(self.screen)
                self.TO3.update(self.width * 0.572, self.height * 0.57, self.width * 0.068, self.height * 0.05)
                self.TO3.draw(self.screen)
                self.RES.update(self.width * 0.54, self.height * 0.513, self.width * 0.1, self.height * 0.05)
                self.RES.draw(self.screen)
                self.Addq.draw(self.screen)
            elif self.settings_pagenr == 1:
                self.M1.draw(self.screen)
                self.Cbg.draw(self.screen)
                self.Cross2.draw(self.screen)
            elif self.settings_pagenr == 2:
                self.M1.draw(self.screen)
                self.Addq_bg.draw(self.screen)
                self.Cross4.draw(self.screen)
                self.Add.draw(self.screen)
                self.Addqc.update(self.width * 0.232, self.height * 0.318, self.width * 0.18, self.height * 0.044)
                self.Addqc.draw(self.screen)
                self.Add_Q.draw(self.screen)
                self.Add_AG.draw(self.screen)
                self.Add_AW1.draw(self.screen)
                self.Add_AW2.draw(self.screen)
        pygame.display.update()

    def process_events(self):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        ### Backgrounds
        self.M1 = Menu(self.width, self.height, BG0)
        self.Pbg1 = Backg(self.width, self.height, BG1)
        self.Pbg2 = Backg(self.width, self.height, BG2)
        self.Pbg3 = Backg(self.width, self.height, BG4)
        self.Helpbg = Backg(self.width, self.height, BG3)
        self.Q = Backg(self.width, self.height, I19)
        self.Sbg = Backg(self.width, self.height, BG5)
        self.Cbg = Backg(self.width, self.height, BG6)
        self.Wonbg = Backg(self.width, self.height, BG7)
        self.Addq_bg = Backg(self.width, self.height, BG8)

        ### Back/next/previous/cross buttons
        self.B1 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.B2 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.B3 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
        self.Next1 = Button(self.width * 0.88, self.height * 0.90, self.width * 0.1, self.height * 0.07, I6)
        self.Next2 = Button(self.width * 0.88, self.height * 0.90, self.width * 0.1, self.height * 0.07, I6)
        self.Prev1 = Button(self.width * 0.77, self.height * 0.90, self.width * 0.1, self.height * 0.07, I7)
        self.Prev2 = Button(self.width * 0.77, self.height * 0.90, self.width * 0.1, self.height * 0.07, I7)
        self.Cross1 = Button2(self.width * 0.63, self.height * 0.161, self.width * 0.044, self.height * 0.075, S1)
        self.Cross2 = Button2(self.width * 0.63, self.height * 0.0745, self.width * 0.044, self.height * 0.075, S1)
        self.Cross3 = Button2(self.width * 0.681, self.height * 0.396, self.width * 0.044, self.height * 0.075, S1)
        self.Cross4 = Button2(self.width * 0.763, self.height * 0.168, self.width * 0.044, self.height * 0.075, S1)
        self.Highscores = Highscore(self.width * 0.415, self.height * 0.42, int(self.width * 0.0235))

        ### Play screen
        self.PL2 = Button(self.width * 0.425, self.height * 0.22, self.width * 0.15, self.height * 0.15, I9)
        self.PL3 = Button(self.width * 0.425, self.height * 0.43, self.width * 0.15, self.height * 0.16, I10)
        self.PL4 = Button(self.width * 0.425, self.height * 0.64, self.width * 0.15, self.height * 0.17, I11)
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

        ### Help screen
        self.Credits = Button2(self.width * 0.36, self.height * 0.747, self.width * 0.13, self.height * 0.065, S2)
        self.Addq = Button2(self.width * 0.36, self.height * 0.679, self.width * 0.24, self.height * 0.065, S8)
        self.Add = Button2(self.width * 0.653, self.height * 0.726, self.width * 0.122, self.height * 0.071, S9)
        self.T1_1.update(events, self.width * 0.031, self.height * 0.145, int(self.width * 0.03), 0)
        self.T1_2.update(events, self.width * 0.095, self.height * 0.145, int(self.width * 0.03), self.width * 0.3)
        self.T2_1.update(events, self.width * 0.031, self.height * 0.245, int(self.width * 0.03), 0)
        self.T2_2.update(events, self.width * 0.095, self.height * 0.245, int(self.width * 0.03), self.width * 0.3)
        self.T3_1.update(events, self.width * 0.031, self.height * 0.345, int(self.width * 0.03), 0)
        self.T3_2.update(events, self.width * 0.095, self.height * 0.345, int(self.width * 0.03), self.width * 0.3)
        self.T4_1.update(events, self.width * 0.031, self.height * 0.445, int(self.width * 0.03), 0)
        self.T4_2.update(events, self.width * 0.095, self.height * 0.445, int(self.width * 0.03), self.width * 0.3)
        self.Add_Q.update(events, self.width * 0.232, self.height * 0.418, int(self.width * 0.022), self.width * 0.54)
        self.Add_AG.update(events, self.width * 0.232, self.height * 0.512, int(self.width * 0.028), self.width * 0.35)
        self.Add_AW1.update(events, self.width * 0.232, self.height * 0.618, int(self.width * 0.028), self.width * 0.35)
        self.Add_AW2.update(events, self.width * 0.232, self.height * 0.721, int(self.width * 0.028), self.width * 0.35)
        self.Text1 = Textbg(self.width * 0.02, self.height * 0.15, self.width * 0.95, self.height * 0.7, HELP1)
        self.Text2 = Textbg(self.width * 0.02, self.height * 0.15, self.width * 0.95, self.height * 0.7, HELP2)
        self.Text3 = Textbg(self.width * 0.02, self.height * 0.15, self.width * 0.95, self.height * 0.7, HELP3)

        self.screen_rect = self.screen.get_rect()

        for event in events:
            if event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                self.width = event.dict['size'][0]
                self.height = event.dict['size'][1]
                self.size = (self.width, self.height)
                if self.D1.rc == 0:
                    self.D1 = Dice(self.width * 0.81, self.height * 0.53, self.width * 0.1, self.width * 0.1, ID1)
            elif event.type == pygame.QUIT:
                return True
            elif keys[pygame.K_LCTRL] and keys[pygame.K_w]:
                return True
            elif keys[pygame.K_LALT] and keys[pygame.K_F4]:
                return True
            elif keys[pygame.K_F11]:
                if self.fs == 0:
                    self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | FULLSCREEN)
                    self.fs = 1
                    self.TO3.cc = 0
                elif self.fs ==  1:
                    self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
                    self.fs = 0
                    self.TO3.cc = 1
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
                if self.T1_2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    self.T1_1.focus = 1
                    self.T1_2.focus = 1
                elif not self.T1_2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    self.T1_1.focus = 0
                    self.T1_2.focus = 0
                if self.T2_2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    self.T2_1.focus = 1
                    self.T2_2.focus = 1
                elif not self.T2_2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    self.T2_1.focus = 0
                    self.T2_2.focus = 0
                if self.T3_2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    self.T3_1.focus = 1
                    self.T3_2.focus = 1
                elif not self.T3_2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    self.T3_1.focus = 0
                    self.T3_2.focus = 0
                if self.T4_2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    self.T4_1.focus = 1
                    self.T4_2.focus = 1
                elif not self.T4_2.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 1:
                    self.T4_1.focus = 0
                    self.T4_2.focus = 0
                if self.Add_Q.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    self.Add_Q.focus = 1
                elif not self.Add_Q.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    self.Add_Q.focus = 0
                if self.Add_AG.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    self.Add_AG.focus = 1
                elif not self.Add_AG.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    self.Add_AG.focus = 0
                if self.Add_AW1.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    self.Add_AW1.focus = 1
                elif not self.Add_AW1.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    self.Add_AW1.focus = 0
                if self.Add_AW2.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    self.Add_AW2.focus = 1
                elif not self.Add_AW2.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    self.Add_AW2.focus = 0
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.D1.click = False
                if self.D1.rc == 1:
                    self.D1.rc = 2
                if self.Next2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1 and self.play_pagenr == 1 and Checkplayers(self.T1_2, self.T2_2, self.T3_2, self.T4_2, self.P1C, self.P2C, self.P3C, self.P4C, self.P1CA, self.P2CA, self.P3CA, self.P4CA, self.players):
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
                elif self.Prev2.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[1] == 1 and self.play_pagenr == 1:
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
                if self.TO1.rect1.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1 and self.settings_pagenr == 0:
                    if self.TO1.cc > 0:
                        self.TO1.cc -= 1
                        Sound1.set_volume(1)
                elif self.TO1.rect2.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1 and self.settings_pagenr == 0:
                    if self.TO1.cc < 1:
                        self.TO1.cc += 1
                        Sound1.set_volume(0)
                if self.TO2.rect1.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1 and self.settings_pagenr == 0:
                    if self.TO2.cc > 0:
                        self.TO2.cc -= 1
                        pygame.mixer.music.unpause()
                elif self.TO2.rect2.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1 and self.settings_pagenr == 0:
                    if self.TO2.cc < 1:
                        self.TO2.cc += 1
                        pygame.mixer.music.pause()
                if self.TO3.rect1.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.TO3.cc > 0:
                        self.TO3.cc -= 1
                        self.fs = 1
                        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | FULLSCREEN)
                elif self.TO3.rect2.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1:
                    if self.TO3.cc < 1:
                        self.TO3.cc += 1
                        self.fs = 0
                        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
                if self.RES.rect1.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1 and self.settings_pagenr == 0:
                    if self.RES.cc > 0:
                        self.RES.cc -= 1
                        self.resc -= 1
                        self.size = self.res[self.resc]
                        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
                        self.TO3.cc = 1
                elif self.RES.rect2.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1 and self.settings_pagenr == 0:
                    if self.RES.cc < 2:
                        self.RES.cc += 1
                        self.resc += 1
                        self.size = self.res[self.resc]
                        self.screen = pygame.display.set_mode((self.size), HWSURFACE | DOUBLEBUF | RESIZABLE)
                        self.TO3.cc = 1
                if self.Credits.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1 and self.settings_pagenr == 0:
                    if self.settings_pagenr < self.settings_pages:
                        self.settings_pagenr = 1
                elif self.Addq.rect.collidepoint(pygame.mouse.get_pos()) and self.S0[3] == 1 and self.settings_pagenr == 0:
                    self.settings_pagenr = 2
                if self.Cross2.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 1:
                    self.settings_pagenr = 0
                elif self.Cross3.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 4:
                    self.S0 = [1, 0, 0, 0]
                    self.play_pagenr = int(0)
                elif self.Cross4.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    self.settings_pagenr = 0
                if self.Addqc.rect1.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    if self.Addqc.cc > 0:
                        self.Addqc.cc -= 1
                elif self.Addqc.rect2.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    if self.Addqc.cc < 3:
                        self.Addqc.cc += 1
                if self.Add.rect.collidepoint(pygame.mouse.get_pos()) and self.settings_pagenr == 2:
                    Add_question(None, self.Add_Q.atext, self.Addqc.category, self.Add_AG.atext, self.Add_AW1.atext, self.Add_AW2.atext)
                    self.Add_Q.atext = ""
                    self.Add_AG.atext = ""
                    self.Add_AW1.atext = ""
                    self.Add_AW2.atext = ""

                # Player move with direction pad
                elif self.AR_L.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 2 and self.action == 2:
                    #self.P1.Tile = self.P1.Tile.Left
                    self.stepdirection = "Left"
                elif self.AR_U.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 2 and self.action == 2:
                    if self.P1.Tile.Up != None:
                        #self.P1.Tile = self.P1.Tile.Up
                        self.stepdirection = "Up"
                elif self.AR_R.rect.collidepoint(pygame.mouse.get_pos()) and self.play_pagenr == 2 and self.action == 2:
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
