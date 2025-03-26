from dataclasses import dataclass

@dataclass
class RotationCounter:
    counter: int = 6
    
    @property
    def decreaseCounter(self):
        if self.counter > 0:
            self.counter -= 1
