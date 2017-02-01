import MySQLdb

def Add_question(Q_id,Question,Category,Right_answer,Wrong_answer,Wrong_answer2):
    query = ( "INSERT INTO Vragen VALUES (%s, %s, %s, %s, %s)")
    print(query)
    # Open database connection
    db = MySQLdb.connect("5.79.70.63", "Boardgame", "groep12017", "Boardgame")

    cursor = db.cursor()

    cursor.execute(query, (Q_id,Question,Category,Right_answer,Wrong_answer,Wrong_answer2))
    db.commit()



    # disconnect from server
    db.close()


Add_question(ID,vraag,Category,Goede antwoord,Foute antwoord1, Foute antwoord2)


Question_nr = 21
Question_nr += 1

class Add_questions:
    def __init__(self, x, y, size):

        self.x = x
        self.y = y
        self.size = size

    def draw(self, surface):

        surface.blit(self., (self.x, self.y))
        surface.blit(self., (self.x, self.y + self.y * 0.2))
        surface.blit(self., (self.x, self.y + self.y * 0.4))
        surface.blit(self., (self.x, self.y + self.y * 0.6))