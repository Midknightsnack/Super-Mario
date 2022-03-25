import pygame as pg
from vector import Vector
from pygame.sprite import Sprite, Group
from pygame import mixer

class Mario(Sprite):

  def __init__(self, game):
    super().__init__()
    self.game = game
    self.screen = game.screen
    self.settings = game.settings
    self.image = pg.image.load('images/Mario_sprites.png')

  def update(self):
    pass

  def draw(self):
    # image = self.image()
    # rect = image.get_rect()
    # rect.x, rect.y = self.rect.x, self.rect.y
    # self.screen.blit(image, rect)
    self.screen.blit(self.image, (200, 550))