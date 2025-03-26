from UI.classDrawText import DrawText
from UI.classTextGroup import TextGroup

from config.createObjects import scr, fonts, colors, roundsCounter, scores


def createText():

        textGroup = TextGroup(group = [DrawText(screen = scr,
                                                font = fonts.Robotomono,
                                                color = colors.orange,
                                                pos = (scr.size[0] // 2 - 230, 75), text = f'Осталось раундов: {roundsCounter.rounds}'),
                                        DrawText(screen = scr,
                                                font = fonts.Robotomono,
                                                color = colors.orange,
                                                pos = (scr.size[0] // 2 - 50, scr.size[1] - 140), text = f'{scores.playerScore} : {scores.computerScore}'),])

        textGroup.update()