from dataclasses import dataclass

@dataclass
class RoundsCounter:
    rounds: int = 0
    
    @property
    def decreaseRounds(self):
        if self.rounds > 0:
            self.rounds -= 1