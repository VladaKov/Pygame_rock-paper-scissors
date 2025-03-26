from dataclasses import dataclass, InitVar

@dataclass
class DrawText:
    screen: object = None
    text: InitVar[str] = ''
    color: str = '#D87764'
    font: object = None
    pos: tuple = (0, 0)

    def __post_init__(self, text: str):
        self.text = text if type(text) == str else str(text)

    def update(self):
        self.textView = self.font.render(self.text, True, self.color)
        self.screen.window.blit(self.textView, self.pos)