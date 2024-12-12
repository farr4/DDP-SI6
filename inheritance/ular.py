from animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembangbiak, bisa, jenis_lidah):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.jenis_lidah = jenis_lidah
        self.bisa = bisa 

    def cetak_ular(self):
        super().cetak()
        print(f'hewan ini {self.bisa} dan memiliki jenis lidah {self.jenis_lidah}')

piton = ular('piton', ' daging', 'darat', 'bertelur', 'tidak berbisa', 'bercabang' )
piton.cetak_ular()

kobra = ular('kobra', 'daging','darat', 'bertelur', 'berbisa', 'bercabang')
kobra.cetak_ular()
