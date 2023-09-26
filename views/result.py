from tkinter import Frame, Label, Button
from PIL import Image, ImageTk

class ResultView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(1, weight=1)

        self.header = Label(self, text="Result")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.selected_img = Label(self)
        self.selected_img.grid(row=1, column=0, rowspan=5, padx=10, pady=10)

        self.face_shape_txt = Label(self, text="Wajah: Oval")
        self.face_shape_txt.grid(row=1, column=1)

        self.eyes_shape_txt = Label(self, text="Mata: sipit")
        self.eyes_shape_txt.grid(row=2, column=1)

        self.nose_shape_txt = Label(self, text="Hidung: mancung")
        self.nose_shape_txt.grid(row=3, column=1)

        self.cheeks_shape_txt = Label(self, text="Pipi: tirus")
        self.cheeks_shape_txt.grid(row=4, column=1)

        self.mouth_shape_txt = Label(self, text="Bibir: thin")
        self.mouth_shape_txt.grid(row=5, column=1)

        self.back_btn = Button(self, text="Back")
        self.back_btn.grid(row=7, column=0, padx=10, pady=10)
