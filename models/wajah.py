#import sqlite3

class Wajah():
    def __init__(self):
        #self.conn = sqlite3.connect('framefit.db')
        #self.cursor = self.conn.cursor()

        self.bentuk_wajah = 0
        self.mata = 0
        self.hidung = 0
        self.pipi = 0
        self.mulut = 0

    def ambilSemuaGambar(self):
        data = self.cursor.execute("SELECT * FROM wajah")
        return data

    def kirimGambar(self, bentuk_wajah, mata, hidung, pipi, mulut):
        self.bentuk_wajah = bentuk_wajah
        self.mata = mata
        self.hidung = hidung
        self.pipi = pipi
        self.mulut = mulut
        data = self.cursor.execute("INSERT INTO wajah (bentuk_wajah, mata, hidung, pipi, mulut) VALUES ({a}, {b}, {c}, {d}, {e})".format(a = self.bentuk_wajah, b = self.mata, c = self.hidung, d = self.pipi, e = self.mulut))
        return data
