from UI.classScreenGame import ScreenGame
from UI.classButton import Button
from UI.classColors import Colors
from UI.classFonts import Fonts

from logic.classIsChoice import IsChoice
from logic.classIsStart import IsStart
from logic.classRotationCounter import RotationCounter
from logic.classRoundsCounter import RoundsCounter
from logic.classScores import Scores

from classes.classPlayer import Player
from classes.classSounds import Sounds



isStart = IsStart()
isChoice = IsChoice()
rotationCounter = RotationCounter()
roundsCounter = RoundsCounter(5)
scores = Scores()
sounds = Sounds()
fonts = Fonts()
colors = Colors()



scr = ScreenGame(size = (1000, 700),
                  color = '#1B8181',
                  caption = 'Камень Ножницы Бумага',
                  icon = 'images/win.png')


player = Player(name = 'Игрок',
                  screen = scr,
                  size = (252, 326),
                  centerPos = (180, scr.size[1] // 2))


computer = Player(name = 'Компьютер',
                  autoGame = True,
                  screen = scr,
                  size = (252, 326),
                  centerPos = (scr.size[0] - 180, scr.size[1] // 2))



btnGroup = [Button(pos = (scr.size[0] // 2 - 125, scr.size[1] // 2),
                  size = (250, 60),
                  text = 'Старт',
                  onClickReference = isStart.changeIsStart),
            Button(pos = (scr.size[0] // 2 - 220, scr.size[1] // 2 + 100), #расположение кнопоки
                  size = (145, 55), # размер кнопок
                  text = 'Камень',
                  referenceKwargs = dict(value = 'rock'),
                  onClickReference = player.setChoice),
            Button(pos = (scr.size[0] // 2 - 64, scr.size[1] // 2 + 100),#расположение кнопоки
                  size = (145, 55), # размер кнопок
                  text = 'Ножницы',
                  referenceKwargs = dict(value = 'scissors'),
                  onClickReference = player.setChoice),
            Button(pos = (scr.size[0] // 2 + 95, scr.size[1] // 2 + 100),#расположение кнопоки
                  size = (145, 55), # размер кнопок
                  text = 'Бумага',
                  referenceKwargs = dict(value = 'paper'),
                  onClickReference = player.setChoice)]


