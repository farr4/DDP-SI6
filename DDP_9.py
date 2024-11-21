print('\n----celcius ke fahrenheit----')
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

print('\n----Mencari Bilangan Genap----')
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print('\n----Keterangan Lulus dan Tidak Lulus----')
#rata-rata nilai kelulusan 70
def skor(nilai):
    if nilai >= 80:
        print('Lulus')
    else:
        print('Tidak Lulus')
skor(80)
skor(60)

print('\n----Mencetak Bilangan Ganjil----')
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1,2):
        print(i, end=' ') # end fungsinya biar deretnya kesamping

bil_ganjil(20)