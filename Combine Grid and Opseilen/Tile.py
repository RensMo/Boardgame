import pygame
from Node import *

class Position:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class Tile:
    def __init__(self, colour, position):
        self.Colour = colour
        self.Up = None
        self.Down = None
        self.Left = None
        self.Right = None
        self.Position = position

    def Draw(self, screen):
        margin = 5
        width = 30
        height = 30
        pygame.draw.rect(screen, self.Colour,
                         ((margin + width) * self.Position.X + margin,
                          (margin + height) * self.Position.Y + margin,
                          width,
                          height))
        if self.Right != None:
            self.Right.Draw(screen)

        if self.Position.X == 0 and self.Down != None:
            self.Down.Draw(screen)


def build_square_matrix(width, height):
    entry_point = None
    above_line = None
    prev_node = None
    for line in range(height):
        for tile in range(width):
            if tile <= 1 * (width // 4) - 1:
                colour = (255, 0, 0)  # red
            elif tile <= 2 * (width // 4) - 1:
                colour = (0, 255, 0)  # green
            elif tile <= 3 * (width // 4) - 1:
                colour = (255, 255, 0)  # yellow
            else:
                colour = (0, 0, 255)  # blue

            node = Tile(colour, Position(tile, line))

            if line == 0 and tile == 0:
                entry_point = node
            if tile == 0:
                prev_node = node
            else:
                prev_node.Right = node
                node.Left = prev_node
                prev_node = node
            if line > 0:
                node.Up = above_line
                above_line.Down = node
                above_line = above_line.Right

        while prev_node.Left != None:
            prev_node = prev_node.Left
        above_line = prev_node
    return entry_point