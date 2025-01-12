import customtkinter as ctk

def drawText(surface, text, font, color):
    label = ctk.CTkLabel(surface.window, text=text, font=font, text_color=color)
    label.pack()

__all__ = ['drawText']