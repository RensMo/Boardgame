import MySQLdb
import pygame

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
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", size)
        self.Questions = self.font.render(res[0][1], 1, (0,0,0))
        self.categ = self.font.render(res[0][2], 1, (0,0,0))
        self.ranswer = self.font.render(res[0][3], 1, (0,0,0))
        self.wanswer1 = self.font.render(res[0][4], 1, (0,0,0))
        self.wanswer2 = self.font.render(res[0][5], 1, (0,0,0))
        self.x = x
        self.y = y
        self.size = size
        self.maxsize = 40

    def update(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", size)
        self.Questions = self.font.render(res[0][1], 1, (0,0,0))
        self.categ = self.font.render(res[0][2], 1, (0,0,0))
        self.ranswer = self.font.render(res[0][3], 1, (0,0,0))
        self.wanswer1 = self.font.render(res[0][4], 1, (0,0,0))
        self.wanswer2 = self.font.render(res[0][5], 1, (0,0,0))

    def draw(self, surface):
        if len(res[0][1]) > self.maxsize:
            self.Questions1 = self.font.render(res[0][1][:self.maxsize], 1, (0,0,0))
            self.Questions2 = self.font.render(res[0][1][self.maxsize:], 1, (0,0,0))
            surface.blit(self.Questions1, (self.x, self.y))
            surface.blit(self.Questions2, (self.x, self.y + self.size))
        else:
            surface.blit(self.Questions, (self.x, self.y))
        surface.blit(self.ranswer, (self.x * 1.25, self.y * 1.315 + self.y * 0.3))
        surface.blit(self.wanswer1, (self.x * 1.25, self.y * 1.451 + self.y * 0.3 + self.size))
        surface.blit(self.wanswer2, (self.x * 1.25, self.y * 1.582 + self.y * 0.3 + self.size * 2))
