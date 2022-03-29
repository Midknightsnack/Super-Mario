import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group

class Level(Sprite):

  def __init__(self, game):
    super().__init__()
    self.game = game
    self.screen = game.screen
    self.settings = game.settings

  def update(self):
    pass

  def draw(self): 
    with open('images/level_loc.txt', "r") as file:
      if 'X' in file.read:
        ground = pg.image.load('images/Ground_Brick.png').convert()
        self.screen.blit(ground, (200, 400))    # what is the positioning of the text file?
      if 'B' in file.read:
        ground = pg.image.load('images/Red_Brick.png').convert()
        self.screen.blit(ground, (200, 400))
      if '?' in file.read:
        ground = pg.image.load('images/Item_Brick.png').convert()
        self.screen.blit(ground, (200, 400))
      if 'R' in file.read:
        ground = pg.image.load('images/Stair_Brick.png').convert()
        self.screen.blit(ground, (200, 400))   