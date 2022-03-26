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

  def draw(self): pass
    # image = self.image()
    # rect = image.get_rect()
    # rect.x, rect.y = self.rect.x, self.rect.y
    # self.screen.blit(image, rect)
    # file = open('images/level_loc.txt', "r")
    # print(file.read())
    # self.screen.blit(file, (200, 550))
    # file.close()
