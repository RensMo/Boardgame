import MySQLdb
import pygame

import random
from Image import *

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
    def __init__(self, x, y, size, category):
        self.x = x
        self.y = y
        self.size = size
        self.category = category
        self.res = question(self.category)
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", size)
        self.Questions = self.font.render(self.res[0][1], 1, (0,0,0))
        self.categ = self.font.render(self.res[0][2], 1, (0,0,0))
        self.ranswer = self.font.render(self.res[0][3], 1, (0,0,0))
        self.wanswer1 = self.font.render(self.res[0][4], 1, (0,0,0))
        self.wanswer2 = self.font.render(self.res[0][5], 1, (0,0,0))
        self.rect1 = pygame.Rect(self.x * 1.2, self.y * 1.305 + self.y * 0.3, int(self.size * 14), int(self.size * 1.5))
        self.rect2 = pygame.Rect(self.x * 1.2, self.y * 1.450 + self.y * 0.3 + self.size, int(self.size * 14), int(self.size * 1.5))
        self.rect3 = pygame.Rect(self.x * 1.2, self.y * 1.595 + self.y * 0.3 + self.size * 2, int(self.size * 14), int(self.size * 1.5))
        self.maxsize = 39
        self.answers = [self.ranswer, self.wanswer1, self.wanswer2]
        self.answersc = [0, 1, 2]
        self.ra1 = random.choice(self.answersc)
        self.a1 = self.answers[self.ra1]
        self.answersc.remove(self.ra1)
        self.ra2 = random.choice(self.answersc)
        self.a2 = self.answers[self.ra2]
        self.answersc.remove(self.ra2)
        self.ra3 = self.answersc[0]
        self.a3 = self.answers[self.ra3]
        self.answer_correct = None

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

    def draw(self, surface, width, height):
        #print(self.ra1, self.ra2, self.ra3, self.answer_correct)
        mouse = pygame.mouse.get_pressed()
        self.IQ1 = pygame.transform.scale(IQ1, (int(width), int(height)))
        self.IQ2 = pygame.transform.scale(IQ2, (int(width), int(height)))

        if self.answer_correct == True:
            surface.blit(self.IQ1, (0,0))
        elif self.answer_correct == False:
            surface.blit(self.IQ2, (0,0))

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
            if mouse[0] and self.ra1 == 0:
                self.answer_correct = True
            elif mouse[0] and self.ra1 != 0:
                self.answer_correct = False
            self.srect1.fill(pygame.Color("Light Green"))
            self.srect1.set_alpha(68)
            surface.blit(self.srect1, (self.x * 1.2, self.y * 1.305 + self.y * 0.3))
        if self.rect2.collidepoint(pygame.mouse.get_pos()):
            if mouse[0] and self.ra2 == 0:
                self.answer_correct = True
            elif mouse[0] and self.ra2 != 0:
                self.answer_correct = False
            self.srect2.fill(pygame.Color("Light Green"))
            self.srect2.set_alpha(68)
            surface.blit(self.srect2, (self.x * 1.2, self.y * 1.450 + self.y * 0.3 + self.size))
        if self.rect3.collidepoint(pygame.mouse.get_pos()):
            if mouse[0] and self.ra3 == 0:
                self.answer_correct = True
            elif mouse[0] and self.ra3 != 0:
                self.answer_correct = False
            self.srect3.fill(pygame.Color("Light Green"))
            self.srect3.set_alpha(68)
            surface.blit(self.srect3, (self.x * 1.2, self.y * 1.595 + self.y * 0.3 + self.size * 2))
