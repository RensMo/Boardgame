# Save a dictionary into a pickle file.
import pickle
import pygame

height = 800
width = 600
screen = pygame.display.set_mode((height, width))
white = (255, 255, 255)
score = 0
name = "Luciano"

file = {name, score}

pickle.dump(file, open("save.p", "wb"))
