from .surface import Surface
from .font import Font
import customtkinter as ctk

def drawText(surface: Surface, text: str, font: Font):
    if hasattr(surface, 'label'):
        surface.label.configure(text=text)
    else:
        surface.label = ctk.CTkLabel(surface.window, text=text, font=font.get_font())
        surface.label.pack()