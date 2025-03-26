from pygame.font import SysFont
from dataclasses import dataclass

@dataclass(frozen = True)
class Fonts:
    Robotomono: object = SysFont("Robotomono", 36)
    Robotomono: object = SysFont("Robotomono", 70)
