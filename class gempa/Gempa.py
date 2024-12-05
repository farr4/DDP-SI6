class Gempa:
    #Konstruktor Inisialisasi Atribut
    def __init__(self, lokasi, skala) :
        self.lokasi = lokasi
        self.skala = skala

    # Method Penentu Skala 
    def dampak(self):
        #logika statement
        if self.skala < 2:
            print('Gempa Tidak Berasa')
        elif 2 <= self.skala <=4:
            print('Gempa Bangunan Retak-Retak')
        elif 4 <= self.skala <= 6:
            print('Gempa Bangunan Roboh')
        elif self.skala >6: 
            print('Gempa Bangunan Roboh dan Berpotensi Tsunami')

        #menampilkan lokasi dan skala gempa
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Lokasi Gempa: {self.skala}')
        