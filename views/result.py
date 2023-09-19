from tkinter import Frame, Label, Button
from PIL import Image, ImageTk

class ResultView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Result")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.selected_img = Label(self)
        self.selected_img.grid(row=1, column=0, padx=10, pady=10)

        self.face_shape_txt = Label(self, text="Your face is: Oval")
        self.face_shape_txt.grid(row=2, column=0, padx=10, pady=10)

        self.back_btn = Button(self, text="Back")
        self.back_btn.grid(row=3, column=0, padx=10, pady=10)
