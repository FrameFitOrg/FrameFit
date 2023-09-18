from tkinter import Tk

class Root(Tk):
    def __init__(self):
        super().__init__()

        min_width = 900
        min_height = 500

        self.minsize(width=min_width, height=min_height)
        self.title("FrameFit")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)