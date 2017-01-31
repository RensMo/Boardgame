import MySQLdb

def High_score(Name_player,High_score,Player_wins,Player_loses,Win_loss_ratio):
    query = ( "INSERT INTO High_Score VALUES (%s, %s, %s, %s, %s)")
    print(query)
    # Open database connection
    db = MySQLdb.connect("5.79.70.63", "Boardgame", "groep12017", "Boardgame")

    cursor = db.cursor()

    cursor.execute(query, (Name_player,High_score,Player_wins,Player_loses,Win_loss_ratio))
    #data = cursor.commit()
    db.commit()

    #result = data

    # disconnect from server
    db.close()


High_score('player1',185,5,6,5)

