import os
from random import randint

FPS = 165
WIDTH = 1900#px
HEIGHT = 1000#px

#World Size
wrld_size = 4
wrld_width = WIDTH * wrld_size
wrld_height = HEIGHT * wrld_size

import pygame as engine
entity = engine.sprite.Sprite
img_load = engine.image.load
refresh = engine.display.flip
group = engine.sprite.Group

from Engine.game import Game
game = Game(engine)
