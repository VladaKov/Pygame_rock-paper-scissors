from pygame.transform import rotozoom, flip, scale
from pygame.image import load

from random import choice
from collections import OrderedDict
from dataclasses import dataclass, field


@dataclass
class Player:
    name: str = ''
    autoGame: bool = False
    screen: object = None
    size: tuple = (0, 0)
    flStart: bool = False
    flRotation: bool = False
    flWin: bool = False
    centerPos: tuple = (0, 0)

    playerChoice: str = ''
    signDict: dict = field(default_factory = OrderedDict)

    def __post_init__(self):
        self.signDict['rock'] = scale(load('images/rock.png'), self.size) if not self.autoGame else flip(scale(load('images/rock.png'), self.size), True, False)

        self.signDict['paper'] = scale(load('images/paper.png'), self.size) if not self.autoGame else flip(scale(load('images/paper.png'), self.size), True, False)

        self.signDict['scissors'] = scale(load('images/scissors.png'), self.size) if not self.autoGame else flip(scale(load('images/scissors.png'), self.size), True, False)

        self.signDict['start'] = scale(load('images/start.png'), self.size) if not self.autoGame else flip(scale(load('images/start.png'), self.size), True, False)
        self.commonRect = self.signDict['start'].get_rect(center = self.centerPos)
        self.signRotation = self.signDict['start']

        self.signDict['win'] = flip(scale(load('images/win.png'), self.size), True, False) if not self.autoGame else scale(load('images/win.png'), self.size)

    def setChoice(self, value = 'auto'):
        if value != 'auto':
            self.playerChoice = value
        else:
            self.playerChoice = choice(list(self.signDict.keys())[:3])

    def rotation(self, angle = 0):
        if  self.flRotation:
            self.flRotation = False
            self.signRotation = self.signDict['start']
            self.commonRect = self.signDict['start'].get_rect(center = self.centerPos)
        else:
            self.flRotation = True
            self.commonRect = self.signRotation.get_rect(center = (self.centerPos[0] - 50, self.centerPos[1] + 50))
            self.signRotation = rotozoom(self.signDict['start'], angle, 1)

    def update(self, sign = None):
        if not self.flRotation:
            self.screen.window.blit(self.signDict[sign], self.commonRect)
        else:
            self.screen.window.blit(self.signRotation, self.commonRect)