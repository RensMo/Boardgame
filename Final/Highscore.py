import pygame
import MySQLdb

def High_score(Name_player,Player_wins,Player_loses):
    query = "INSERT INTO High_Score (Name_player, Player_wins, Player_loses) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE Name_player=Name_player, Player_wins=Player_wins+%s, Player_loses=Player_loses+%s"

    print(query)

    db = MySQLdb.connect("5.79.70.63", "Boardgame", "groep12017", "Boardgame")
    cursor = db.cursor()

    cursor.execute(query, (Name_player, Player_wins, Player_loses, Player_wins, Player_loses))
  
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

class Highscore:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", size)
        self.playeramount = 10
        self.resultLinesn = []
        self.resultLinesw = []
        self.resultLinesl = []
        self.resultLineswl = []

    def update(self):
        for i in range(self.playeramount):
            if i < 9:
                ic = "0" + str(i + 1)
            else:
                ic = str(i + 1)
            self.resultLinesn.append("%s %s" % (ic, Score[i][0]))
            self.resultLinesw.append("%i" % (Score[i][1]))
            self.resultLinesl.append("%i" % (Score[i][2]))
            try:
                wl = str((Score[i][1] / (Score[i][1] + Score[i][2])) * 100)[0:4]
            except ZeroDivisionError:
                wl = "0.00"
            self.resultLineswl.append(wl)
        self.p1n = self.font.render(self.resultLinesn[0], 1, (0,200,255))
        self.p1w = self.font.render(self.resultLinesw[0], 1, (0,200,255))
        self.p1l = self.font.render(self.resultLinesl[0], 1, (0,200,255))
        self.p1wl = self.font.render(self.resultLineswl[0], 1, (0,200,255))
        self.p2n = self.font.render(self.resultLinesn[1], 1, (0,200,255))
        self.p2w = self.font.render(self.resultLinesw[1], 1, (0,200,255))
        self.p2l = self.font.render(self.resultLinesl[1], 1, (0,200,255))
        self.p2wl = self.font.render(self.resultLineswl[1], 1, (0,200,255))
        self.p3n = self.font.render(self.resultLinesn[2], 1, (0,200,255))
        self.p3w = self.font.render(self.resultLinesw[2], 1, (0,200,255))
        self.p3l = self.font.render(self.resultLinesl[2], 1, (0,200,255))
        self.p3wl = self.font.render(self.resultLineswl[2], 1, (0,200,255))
        self.p4n = self.font.render(self.resultLinesn[3], 1, (0,200,255))
        self.p4w = self.font.render(self.resultLinesw[3], 1, (0,200,255))
        self.p4l = self.font.render(self.resultLinesl[3], 1, (0,200,255))
        self.p4wl = self.font.render(self.resultLineswl[3], 1, (0,200,255))
        self.p5n = self.font.render(self.resultLinesn[4], 1, (0,200,255))
        self.p5w = self.font.render(self.resultLinesw[4], 1, (0,200,255))
        self.p5l = self.font.render(self.resultLinesl[4], 1, (0,200,255))
        self.p5wl = self.font.render(self.resultLineswl[4], 1, (0,200,255))
        self.p6n = self.font.render(self.resultLinesn[5], 1, (0,200,255))
        self.p6w = self.font.render(self.resultLinesw[5], 1, (0,200,255))
        self.p6l = self.font.render(self.resultLinesl[5], 1, (0,200,255))
        self.p6wl = self.font.render(self.resultLineswl[5], 1, (0,200,255))
        self.p7n = self.font.render(self.resultLinesn[6], 1, (0,200,255))
        self.p7w = self.font.render(self.resultLinesw[6], 1, (0,200,255))
        self.p7l = self.font.render(self.resultLinesl[6], 1, (0,200,255))
        self.p7wl = self.font.render(self.resultLineswl[6], 1, (0,200,255))
        self.p8n = self.font.render(self.resultLinesn[7], 1, (0,200,255))
        self.p8w = self.font.render(self.resultLinesw[7], 1, (0,200,255))
        self.p8l = self.font.render(self.resultLinesl[7], 1, (0,200,255))
        self.p8wl = self.font.render(self.resultLineswl[7], 1, (0,200,255))
        self.p9n = self.font.render(self.resultLinesn[8], 1, (0,200,255))
        self.p9w = self.font.render(self.resultLinesw[8], 1, (0,200,255))
        self.p9l = self.font.render(self.resultLinesl[8], 1, (0,200,255))
        self.p9wl = self.font.render(self.resultLineswl[8], 1, (0,200,255))
        self.p10n = self.font.render(self.resultLinesn[9], 1, (0,200,255))
        self.p10w = self.font.render(self.resultLinesw[9], 1, (0,200,255))
        self.p10l = self.font.render(self.resultLinesl[9], 1, (0,200,255))
        self.p10wl = self.font.render(self.resultLineswl[9], 1, (0,200,255))

    def draw(self, surface):
        surface.blit(self.p1n, (self.x, self.y + self.size * 0))
        surface.blit(self.p1w, (self.x + self.size * 9.45, self.y + self.size * 0))
        surface.blit(self.p1l, (self.x + self.size * 11.1, self.y + self.size * 0))
        surface.blit(self.p1wl, (self.x + self.size * 12.5, self.y + self.size * 0))
        surface.blit(self.p2n, (self.x, self.y + self.size * 1))
        surface.blit(self.p2w, (self.x + self.size * 9.45, self.y + self.size * 1))
        surface.blit(self.p2l, (self.x + self.size * 11.1, self.y + self.size * 1))
        surface.blit(self.p2wl, (self.x + self.size * 12.5, self.y + self.size * 1))
        surface.blit(self.p3n, (self.x, self.y + self.size * 2))
        surface.blit(self.p3w, (self.x + self.size * 9.45, self.y + self.size * 2))
        surface.blit(self.p3l, (self.x + self.size * 11.1, self.y + self.size * 2))
        surface.blit(self.p3wl, (self.x + self.size * 12.5, self.y + self.size * 2))
        surface.blit(self.p4n, (self.x, self.y + self.size * 3))
        surface.blit(self.p4w, (self.x + self.size * 9.45, self.y + self.size * 3))
        surface.blit(self.p4l, (self.x + self.size * 11.1, self.y + self.size * 3))
        surface.blit(self.p4wl, (self.x + self.size * 12.5, self.y + self.size * 3))
        surface.blit(self.p5n, (self.x, self.y + self.size * 4))
        surface.blit(self.p5w, (self.x + self.size * 9.45, self.y + self.size * 4))
        surface.blit(self.p5l, (self.x + self.size * 11.1, self.y + self.size * 4))
        surface.blit(self.p5wl, (self.x + self.size * 12.5, self.y + self.size * 4))
        surface.blit(self.p6n, (self.x, self.y + self.size * 5))
        surface.blit(self.p6w, (self.x + self.size * 9.45, self.y + self.size * 5))
        surface.blit(self.p6l, (self.x + self.size * 11.1, self.y + self.size * 5))
        surface.blit(self.p6wl, (self.x + self.size * 12.5, self.y + self.size * 5))
        surface.blit(self.p7n, (self.x, self.y + self.size * 6))
        surface.blit(self.p7w, (self.x + self.size * 9.45, self.y + self.size * 6))
        surface.blit(self.p7l, (self.x + self.size * 11.1, self.y + self.size * 6))
        surface.blit(self.p7wl, (self.x + self.size * 12.5, self.y + self.size * 6))
        surface.blit(self.p8n, (self.x, self.y + self.size * 7))
        surface.blit(self.p8w, (self.x + self.size * 9.45, self.y + self.size * 7))
        surface.blit(self.p8l, (self.x + self.size * 11.1, self.y + self.size * 7))
        surface.blit(self.p8wl, (self.x + self.size * 12.5, self.y + self.size * 7))
        surface.blit(self.p9n, (self.x, self.y + self.size * 8))
        surface.blit(self.p9w, (self.x + self.size * 9.45, self.y + self.size * 8))
        surface.blit(self.p9l, (self.x + self.size * 11.1, self.y + self.size * 8))
        surface.blit(self.p9wl, (self.x + self.size * 12.5, self.y + self.size * 8))
        surface.blit(self.p10n, (self.x, self.y + self.size * 9))
        surface.blit(self.p10w, (self.x + self.size * 9.45, self.y + self.size * 9))
        surface.blit(self.p10l, (self.x + self.size * 11.1, self.y + self.size * 9))
        surface.blit(self.p10wl, (self.x + self.size * 12.5, self.y + self.size * 9))
