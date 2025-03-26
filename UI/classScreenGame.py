import pygame as pg
from pygame.display import set_mode, set_caption, set_icon
from pygame.image import load

from dataclasses import dataclass

@dataclass
class ScreenGame:
    size: tuple = (1000, 700)
    color: str = '#1B8181'
    caption: str = ''
    icon: str = ''

    def __post_init__(self):
        self.window = set_mode(self.size)
        if self.caption:
            set_caption(self.caption)
        if self.icon:
            set_icon(load(self.icon))
