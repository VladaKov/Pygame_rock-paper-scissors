from dataclasses import dataclass

@dataclass
class IsChoice:
    isChoice: bool = False

    @property
    def changeIsChoice(self):
        self.isChoice = not self.isChoice