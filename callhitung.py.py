 
print('--------gunakan modul-----------')
import hitung
hitung.tambah(5,2)
hitung.kurang(10,3)
hitung.kali(5,6)

print('\n--gunakan modul yg ada dgn alias--')
import hitung as ht
ht.bagi(20,2)
ht.pangkat(2,3)

print('\n--gunakan modul dgn memanggil sebagian fungsinya--')
from hitung import tambah,kurang
tambah(20,30)
kurang(2,3)

print('\n--gunakan modul dgn memanggil seluruh fungsinya--')
from hitung import *
tambah(20,30)
kurang(2,3)
kali(5,6)
bagi(20,2)
pangkat(2,3)

print('\n--gunakan modul dgn memanggil sebagian fungsinya dengan alias--')
from hitung import tambah as add, kali as x, kurang as m 
 
add(3,7)
x(10,10)
m(10,5)