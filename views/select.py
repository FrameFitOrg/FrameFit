from tkinter import Frame, Label, Button
from PIL import Image, ImageTk

class SelectView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Select Picture")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.initial_img = Image.open("./images/upload-img.png")
        self.initial_photo = ImageTk.PhotoImage(self.initial_img)
        self.image = Label(self, image=self.initial_photo)
        self.image.grid(row=1, column=0, padx=10, pady=10)

        self.upload_btn = Button(self, text="upload")
        self.upload_btn.grid(row=2, column=0, padx=10, pady=10)

        self.generate_btn = Button(self, text="Generate")
        self.generate_btn.grid(row=3, column=0, padx=10, pady=10)