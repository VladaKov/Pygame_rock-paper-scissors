from config.createObjects import btnGroup, scr, player, computer, isChoice

def choiceScreen():
    for btn in btnGroup[1:]:
        btn.update(scr.window)
        
    player.update(sign = 'start')
    computer.update(sign = 'start')
    
    if player.playerChoice:
        if not computer.playerChoice:
            computer.setChoice()
        isChoice.changeIsChoice