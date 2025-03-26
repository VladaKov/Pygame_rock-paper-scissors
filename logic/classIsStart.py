from dataclasses import dataclass

@dataclass
class IsStart:
    isStart: bool = False

    def changeIsStart(self):
        self.isStart = not self.isStart