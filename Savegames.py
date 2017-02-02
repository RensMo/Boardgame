import pickle

class Player:
    def __init__(self, name, tile):
        self.Name = name
        self.Tile = tile
        self.Colour = (255, 255, 255)
        self.StartCat = None

    def Draw(self, screen, width, height, pos_x, pos_y):
            margin_x = 0.1 * width
            margin_y = 0.1 * height
            pygame.draw.ellipse(screen, self.Colour,
                                (pos_x + (margin_x + width) * self.Tile.Position.X + margin_x,
                                 pos_y + (-margin_y - height) * self.Tile.Position.Y - margin_y,
                                 width,
                                 height))
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
