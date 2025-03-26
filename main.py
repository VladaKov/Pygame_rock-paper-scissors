import pygame as pg
from sys import exit
from config.createObjects import scr

pg.init()

from classes.classGame import Game


if __name__ == '__main__':
    game = Game()
    game.runGame()
    pg.quit()
    exit()


