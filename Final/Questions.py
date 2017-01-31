import MySQLdb
import pygame

import random

def question(category):
    query = """select * from Vragen WHERE Category = '%s'  ORDER BY RAND() LIMIT 1  """ % (category)

    # Open database connection
    db = MySQLdb.connect("5.79.70.63", "Boardgame", "groep12017", "Boardgame")

    cursor = db.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    result = data

    # disconnect from server
    db.close()

    return result


res = question("Sport")
questions = res[0][1]
answer = res[0][3]
wrongans = res[0][4]
wrongans2 = res[0][5]

class Questions:
    def __init__(self, x, y, size):
        self.category = "Sport"
        self.res = question(self.category)
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", size)
        self.Questions = self.font.render(self.res[0][1], 1, (0,0,0))
        self.categ = self.font.render(self.res[0][2], 1, (0,0,0))
        self.ranswer = self.font.render(self.res[0][3], 1, (0,0,0))
        self.wanswer1 = self.font.render(self.res[0][4], 1, (0,0,0))
        self.wanswer2 = self.font.render(self.res[0][5], 1, (0,0,0))
        self.maxsize = 39
        self.answers = [self.ranswer, self.wanswer1, self.wanswer2]
        self.a1 = random.choice(self.answers)
        self.answers.remove(self.a1)
        self.a2 = random.choice(self.answers)
        self.answers.remove(self.a2)
        self.a3 = self.answers[0]

    def update(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", size)
        self.Questions = self.font.render(self.res[0][1], 1, (0,0,0))
        self.categ = self.font.render(self.res[0][2], 1, (0,0,0))
        self.ranswer = self.font.render(self.res[0][3], 1, (0,0,0))
        self.wanswer1 = self.font.render(self.res[0][4], 1, (0,0,0))
        self.wanswer2 = self.font.render(self.res[0][5], 1, (0,0,0))
        self.rect1 = pygame.Rect(self.x * 1.2, self.y * 1.305 + self.y * 0.3, int(self.size * 14), int(self.size * 1.5))
        self.rect2 = pygame.Rect(self.x * 1.2, self.y * 1.450 + self.y * 0.3 + self.size, int(self.size * 14), int(self.size * 1.5))
        self.rect3 = pygame.Rect(self.x * 1.2, self.y * 1.595 + self.y * 0.3 + self.size * 2, int(self.size * 14), int(self.size * 1.5))
        self.srect1 = pygame.Surface((int(self.size * 14), int(self.size * 1.5)))
        self.srect2 = pygame.Surface((int(self.size * 14), int(self.size * 1.5)))
        self.srect3 = pygame.Surface((int(self.size * 14), int(self.size * 1.5)))

    def draw(self, surface):
        if len(self.res[0][1]) > self.maxsize:
            self.Questions1 = self.font.render(self.res[0][1][:self.maxsize], 1, (0,0,0))
            self.Questions2 = self.font.render(self.res[0][1][self.maxsize:], 1, (0,0,0))
            surface.blit(self.Questions1, (self.x, self.y))
            surface.blit(self.Questions2, (self.x, self.y + self.size))
        else:
            surface.blit(self.Questions, (self.x, self.y))
        surface.blit(self.a1, (self.x * 1.25, self.y * 1.315 + self.y * 0.3))
        surface.blit(self.a2, (self.x * 1.25, self.y * 1.470 + self.y * 0.3 + self.size))
        surface.blit(self.a3, (self.x * 1.25, self.y * 1.630 + self.y * 0.3 + self.size * 2))
        if self.rect1.collidepoint(pygame.mouse.get_pos()):
            self.srect1.fill(pygame.Color("Light Green"))
            self.srect1.set_alpha(68)
            surface.blit(self.srect1, (self.x * 1.2, self.y * 1.305 + self.y * 0.3))
        if self.rect2.collidepoint(pygame.mouse.get_pos()):
            self.srect2.fill(pygame.Color("Light Green"))
            self.srect2.set_alpha(68)
            surface.blit(self.srect2, (self.x * 1.2, self.y * 1.450 + self.y * 0.3 + self.size))
        if self.rect3.collidepoint(pygame.mouse.get_pos()):
            self.srect3.fill(pygame.Color("Light Green"))
            self.srect3.set_alpha(68)
            surface.blit(self.srect3, (self.x * 1.2, self.y * 1.595 + self.y * 0.3 + self.size * 2))
