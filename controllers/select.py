from tkinter import filedialog, Toplevel, Label, Button
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
        try:
            # ganti image di frame result
            self.view.frames["result"].selected_img.config(image=img)
        except NameError:
            self.img_is_not_selected_popup()

        self.view.switch("result")
    
    def img_is_not_selected_popup(self):
        popup = Toplevel(self.frame)
        popup.title("Alert")
        popup.geometry("200x100")
        alert = Label(popup, text="Select an image first")
        ok_btn = Button(popup, text="Ok", command=popup.destroy)
        alert.pack()
        ok_btn.pack()
        popup.mainloop()

