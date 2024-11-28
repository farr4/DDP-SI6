print('## 1. Biodata Diri ##')
print('===========================')
nama = 'Fara Nabila'
nim = '0110124216'
rombel = '24SI06'
asdos = 'Ka Jaya'
alamat = 'Jalan Nurul Falah, Cimanggis, Depok' # Ini perbaikan

print(f'Namaku {nama}')
print(f'NIMku {nim}')
print(f'Rombelku {rombel}')
print(f'Asdosku {asdos}')
print(f'Alamatku {alamat}')


# Menghitung Berat Badan Ideal
print()
print('===Berat Badan Ideal===')

tinggi_badan = 165
berat_badan_ideal = (tinggi_badan-100)-(tinggi_badan-100)*1/10

print('Berat badan ideal untuk tinggi', tinggi_badan, 'CM adalah', berat_badan_ideal, 'kg')


# Menghitung Celcius Ke Fahrenheit
print()
print('===Suhu Celcius Ke Fahrenheit===')

celcius = int(input('Masukan Suhu Celcius: '))

rumus_fahrenheit = int(celcius*9/5)+32

print(celcius, 'Celcius sama dengan', rumus_fahrenheit, 'Fahrenheit')


# Menghitung Luas Tabung
print("")
print("=====Luas Tabung======")

phi = 3.14
jari2 = int(input('Masukan nilai jari-jari: '))
tinggi = int(input('Masukan nilai tinggi: '))

luas_permukaan =  2*phi*jari2*(jari2+tinggi)
luas_alas = phi*jari2**2
luas_selimut = 2 * phi * jari2 * tinggi

print('Luas Permukaan Tabung Adalah: ', luas_permukaan)
print('Luas Alas Tabung Adalah: ', luas_alas)
print('Luas Selimut Tabung Adalah: ', luas_selimut)


# Menghitung Keliling Tabung
print()
print('===Keliling Tabung===')

r = int(input("Masukan Jari-Jari: "))
tinggi = int(input("Masukan tinggi: "))
phi = 3.14
rumus = 2*phi*r*tinggi

print('Keliling Tabung Adalah', rumus)