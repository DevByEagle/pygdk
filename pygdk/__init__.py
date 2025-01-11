# Global Imports
import customtkinter as ctk

window = ctk.CTk()

def init(width, height, title):
    window.title(title)
    window.geometry(f"{width}x{height}")

def drawText(text, font=("Arial", 12), color="black"):
    label = ctk.CTkLabel(window, text=text, font=font, text_color=color)
    label.pack()

def show():
    window.mainloop()
