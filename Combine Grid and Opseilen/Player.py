import pygame

class Player:
    def __init__(self, name, tile):
        self.Name = name
        self.Tile = tile
        self.Colour = (255, 255, 255)

    def Draw(self, screen):
        margin = 5
        width = 30
        height = 30
        pygame.draw.ellipse(screen, self.Colour,
                         ((margin + width) * self.Tile.Position.X + margin,
                          (margin + height) * self.Tile.Position.Y + margin,
                          width,
                          height))

    def Update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.Tile.Left != None:
            self.Tile = self.Tile.Left
        elif keys[pygame.K_RIGHT] and self.Tile.Right != None:
            self.Tile = self.Tile.Right

        if keys[pygame.K_UP] and self.Tile.Up != None:
            self.Tile = self.Tile.Up
        elif keys[pygame.K_DOWN] and self.Tile.Down != None:
            self.Tile = self.Tile.Down