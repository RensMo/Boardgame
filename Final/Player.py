import pygame
#githuphup

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