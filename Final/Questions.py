import mysql
from mysql.connector import errorcode

def question(category):
    db = {
    'user': 'Boardgame',
    'password': 'groep12017',
    'host': 'rens.xyz',
    'database': 'Boardgame',
    'raise_on_warnings': True,
    }

    cnx = mysql.connector.connect(**db)
    cursor = cnx.cursor()

    if cnx.is_connected():
        print("Connected to MYSQL database")


    cursor.execute("""select Question,Category,Right_answer, Wrong_answer, Wrong_answer2 from Vragen ORDER BY RAND() LIMIT 1""")

    result = cursor.fetchall()
    cursor.close()
    cnx.close()

    question = result[0][0]
    right_answer = result[0][2]
    wrong_answer1 = result[0][3]
    wrong_answer2 = result[0][4]

    print(question, right_answer, wrong_answer1, wrong_answer2)

question("Geography")
