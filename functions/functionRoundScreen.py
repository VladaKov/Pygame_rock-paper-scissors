from config.createObjects import player, computer, scores

def roundScreen():
    player.update(sign = player.playerChoice)
    computer.update(sign = computer.playerChoice)
    
    if player.playerChoice == computer.playerChoice:
        scores.changeScores()
    elif player.playerChoice == "rock" and computer.playerChoice == "scissors":
        scores.changeScores(1, 0)
    elif player.playerChoice == "paper" and computer.playerChoice == "rock":
        scores.changeScores(1, 0)
    elif player.playerChoice == "scissors" and computer.playerChoice == "paper":
        scores.changeScores(1, 0)
    else:
        scores.changeScores(0, 1)