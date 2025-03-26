from config.createObjects import player, computer, scores

def winScreen():
    if scores.playerScore > scores.computerScore:
        player.update(sign = 'win')
        computer.update(sign = 'start')
    elif scores.playerScore < scores.computerScore:
        player.update(sign = 'start')
        computer.update(sign = 'win')
    else:
        player.update(sign = 'win')
        computer.update(sign = 'win')