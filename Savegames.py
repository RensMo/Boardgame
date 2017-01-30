import cPickle as pickle

def saveGame():
    allNames = []
    for sprite in alites:
        allNames.append(spritl_spre.get_name())
    playerTraits = (player.get_x(), player.get_y(),
                    player.get_inventory(), player.get_location())
    saveObject(playerTraits, 'learnpygame_player_save.obj')
    saveObject(allNames, 'learnpygame_sprite_save.obj')

def saveObject(obj, filename):
    with open(filename, 'w') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
