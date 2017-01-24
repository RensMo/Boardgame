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

    def Draw(self, screen, width, height):
        margin_x = width * 0.10
        margin_y = height * 0.10
        pygame.draw.rect(screen, self.Colour,
                         ((margin_x + width) * self.Position.X + margin_x,
                          (margin_y + height) * self.Position.Y + margin_y,
                          width,
                          height))
        if self.Right.Position.X != 0:
            self.Right.Draw(screen, width, height)

        if self.Position.X == 0 and self.Up != None:
            self.Up.Draw(screen, width, height)


def build_matrix(width, height):
    entry_point = None
    under_line = None
    prev_node = None
    most_left_node = None
    for line in range(height):
        for tile in range(width):
            # Assign colours
            if tile <= 1 * (width // 4) - 1:
                colour = (255, 0, 0)  # red
            elif tile <= 2 * (width // 4) - 1:
                colour = (0, 255, 0)  # green
            elif tile <= 3 * (width // 4) - 1:
                colour = (255, 255, 0)  # yellow
            else:
                colour = (0, 0, 255)  # blue

            # Create Node
            node = Tile(colour, Position(tile, line))

            if line == 0 and tile == 0:  # Define entry point
                entry_point = node

            if tile == 0:
                prev_node = node
                most_left_node = node
            elif tile == width - 1:
                node.Left = prev_node
                most_left_node.Left = node
                node.Right = most_left_node
                prev_node.Right = node
                prev_node = node
            else:
                node.Left = prev_node
                prev_node.Right = node
                prev_node = node

            if line > 0:
                node.Down = under_line  # Define .Down
                under_line.Up = node  # Define .up
                under_line = under_line.Right

        prev_node = most_left_node
        under_line = prev_node
    return entry_point