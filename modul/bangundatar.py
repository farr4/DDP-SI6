import math

def persegi (sisi):
    luas = sisi * sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas Persegi {sisi} * {sisi} = {luas}')

def persegi_pnjg(panjang, lebar):
    luas = panjang * lebar
    keliling =  2 * panjang + lebar
    print(f'Luas Persegi Panjang {panjang} * {lebar} = {luas}')

def segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi
    print(f'Luas Segitiga {1.5} * {alas} * {tinggi} = {luas}' )

def jajar_genjang(alas, tinggi):
    luas = alas * tinggi
    print(f'Luas Jajar Genjang {alas} * {tinggi} = {luas}' )

def lingkaran(r):
    luas = math.pi * r * r
    print(f'Luas Lingkaran {math.pi} * {r} * {r} = {luas}' )