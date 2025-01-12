import customtkinter as ctk

window = ctk.CTk()

def init(width, height, title):
    window.title(title)
    window.geometry(f"{width}x{height}")
    
def show():
    window.mainloop()

def drawText(text, color, font=("Arial", 12)):
    label = ctk.CTkLabel(window, text=text, font=font, text_color=color.RGBName)
    label.pack()

