from animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembangbiak, warna, jenis):
        super().__init__(nama, makanan, hidup, berkembangbiak)
        self.warna = warna
        self.jenis = jenis

    def cetak_ikan(self):
        super().cetak()
        print(f'warna ikan ini adalah warna {self.warna}, dan jenis ikan ini adalah {self.jenis}' )

salmon = ikan('Ikan salmon', 'serangga air', 'air', 'bertelur', 'oranye untuk dagingnya', 'air tawar maupun laut' )
salmon.cetak_ikan()

lele = ikan('ikan lele', 'cacing', 'air', 'bertelur', 'abu-abu', 'air tawar' )
lele.cetak_ikan()