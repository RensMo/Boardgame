import pygame

import mysql
from mysql.connector import errorcode

db = {
'user': 'Boardgame',
'password': 'groep12017',
'host': '5.79.70.63',
'database': 'Boardgame',
'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**db)
cursor = cnx.cursor()

if cnx.is_connected():
    print("Connected to MYSQL database")


class sql:

    dbinfo = {
        'user': 'Boardgame',
        'password': 'groep12017',
        'host': '5.79.70.63',
        'database': 'Boardgame',
        'raise_on_warnings': True,
    }

    def __init__(self):
        self.db = mysql.connector.connect(**self.dbinfo)

    def query(self,sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def rows(self):
        return self.db.cursor().rowcount

sqlI = sql()
quest = sqlI.query("""select Question,Category,Right_answer, Wrong_answer, Wrong_answer2 from Vragen ORDER BY RAND() LIMIT 1""")

class Questions:
    def __init__(self, x, y, size):
        self.Questions = quest[0][0]
        self.categ = quest[0][1]
        self.ranswer = quest[0][2]
        self.wanswer1 = quest[0][3]
        self.wanswer2 = quest[0][4]
        self.x = x
        self.y = y
        self.size = size
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", self.size)

        self.B1 = Button(self.x * 0.12, self.y * 0.29, self.x * 0.23, self.y * 0.14, I1)
        self.B2 = Button(self.x * 0.12, self.y * 0.44, self.x * 0.23, self.y * 0.14, I2)
        self.B3 = Button(self.x * 0.12, self.y * 0.59, self.x * 0.23, self.y * 0.14, I3)

    def draw(self, surface):
        surface.blit(self.Questions, (self.x, self.y))
        self.B1.draw(surface)
        self.B2.draw(surface)
        self.B3.draw(surface)
        surface.blit(self.ranswer, (self.x, self.y + self.y * 0.1))
        surface.blit(self.wanswer1, (self.x, self.y + self.y * 0.1))
        surface.blit(self.wanswer2, (self.x, self.y + self.y * 0.1))
