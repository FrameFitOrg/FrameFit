import requests

class Wajah():
    def __init__(self):
        self.bentuk_wajah = 0
        self.mata = 0
        self.hidung = 0
        self.pipi = 0
        self.mulut = 0

    def ambilSemuaGambar(self):
        # isi sesuai dengan endpoint di database api
        pass

    def kirimGambar(self, bentuk_wajah, mata, hidung, pipi, mulut):
        # isi sesuai dengan endpoint di database api
        pass

    def ambilBentukWajah(self):
        # isi sesuai dengan endpoint di ML api
        pass

    def send_image(self, url, image_path):
        try:
            # Membuka file gambar
            with open(image_path, 'rb') as file:
                # Membuat permintaan POST
                response = requests.post(url, files={'image': file})
                
                # Menampilkan respons dari server
                print(response)
                print(response.json())
        except Exception as e:
            # print(str(e))
            print("fuck")

