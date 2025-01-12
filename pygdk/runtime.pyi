from pygdk.color import Color
from typing import NoReturn

#======================================
# Window and Graphics Device Functions
#======================================
def init(width: int, height: int, title: str) -> NoReturn: ...
def show() -> None: ...

#======================================
# Font and Text Functions
#======================================
def drawText(text: str, color: Color, font=("Arial", 12)) -> None: ...
