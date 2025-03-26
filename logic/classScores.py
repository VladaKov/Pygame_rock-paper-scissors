from dataclasses import dataclass

@dataclass
class Scores:
    playerScore: int = 0
    computerScore: int = 0
    
    def changeScores(self, playerScore = 0, computerScore = 0):
        self.playerScore += playerScore
        self.computerScore += computerScore