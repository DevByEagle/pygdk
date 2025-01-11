import customtkinter as ctk

window: ctk.CTk = None


def init(width, height, title):
    global window

    if window is None:
        window = ctk.CTk()

    window.title(title)
    window.geometry(f"{width}x{height}")
    
    ctk.set_appearance_mode("System")

    window.mainloop()
