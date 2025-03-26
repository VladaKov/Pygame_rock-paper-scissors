import pygame as pg

class Sounds:
    def playBackgroundMusic(self, backMusic = None):
        if backMusic:
            self.bsckMusic = pg.mixer.music.load(backMusic)
            pg.mixer.music.set_volume(0.2)
            pg.mixer.music.play(-1)

    def playGameSound(self, sound = None):
        if sound:
            self.sound = pg.mixer.Sound(sound)
            pg.mixer.Sound.set_volume(self.sound, 0.4)
            pg.mixer.Sound.play(self.sound)