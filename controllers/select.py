import cv2
import os

from tkinter import filedialog, Toplevel, Label, Button, Canvas, NW
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
        self.frame.photo_btn.config(command=self.camera_capture)
        self.frame.generate_btn.config(command=self.changeToResultView)
    
    def selectImage(self):
        global filename
        filename = filedialog.askopenfilename(initialdir="/images", title="Select Image", filetypes=(("png images", "*.png"), ("jpg images", "*.jpg")))
        img = Image.open(filename)
        self.change_image(img)
    
    def camera_capture(self):
        self.popup = Toplevel(self.frame)
        self.popup.title("Camera")
        self.canvas = Canvas(self.popup, width=640, height=480)
        self.canvas.grid(row=0, column=0)
        self.capture_btn = Button(self.popup, text="Capture", command=self.captured_image)
        self.capture_btn.grid(row=1, column=0)

        # OpenCV variables
        self.video_capture = cv2.VideoCapture(0)
        self.current_image = None

        self.update_webcam()

        self.popup.mainloop()

    def update_webcam(self):
        ret, frame = self.video_capture.read()

        if ret:
            self.current_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.photo = ImageTk.PhotoImage(image=self.current_image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
            self.popup.after(15, self.update_webcam)
    
    def captured_image(self):
        if self.current_image is not None:
            self.change_image(self.current_image)

            # tutup window camera
            self.popup.destroy()

    def change_image(self, image):
        global img
        img = image.resize((300, 200), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        self.frame.canvas_image.itemconfig(self.frame.image_container, image=img)

    def changeToResultView(self):
        try:
            # ganti image di frame result dan kirim gambar ke ML server
            self.view.frames["result"].selected_img.config(image=img)

            # URL endpoint untuk mengirim gambar
            url = 'https://vlm2jkrd-5000.asse.devtunnels.ms/predict'  # Ganti dengan URL API Anda

            # Mengirim gambar ke server
            self.model.wajah_model.send_image(url, filename)
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

