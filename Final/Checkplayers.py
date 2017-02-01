def Checkplayers(p1n, p2n, p3n, p4n, p1c, p2c, p3c, p4c, p1sc, p2sc, p3sc, p4sc, p):
    playerN = []
    playerC = []
    playerSC = []

    if p == 2:
        playerN = [p1n.atext, p2n.atext]
        playerC = [p1c.color, p2c.color]
        playerSC = [p1sc.category, p2sc.category]
    elif p == 3:
        playerN = [p1n.atext, p2n.atext, p3n.atext]
        playerC = [p1c.color, p2c.color, p3c.color]
        playerSC = [p1sc.category, p2sc.category, p3sc.category]
    elif p == 4:
        playerN = [p1n.atext, p2n.atext, p3n.atext, p4n.atext]
        playerC = [p1c.color, p2c.color, p3c.color, p4c.color]
        playerSC = [p1sc.category, p2sc.category, p3sc.category, p4sc.category]

    ready = True
    
    for c in playerN:
        playerN.remove(c)
        for v in playerN:
            if c == v:
                ready = False
    for c in playerC:
        playerC.remove(c)
        for v in playerC:
            if c == v:
                ready = False
    for c in playerSC:
        playerSC.remove(c)
        for v in playerSC:
            if c == v:
                ready = False

    print(p, ready)

    return ready