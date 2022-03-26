import pygame as pg
import game_functions as gf
from sys import exit
from time import sleep
from settings import Settings
from pygame import mixer
from mario import Mario
from create_level import Level


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        
        pg.display.set_caption("Space Mario")
        
        self.mario = Mario(game=self)
        # self.level = Level(game=self)
        self.mixer = mixer.init()
         
    def restart(self):
        pass


    def update(self):
        self.mario.update()

    def draw(self):
        #self.screen.fill(self.bg_color)
        level_1_bg = pg.image.load(f'images/level_bg.png').convert()
        self.screen.blit(level_1_bg, (0, 0))
        # self.level.draw()
        self.mario.draw()
        pg.display.flip()
        
    def play(self):
        self.finished = False
        self.music = pg.mixer.Sound('sounds/SMB_theme.wav')
        self.music.play(loops=-1)
        self.music.set_volume(0.1)

        while not self.finished:
            self.update()
            self.draw()
            gf.check_events(game=self)   # exits game if QUIT pressed
        self.game_over()

    def game_over(self): 
        # self.gameover_music = pg.mixer.Sound('sounds/game_over.wav')
        # self.gameover_music.play()
        # self.gameover_music.set_volume(0.2)
        print('\nGAME OVER!\n\n') 
        self.music.stop()
        exit()    

def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()