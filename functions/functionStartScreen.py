from config.createObjects import btnGroup, scr, player, computer

def startScreen():
    btnGroup[0].update(scr.window)
    player.update(sign = 'start')
    computer.update(sign = 'start')