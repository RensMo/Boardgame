""" Python test Rens
19-01-2017"""

import pygame
from Tile import *
from Player import *

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
    return False


# Main program logic
def program():
    pygame.init()
    size = 600, 600
    screen = pygame.display.set_mode(size)

    grid_width = 4
    grid_height = 12
    entry_tile = build_square_matrix(grid_width, grid_height)

    # Set up the default font
    font = pygame.font.Font(None, 30)

    #create player
    player1 = Player("Rens", entry_tile)

    clock = pygame.time.Clock()

    while not process_events():
        clock.tick(10)

        # Clear the screen
        screen.fill((0, 0, 0))
        entry_tile.Draw(screen)

        player1.Update()
        player1.Draw(screen)

        # Flip the screen
        pygame.display.flip()


# Start the program
program()
