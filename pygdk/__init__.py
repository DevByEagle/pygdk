# Global Imports
import customtkinter as ctk

window = ctk.CTk()

def init(width, height, title):
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.mainloop()
