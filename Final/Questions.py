import MySQLdb

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


res =  question()
questions = res[0][1]
answer = res[0][3]
wrongans = res[0][4]
wrongans2 = res[0][5]
print(questions)

class Questions:
    def __init__(self, x, y, size):
        self.Questions = res[0][1]
        self.categ = res[0][2]
        self.ranswer = res[0][3]
        self.wanswer1 = res[0][4]
        self.wanswer2 = res[0][5]
        self.x = x
        self.y = y
        self.size = size
        self.font = pygame.font.Font("Assets/Berlin Sans FB.ttf", self.size)

    def draw(self, surface):
        surface.blit(self.Questions, (self.x, self.y))
        surface.blit(self.ranswer, (self.x, self.y + self.y * 0.1))
        surface.blit(self.wanswer1, (self.x, self.y + self.y * 0.1))
        surface.blit(self.wanswer2, (self.x, self.y + self.y * 0.1))
