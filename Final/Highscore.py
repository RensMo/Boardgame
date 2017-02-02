import pygame
import MySQLdb

def High_score(Name_player,Player_wins,Player_loses):
    query = "INSERT INTO High_Score (Name_player, Player_wins, Player_loses) VALUES (%s, %s, %s)"
    query2 = "INSERT INTO High_Score (Name_player, Player_wins, Player_loses) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE"
    print(query)
    
    db = MySQLdb.connect("5.79.70.63", "Boardgame", "groep12017", "Boardgame")
    cursor = db.cursor()

    cursor.execute(query, (Name_player,Player_wins,Player_loses))
  
    db.commit()

    db.close()


def Overview_score():
    query = """SELECT * FROM High_Score ORDER BY Player_wins DESC LIMIT 10"""
    
    db = MySQLdb.connect("5.79.70.63", "Boardgame", "groep12017", "Boardgame")

    cursor = db.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    result = data
    db.close()

    return result

Score = Overview_score()
resultLines = []


playeramount = 10
for i in range(playeramount):
    resultLines.append("%s %i %i" % (Score[i][0], Score[i][1], Score[i][2]))

class Highscore:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", size)
        self.playeramount = 10
        self.resultLines = []

    def update(self):
        for i in range(self.playeramount):
            self.resultLines.append("%s %i %i" % (Score[i][0], Score[i][1], Score[i][2]))
        self.p1n = self.font.render(self.resultLines[0][0], 1, (0,0,0))
        self.p1w = self.font.render(self.resultLines[0][1], 1, (0,0,0))
        self.p1l = self.font.render(self.resultLines[0][2], 1, (0,0,0))
        self.p2n = self.font.render(self.resultLines[1][0], 1, (0,0,0))
        self.p2w = self.font.render(self.resultLines[1][1], 1, (0,0,0))
        self.p2l = self.font.render(self.resultLines[1][2], 1, (0,0,0))
        self.p3n = self.font.render(self.resultLines[2][0], 1, (0,0,0))
        self.p3w = self.font.render(self.resultLines[2][1], 1, (0,0,0))
        self.p3l = self.font.render(self.resultLines[2][2], 1, (0,0,0))
        self.p4n = self.font.render(self.resultLines[3][0], 1, (0,0,0))
        self.p4w = self.font.render(self.resultLines[3][1], 1, (0,0,0))
        self.p4l = self.font.render(self.resultLines[3][2], 1, (0,0,0))
        self.p5n = self.font.render(self.resultLines[4][0], 1, (0,0,0))
        self.p5w = self.font.render(self.resultLines[4][1], 1, (0,0,0))
        self.p5l = self.font.render(self.resultLines[4][2], 1, (0,0,0))
        self.p6n = self.font.render(self.resultLines[5][0], 1, (0,0,0))
        self.p6w = self.font.render(self.resultLines[5][1], 1, (0,0,0))
        self.p6l = self.font.render(self.resultLines[5][2], 1, (0,0,0))
        self.p7n = self.font.render(self.resultLines[6][0], 1, (0,0,0))
        self.p7w = self.font.render(self.resultLines[6][1], 1, (0,0,0))
        self.p7l = self.font.render(self.resultLines[6][2], 1, (0,0,0))
        self.p8n = self.font.render(self.resultLines[7][0], 1, (0,0,0))
        self.p8w = self.font.render(self.resultLines[7][1], 1, (0,0,0))
        self.p8l = self.font.render(self.resultLines[7][2], 1, (0,0,0))
        self.p9n = self.font.render(self.resultLines[8][0], 1, (0,0,0))
        self.p9w = self.font.render(self.resultLines[8][1], 1, (0,0,0))
        self.p9l = self.font.render(self.resultLines[8][2], 1, (0,0,0))
        self.p10n = self.font.render(self.resultLines[9][0], 1, (0,0,0))
        self.p10w = self.font.render(self.resultLines[9][1], 1, (0,0,0))
        self.p10l = self.font.render(self.resultLines[9][2], 1, (0,0,0))

    def draw(self, surface):
        surface.blit(self.p1n, (self.x, self.y + self.size * 0))
        surface.blit(self.p1w, (self.x, self.y + self.size * 0))
        surface.blit(self.p1l, (self.x, self.y + self.size * 0))
        surface.blit(self.p2n, (self.x, self.y + self.size * 1))
        surface.blit(self.p2w, (self.x, self.y + self.size * 1))
        surface.blit(self.p2l, (self.x, self.y + self.size * 1))
        surface.blit(self.p3n, (self.x, self.y + self.size * 2))
        surface.blit(self.p3w, (self.x, self.y + self.size * 2))
        surface.blit(self.p3l, (self.x, self.y + self.size * 2))
        surface.blit(self.p4n, (self.x, self.y + self.size * 3))
        surface.blit(self.p4w, (self.x, self.y + self.size * 3))
        surface.blit(self.p4l, (self.x, self.y + self.size * 3))
        surface.blit(self.p5n, (self.x, self.y + self.size * 4))
        surface.blit(self.p5w, (self.x, self.y + self.size * 4))
        surface.blit(self.p5l, (self.x, self.y + self.size * 4))
        surface.blit(self.p6n, (self.x, self.y + self.size * 5))
        surface.blit(self.p6w, (self.x, self.y + self.size * 5))
        surface.blit(self.p6l, (self.x, self.y + self.size * 5))
        surface.blit(self.p7n, (self.x, self.y + self.size * 6))
        surface.blit(self.p7w, (self.x, self.y + self.size * 6))
        surface.blit(self.p7l, (self.x, self.y + self.size * 6))
        surface.blit(self.p8n, (self.x, self.y + self.size * 7))
        surface.blit(self.p8w, (self.x, self.y + self.size * 7))
        surface.blit(self.p8l, (self.x, self.y + self.size * 7))
        surface.blit(self.p9n, (self.x, self.y + self.size * 8))
        surface.blit(self.p9w, (self.x, self.y + self.size * 8))
        surface.blit(self.p9l, (self.x, self.y + self.size * 8))
        surface.blit(self.p10n, (self.x, self.y + self.size * 9))
        surface.blit(self.p10w, (self.x, self.y + self.size * 9))
        surface.blit(self.p10l, (self.x, self.y + self.size * 9))

High_score("Rens", 1, 34875)
