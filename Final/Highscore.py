import MySQLdb

def High_score(Name_player,High_score,Player_wins,Player_loses,Win_loss_ratio):
    query = ( "INSERT INTO High_Score VALUES (%s, %s, %s, %s, %s)")
    print(query)
    
    db = MySQLdb.connect("5.79.70.63", "Boardgame", "groep12017", "Boardgame")
    cursor = db.cursor()

    cursor.execute(query, (Name_player,High_score,Player_wins,Player_loses,Win_loss_ratio))
  
    db.commit()

   
    db.close()





def Overview_score():
    query = """SELECT * FROM High_Score ORDER BY High_score DESC LIMIT 10"""
    
    db = MySQLdb.connect("5.79.70.63", "Boardgame", "groep12017", "Boardgame")

    cursor = db.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    result = data
    db.close()

    return result

print(Overview_score())

Score = Overview_score()


resultLines = []


playeramount = 10
for i in range(playeramount):
    resultLines.append("%s %i %i %i %i" % (Score[i][0], Score[i][1], Score[i][2], Score[i][3], Score[i][4]))


print(resultLines)



