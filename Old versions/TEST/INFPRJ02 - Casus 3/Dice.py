import pygame
import random

class Dice:
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x, y), (sx, sy))
        self.click = False
        self.rcolor = ["Red", "Green", "Blue", "White", "Yellow", "Black"]
        self.color = pygame.Color("White")
        self.ccolor = random.choice(self.rcolor)

        self.vxy = 0
        self.vx = 0
        self.vy = 0
        self.rvx = 0
        self.rvy = 0
        self.vc = 0
        self.rc = 0
        self.rcc = 0
        self.vcc = 0
        self.vcc2 = 0

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            pygame.mouse.get_rel()
            self.rc = 1

    def vel(self, width, height):
        self.vxy = pygame.mouse.get_rel()
        self.vx = self.vxy[0]
        self.vy = self.vxy[1]

        self.vc += 1
        if self.vxy == (0,0):
            self.vc = 0
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

    def update(self, screen_rect):
        self.vcc2 = abs(self.rvx) + abs(self.rvy)
        if self.click:
            self.rect.move_ip(pygame.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
        if self.rc == 3:
            if self.rvx > 0:
                self.rvx -= 1
            if self.rvx < 0:
                self.rvx += 1
            if self.rvy > 0:
                self.rvy -= 1
            if self.rvy < 0:
                self.rvy += 1
        if self.vcc >= 30:
            self.color = pygame.Color(random.choice(self.rcolor))
        if self.rc == 3 and self.vcc2 < 30:
            self.color = pygame.Color(self.ccolor)
        self.rect.move_ip(self.rvx, self.rvy)
        self.rect.clamp_ip(screen_rect)
        print(self.rc, self.vcc)

    def draw(self, surface):
        surface.fill(self.color, self.rect)
            