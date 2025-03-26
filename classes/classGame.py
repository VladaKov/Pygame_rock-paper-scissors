import pygame as pg
from pygame.locals import *
from pygame.transform import scale, flip
from pygame.image import load

from icecream import ic

from config.createObjects import scr, btnGroup, player, computer, isStart, isChoice, rotationCounter, roundsCounter, scores, sounds

from functions.functionCreateText import createText
from functions.functionStartScreen import startScreen
from functions.functionChoiceScreen import choiceScreen
from functions.functionRotationScreen import rotationScreen
from functions.functionRoundScreen import roundScreen
from functions.functionWinScreen import winScreen



class Game:
    def __init__(self):
        self.run = True
        self.fps = 120
        self.clock = pg.time.Clock()
        sounds.playBackgroundMusic('sounds/backMusic.mp3')

    def eventGame(self):
        for event in pg.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.run = False

            for btn in btnGroup:
                btn.handleEvent(event)

    def runGame(self):
        while self.run:
            scr.window.fill(scr.color)

            self.eventGame()
            createText()

            if not isStart.isStart:
                startScreen()
            elif isStart.isStart and not isChoice.isChoice:
                choiceScreen()
            elif isStart.isStart and isChoice.isChoice:
                if rotationCounter.counter > 0:
                    if rotationCounter.counter % 2 == 0:
                        sounds.playGameSound('sounds/sign.mp3')
                    rotationScreen()
                    rotationCounter.decreaseCounter
                    pg.display.update()
                    pg.time.delay(500)
                else:
                    if roundsCounter.rounds > 0:
                        roundsCounter.decreaseRounds
                        rotationCounter.counter = 6
                        isChoice.changeIsChoice
                        scr.window.fill(scr.color)
                        roundScreen()
                        createText()
                        pg.display.update()
                        pg.time.delay(2000)
                        player.playerChoice = ''
                        computer.playerChoice = ''
            if roundsCounter.rounds <= 0:
                scr.window.fill(scr.color)
                pg.mixer.music.pause()
                sounds.playGameSound('sounds/win.mp3')
                winScreen()
                createText()
                pg.display.update()
                pg.time.delay(3500)
                pg.mixer.music.unpause()
                roundsCounter.rounds = 5
                isStart.changeIsStart()
                scores.playerScore = 0
                scores.computerScore = 0

            pg.display.update()
            self.clock.tick(self.fps)


