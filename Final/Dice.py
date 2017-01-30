import random

import pygame
from Image import *

class Dice:
    def __init__(self, x, y, sx, sy, I):
        self.x = x
        self.y = y
        self.click = False
        self.I = I
        self.I = pygame.transform.scale(self.I, (int(sx), int(sy)))
        self.rect = pygame.Rect((x, y), (sx, sy))
        self.rI = ["", ID1, ID2, ID3, ID4, ID5, ID6]
        self.rrI = [ID1, ID2, ID3, ID4, ID5, ID6]
        self.rcI = random.randint(1,6)
        self.cI = self.rI[self.rcI]
        self.DiceRolled = 0

        self.vxy = 0
        self.vx = 0
        self.vy = 0
        self.rvx = 0
        self.rvy = 0
        self.rc = 0
        self.rcc = 0
        self.vcc = 0
        self.vcc2 = 0

        self.rotate = self.rvx
        self.endrotate = random.randint(0, 360)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            pygame.mouse.get_rel()
            self.rc = 1

    def vel(self, width, height):
        self.vxy = pygame.mouse.get_rel()
        self.vx = self.vxy[0]
        self.vy = self.vxy[1]

        if self.rc == 4:
            self.rvx = random.randint(-80, -40)
            self.rvy = random.randint(40, 80)
            self.vcc = abs(self.rvx) + abs(self.rvy)
            self.rc = 3
        if self.rc == 2:
            self.rcc += 1
            if self.rcc == 3:
                self.rc = 3
                self.rcc = 0
        if self.rc == 2 and self.rcc == 2:
            self.rvx = self.vx
            self.rvy = self.vy
            self.vcc = abs(self.rvx) + abs(self.rvy)
        if self.rect.left == 0 or self.rect.right == width:
            self.rvx = -self.rvx
        if self.rect.top == 0 or self.rect.bottom == height:
            self.rvy = -self.rvy
        if self.rvx > 80:
            self.rvx = 80
        elif self.rvx < -80:
            self.rvx = -80
        if self.rvy > 80:
            self.rvy = 80
        elif self.rvy < -80:
            self.rvy = -80

    def update(self, screen_rect):
        self.vcc2 = abs(self.rvx) + abs(self.rvy)
        self.rotate = self.rvx
        if self.click:
            self.rect.move_ip(pygame.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
        if self.rc == 3:
            if self.rvx > 0:
                self.rvx -= 1
            elif self.rvx < 0:
                self.rvx += 1
            if self.rvy > 0:
                self.rvy -= 1
            elif self.rvy < 0:
                self.rvy += 1
        if self.vcc > 30:
            self.I = random.choice(self.rrI)
            self.I = pygame.transform.rotate(self.I, int(self.rotate))
            self.DiceRolled = 1
        if self.DiceRolled == 1 and self.vcc2 < 30:
            self.I = self.cI
            self.I = pygame.transform.rotate(self.I, int(self.endrotate))
        if self.rc == 3 and self.vcc < 30:
            self.vxy = 0
            self.vx = 0
            self.vy = 0
            self.rvx = 0
            self.rvy = 0
            self.rc = 0
            self.rcc = 0
            self.vcc = 0
            self.vcc2 = 0
        self.rect.move_ip(self.rvx, self.rvy)
        self.rect.clamp_ip(screen_rect)

    def draw(self, surface, sx, sy):
        self.I = pygame.transform.scale(self.I, (int(sx), int(sy)))
        self.rect = pygame.Rect((self.rect.left, self.rect.top), (sx, sy))
        surface.blit(self.I, (self.rect))