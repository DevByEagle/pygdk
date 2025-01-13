from .surface import Surface
from typing import Optional 

def init(width: int, height: int, title: Optional[str] = None) -> Surface:
    surface = Surface((width, height))
    surface.window.title(title)
    return surface
