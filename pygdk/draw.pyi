from typing import Tuple
from .surface import Surface

def drawText(surface: Surface, text: str, font: Tuple[str, int], color) -> None: ... # TODO Change font to be a official pygdk font & add colors arg for text and backgroud

__all__ = ['drawText']