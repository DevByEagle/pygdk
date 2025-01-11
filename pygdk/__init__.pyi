# Global Imports
from typing import NoReturn

#======================================
# Window and Graphics Device Functions
#======================================
def init(width: int, height: int, title: str) -> NoReturn: ...
def show() -> None: ...

#======================================
# Font and Text Functions
#======================================
def drawText(text: str, font=("Arial", 12), color="black") -> None: ...
