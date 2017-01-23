import pygame
from pygame.locals import *

#LOAD IMAGES
I0 = pygame.image.load("Assets/Background_S0.jpg")
I1 = pygame.image.load("Assets/Play_Button.jpg")
I2 = pygame.image.load("Assets/Help_Button.jpg")
I3 = pygame.image.load("Assets/Settings_Button.jpg")
I4 = pygame.image.load("Assets/Quit_Button.jpg")
I5 = pygame.image.load("Assets/Back_Button.jpg")

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

    def draw(self):
        if self.S0[0] == 1:
            self.M1.draw(self.screen)
        if self.S0[1] == 1:
            self.screen.fill((pygame.Color("Light Blue")))
            self.B1.draw(self.screen)

        pygame.display.update()

    def process_events(self):
        keys = pygame.key.get_pressed()

        self.B1 = Button(self.width * 0.88, self.height * 0.04, self.width * 0.1, self.height * 0.07, I5)
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

class Menu:
    def __init__(self, x, y, I):
        self.x = x
        self.y = y
        self.I = I
        self.I = pygame.transform.scale(self.I, (int(x), int(y)))
        self.rect = pygame.Rect((0,0), (x, y))

        self.B1 = Button(self.x * 0.12, self.y * 0.29, self.x * 0.2, self.y * 0.14, I1)
        self.B2 = Button(self.x * 0.12, self.y * 0.44, self.x * 0.2, self.y * 0.14, I2)
        self.B3 = Button(self.x * 0.12, self.y * 0.59, self.x * 0.2, self.y * 0.14, I3)
        self.B4 = Button(self.x * 0.12, self.y * 0.74, self.x * 0.2, self.y * 0.14, I4)

    def draw(self, surface):
        surface.blit(self.I, (self.rect))
        self.B1.draw(surface)
        self.B2.draw(surface)
        self.B3.draw(surface)
        self.B4.draw(surface)

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

def run():
    game = Game()
    game.game_loop()

run()

pygame.quit()
