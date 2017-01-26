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


questions = cursor.execute("""select Question,Category,Right_answer, Wrong_answer, Wrong_answer2 from Vragen ORDER BY RAND() LIMIT 1""")

print (cursor.fetchall())
cursor.close()
cnx.close()