import pygame

class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)
        self.caption = "Button Test"
        self.color = pygame.Color("Grey")

        self.M0 = 1
        self.M1 = 0

        pygame.init()

        self.b1 = Button(self.width * 0.85, self.height * 0.05, self.width * 0.1, self.height * 0.05, "Menu")
        self.Menu1 = MainMenu(self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

    def draw(self):
        self.screen.fill(self.color)
        
        if self.M0 == 1:
            self.Menu1.draw(self.screen)
        if self.M1 == 1:
            self.b1.draw(self.screen)

        pygame.display.update()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONUP:
                if self.b1.rect.collidepoint(pygame.mouse.get_pos()):
                    self.M0 = 1
                    self.M1 = 0 
                if self.Menu1.b1.rect.collidepoint(pygame.mouse.get_pos()):
                    self.M0 = 0
                    self.M1 = 1
                if self.Menu1.b4.rect.collidepoint(pygame.mouse.get_pos()):
                    return True

        return False

    def game_loop(self):
        while not self.process_events():
            self.draw()

class MainMenu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (x, y)
        self.color = pygame.Color("Light Blue")
        self.textcolor = pygame.Color("Black")
        self.rect = pygame.Rect((0,0), self.size)
        self.font = pygame.font.Font(None, int(self.x * 0.15))
        self.text = self.font.render("Main Menu", 1, self.textcolor)

        self.b1 = Button(self.x * 0.3, self.y * 0.3, self.x * 0.4, self.y * 0.1, "Play")
        self.b2 = Button(self.x * 0.3, self.y * 0.41, self.x * 0.4, self.y * 0.1, "Instruction")
        self.b3 = Button(self.x * 0.3, self.y * 0.52, self.x * 0.4, self.y * 0.1, "Options")
        self.b4 = Button(self.x * 0.3, self.y * 0.63, self.x * 0.4, self.y * 0.1, "Exit")

    def draw(self, surface):
        surface.fill(self.color, self.rect)
        surface.blit(self.text, (int(self.x * 0.22), int(self.y * 0.1)))
        self.b1.draw(surface)
        self.b2.draw(surface)
        self.b3.draw(surface)
        self.b4.draw(surface)

class Button:
    def __init__(self, x, y, sx, sy, text):
        self.x = x
        self.y = y
        self.size = (sx, sy)
        self.color = pygame.Color("Red")
        self.textcolor = pygame.Color("Black")
        self.rect = pygame.Rect((x,y), self.size)
        self.font = pygame.font.Font(None, int(sy * 0.8))
        self.text = self.font.render(text, 1, self.textcolor)

    def draw(self, surface):
        surface.fill(self.color, self.rect)
        surface.blit(self.text, (self.x, self.y))

def program():
    game = Game()
    game.game_loop()

program()

pygame.quit()
