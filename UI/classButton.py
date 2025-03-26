import pygame as pg
from pygame.locals import MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame.display import set_mode, set_caption, set_icon
from pygame.image import load
from pygame.font import Font, SysFont

from dataclasses import dataclass, InitVar, field

pg.init()

'''
Класс кнопки
    pos - координаты левого верхнего угла
    size - ширина и высота кнопки
    text - текст на кнопке (необязательно)
    image - изображение на кнопке (необязательно)
    font - путь к файлу шрифта (необязательно)
    defaultFont - название системного шрифта (необязательно)
    fontSize - размер шрифта (необязательно)
    bgColor - цвет фона (необязательно)
    textColor - цвет текста (необязательно)
    hoverColor - цвет фона при наведении (необязательно)
    clickColor - цвет фона при нажатии (необязательно)
'''

@dataclass
class Button:
    pos: tuple = (0, 0)
    size: tuple = (50, 50)
    text: str = ''
    image: str = ''
    font: InitVar[str] = ""
    defaultFont: str = 'Robotomono'
    fontSize: int = 45
    bgColor: str = '#D87764'
    textColor: str = '#082C3F'
    hoverColor: str = '#AD4E45'
    clickColor: str = '#AD4E45'
    isHovered: bool = False
    isClicked: bool = False
    onClickReference: object = None
    referenceArgs: tuple = field(default_factory = tuple)
    referenceKwargs: dict = field(default_factory = dict)

    def __post_init__(self, font: str):
        self.rect = pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.font = Font(font, self.fontSize) if font else SysFont(self.defaultFont, self.fontSize)

    def update(self, surface):
        if self.isClicked:
            self.color = self.clickColor
        elif self.isHovered:
            self.color = self.hoverColor
        else:
            self.color = self.bgColor

        pg.draw.rect(surface, self.color, self.rect, border_radius = 20)

        if self.text:
            textSurface = self.font.render(self.text, True, self.textColor)
            textRect = textSurface.get_rect(center = self.rect.center)
            surface.blit(textSurface, textRect)

        if self.image:
            image = load(self.image)
            imageRect = image.get_rect(center = self.rect.center)
            surface.blit(image, imageRect)

    def handleEvent(self, event):
        if event.type == MOUSEMOTION:
            self.isHovered = self.rect.collidepoint(event.pos)
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and self.isHovered:
                self.isClicked = True
                if self.onClickReference:
                    self.onClickReference(*self.referenceArgs, **self.referenceKwargs)
        elif event.type == MOUSEBUTTONUP:
            self.isClicked = False


