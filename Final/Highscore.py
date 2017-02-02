
import MySQLdb

def High_score(Name_player,Player_wins,Player_loses):
    query = ( "INSERT INTO High_Score VALUES (%s, %s, %s)")
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


print(resultLines)
