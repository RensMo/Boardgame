import pygame
from Node import *

#githuphup

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

    def Draw(self, screen, width, height, pos_x, pos_y):
        margin_x = width * 0.10
        margin_y = height * 0.10

        pygame.draw.rect(screen, self.Colour,
                         (pos_x + (margin_x + width) * self.Position.X + margin_x,
                          pos_y + (-margin_y - height) * self.Position.Y - margin_y,
                          width,
                          height))

        if self.Right.Position.X != 0 and self.Right.Position.X != 0.5:
            self.Right.Draw(screen, width, height, pos_x, pos_y)

        if (self.Position.X == 0 or self.Position.X == 0.5) and self.Up != None:
            self.Up.Draw(screen, width, height, pos_x, pos_y)


def build_matrix():
    width = 8
    bot_height = 11

    top_height = 6

    entry_point = None
    under_line = None
    prev_node = None
    most_left_node = None

    #bottom part matrix
    for line in range(bot_height):
        for tile in range(width):
            # Assign colours
            if line == 0:
                colour = (169, 169, 169)  # grey (bottom area)
            elif tile <= 1 * (width // 4) - 1:
                colour = (255, 0, 0)  # red
            elif tile <= 2 * (width // 4) - 1:
                colour = (0, 255, 0)  # green
            elif tile <= 3 * (width // 4) - 1:
                colour = (255, 255, 0)  # yellow
            else:
                colour = (0, 0, 255)  # blue

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

    # top part matrix
    for line in range(bot_height, bot_height + top_height):
        for tile in range(0, width, 2):
            # Assign colours
            if line == bot_height + top_height - 1:
                colour = (0, 0, 0)  # Black (Finish point!)
            elif tile <= 1 * (width // 4) - 1:
                colour = (255, 0, 0)  # red
            elif tile <= 2 * (width // 4) - 1:
                colour = (0, 255, 0)  # green
            elif tile <= 3 * (width // 4) - 1:
                colour = (255, 255, 0)  # yellow
            else:
                colour = (0, 0, 255)  # blue

            node = Tile(colour, Position(tile + 0.5, line))

            if line == bot_height:
                node.Down = under_line
                under_line.Up = node
                under_line.Right.Up = node
                under_line = under_line.Right.Right
            if tile == 0:
                prev_node = node
                most_left_node = node
            elif tile == width - 2:
                node.Left = prev_node
                most_left_node.Left = node
                node.Right = most_left_node
                prev_node.Right = node
                prev_node = node
            else:
                node.Left = prev_node
                prev_node.Right = node
                prev_node = node

            if line > bot_height:
                node.Down = under_line
                under_line.Up = node
                under_line = under_line.Right

        prev_node = most_left_node
        under_line = prev_node

    return entry_point