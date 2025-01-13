from .math import Vector2
from typing import Sequence
import customtkinter as ctk

class Surface:
    def __init__(self, size=(0, 0)):
        self.window = ctk.CTk()
        ctk.set_appearance_mode("system")

        width, height = self.__get_values(size)
        self.window.geometry(f"{width}x{height}")
        
    def __get_values(self, coord):
        if isinstance(coord, tuple):
            x, y = coord
            return x, y
        elif isinstance(coord, Vector2):
            x = coord.x
            y = coord.y
            return x, y
        elif isinstance(coord, list) or isinstance(coord, Sequence):
            return tuple(coord) 

    def show(self):
        self.window.mainloop()
