import customtkinter as ctk

class Surface:
    def __init__(self, size, title):
        self.window = ctk.CTk()

        self.window.geometry(f"{int(size.x)}x{int(size.y)}")
        self.window.title(title)

    def show(self):
        self.window.mainloop()
