import pygame
import random
from Node import *

class Position:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class Tile:
    def __init__(self, colour, position, category):
        self.Colour = colour
        self.Category = category
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
                          height), 2)

        if self.Right.Position.X != 0 and self.Right.Position.X != 0.5:
            self.Right.Draw(screen, width, height, pos_x, pos_y)

        if (self.Position.X == 0 or self.Position.X == 0.5) and self.Up != None:
            if self.Up.Position.X > 0.5:
                self.Up.Left.Draw(screen, width, height, pos_x, pos_y)
            else:
                self.Up.Draw(screen, width, height, pos_x, pos_y)


def build_matrix():
    width = 8
    mid_height = 11

    top_height = 6

    entry_point = None
    under_line = None
    prev_node = None
    most_left_node = None

    # bottom matrix
    for tile in range(0, width, 2):
        colour = (169, 169, 169)  # grey (bottom area)
        node = Tile(colour, Position(tile + 0.5, 0), None)
        if tile == 0:
            node.Category = "Entertainment"
            entry_point = node
            prev_node = node
        if tile == 2 or tile == 4:
            if tile == 2:
                node.Category = "Geography"
            if tile == 4:
                node.Category = "History"
            prev_node.Right = node
            node.Left = prev_node
            prev_node = node
        if tile == 6:
            node.Category = "History"
            prev_node.Right = node
            node.Left = prev_node
            node.Right = entry_point
            entry_point.Left = node

    # mid part matrix
    for line in range(1, mid_height):
        for tile in range(width):
            # Assign colours
            if tile <= 1 * (width // 4) - 1:
                colour = (255, 0, 0)  # red
                category = "Entertainment"
            elif tile <= 2 * (width // 4) - 1:
                colour = (0, 255, 0)  # green
                category = "Geography"
            elif tile <= 3 * (width // 4) - 1:
                colour = (255, 255, 0)  # yellow
                category = "History"
            else:
                colour = (0, 0, 255)  # blue
                category = "Sport"

            node = Tile(colour, Position(tile, line), category)

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

            if line == 1:
                if tile == 0:
                    under_line = entry_point
                node.Down = under_line
                if tile % 2 != 0:
                    random_nr = random.randint(0, 1)
                    if random_nr == 1:
                        under_line.Up = node.Left
                    else:
                        under_line.Up = node
                    under_line = under_line.Right

            if line > 1:
                node.Down = under_line  # Define .Down
                under_line.Up = node  # Define .up
                under_line = under_line.Right
        prev_node = most_left_node
        under_line = prev_node

    # top part matrix
    for line in range(mid_height, mid_height + top_height):
        for tile in range(0, width, 2):
            # Assign colours
            if tile <= 1 * (width // 4) - 1:
                colour = (255, 0, 0)  # red
                category = "Entertainment"
            elif tile <= 2 * (width // 4) - 1:
                colour = (0, 255, 0)  # green
                category = "Geography"
            elif tile <= 3 * (width // 4) - 1:
                colour = (255, 255, 0)  # yellow
                category = "History"
            else:
                colour = (0, 0, 255)  # blue
                category = "Sport"
            if line == mid_height + top_height - 1:
                colour = (0, 0, 0)  # Black (Finish point!)
                category = "Finish"

            node = Tile(colour, Position(tile + 0.5, line), category)

            if line == mid_height:
                random_nr = random.randint(0, 1)
                if random_nr == 1:
                    node.Down = under_line
                else:
                    node.Down = under_line.Right

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

            if line > mid_height:
                node.Down = under_line
                under_line.Up = node
                under_line = under_line.Right

        prev_node = most_left_node
        under_line = prev_node

    return entry_point