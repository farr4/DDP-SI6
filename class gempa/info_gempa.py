from Gempa import *

# membuat objek gempa dengan lokasi dan skala
gempa1 = Gempa('Banten', 1.2)

# info gempa
print('## Informasi Gempa Bumi ##')
print()
gempa1.dampak() # memanggil method dampak()

#gempa kedua
gempa2 = Gempa('Palu', 6.1)
print()
print('## Informasi Gempa Bumi ##')
print()
gempa2.dampak()

#gempa ketiga
gempa3 = Gempa('Cianjur', 5.6)
print()
print('## Informasi Gempa Bumi ##')
print()
gempa3.dampak()

#gempa keempat
gempa4 = Gempa('Jayapura', 3.3)
print()
print('## Informasi Gempa Bumi ##')
print()
gempa4.dampak()

#gempa kelima
gempa5 = Gempa('Garut', 4.0)
print()
print('## Informasi Gempa Bumi ##')
print()
gempa5.dampak()