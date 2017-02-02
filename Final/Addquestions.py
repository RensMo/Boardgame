import MySQLdb

def Add_question(Q_id, Question, Category, Right_answer, Wrong_answer, Wrong_answer2):
    query = ( "INSERT INTO Vragen VALUES (%s, %s, %s, %s, %s, %s)")

    print(query)
    # Open database connection
    db = MySQLdb.connect("5.79.70.63", "Boardgame", "groep12017", "Boardgame")

    cursor = db.cursor()

    cursor.execute(query, (Q_id, Question, Category, Right_answer, Wrong_answer, Wrong_answer2))
    db.commit()



    # disconnect from server
    db.close()
