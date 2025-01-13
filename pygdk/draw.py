from .surface import Surface
from .font import Font
from typing import Optional
import customtkinter as ctk

def drawText(surface: Surface, text: str, font: Optional[Font] = None):
    if hasattr(surface, 'label'):
        surface.label.configure(text=text)
    else:
        surface.label = ctk.CTkLabel(surface.window, text=text)
        if font is not None:
            surface.label.configure(font=font.get_font())
        surface.label.pack()
