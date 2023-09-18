from tkinter import filedialog
from PIL import ImageTk, Image

from models.main import Model
from views.main import View

class SelectController:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["select"]
        self._bind()
    
    def _bind(self):
        self.frame.upload_btn.config(command=self.selectImage)
        self.frame.generate_btn.config(command=self.changeToResultView)
    
    def selectImage(self):
        global img
        filename = filedialog.askopenfilename(initialdir="/images", title="Select Image", filetypes=(("png images", "*.png"), ("jpg images", "*.jpg")))
        img = Image.open(filename)
        img = img.resize((300, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        self.frame.image.config(image=img)

    def changeToResultView(self):
        self.view.switch("result")

