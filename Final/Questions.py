
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

class questions:
    def __init__(self):
        self.Questions = quest[0][0]
        self.categ = quest[0][1]
        self.ranswer = quest[0][2]
        self.wanswer = quest[0][3]
        self.wansert = quest[0][4]


questions()



