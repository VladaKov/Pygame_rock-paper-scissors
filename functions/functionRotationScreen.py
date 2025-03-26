from config.createObjects import player, computer

def rotationScreen():
    player.rotation(angle = -45)
    computer.rotation(angle = 45)
    player.update(sign = 'start')
    computer.update(sign = 'start')