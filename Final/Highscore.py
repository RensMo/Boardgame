
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
        self.p1 = self.font.render(self.resultLines[0], 1, (0,0,0))
        self.p2 = self.font.render(self.resultLines[1], 1, (0,0,0))
        self.p3 = self.font.render(self.resultLines[2], 1, (0,0,0))
        self.p4 = self.font.render(self.resultLines[3], 1, (0,0,0))
        self.p5 = self.font.render(self.resultLines[4], 1, (0,0,0))
        self.p6 = self.font.render(self.resultLines[5], 1, (0,0,0))
        self.p7 = self.font.render(self.resultLines[6], 1, (0,0,0))
        self.p8 = self.font.render(self.resultLines[7], 1, (0,0,0))
        self.p9 = self.font.render(self.resultLines[8], 1, (0,0,0))
        self.p10 = self.font.render(self.resultLines[9], 1, (0,0,0))

    def draw(self, surface):
        surface.blit(self.p1, (self.x, self.y + self.size * 0))
        surface.blit(self.p2, (self.x, self.y + self.size * 1))
        surface.blit(self.p3, (self.x, self.y + self.size * 2))
        surface.blit(self.p4, (self.x, self.y + self.size * 3))
        surface.blit(self.p5, (self.x, self.y + self.size * 4))
        surface.blit(self.p6, (self.x, self.y + self.size * 5))
        surface.blit(self.p7, (self.x, self.y + self.size * 6))
        surface.blit(self.p8, (self.x, self.y + self.size * 7))
        surface.blit(self.p9, (self.x, self.y + self.size * 8))
        surface.blit(self.p10, (self.x, self.y + self.size * 9))

High_score("Rens", 1, 34875)