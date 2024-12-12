from animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembangbiak, jenisbulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.jenisbulu = jenisbulu
        self.bunyi = bunyi 

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenisbulu} dan berbunyi {self.bunyi} ')

beo = Burung('Burung Beo', 'biji-bijian', 'udara', 'bertelur', 'biru dan oranye', 'kamu jelek')
beo.cetak_burung()

gagak = Burung('Burung Elang', 'bangkai hewan lain', 'udara darat', 'bertelur', 'hitam', 'gakgakgakgak')
gagak.cetak_burung()