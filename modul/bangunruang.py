import math

def kubus(sisi): 
    luas = 6 * sisi * sisi
    print(f'Luas Kubus {6} * {sisi} * {sisi} = {luas}')

def balok(panjang, lebar, tinggi):
    luas = 2 * (panjang*lebar + panjang*lebar + lebar*tinggi)
    print(f'Luas Balok {2} * {(panjang*lebar + panjang*lebar + lebar*tinggi)} = {luas}')

def kerucut(r, selimut):
    luas = math.pi * r (r + selimut)
    print(f'Luas Kerucut {math.pi} * {r} * {(r+selimut)} = {luas}' )

def tabung(r, tinggi):
    luas = 2 * math.pi * r (r+tinggi)
    print(f'Luas Tabung {2} * {math.pi} * {r} * {(r+tinggi)} = {luas}')

def bola(r):
    luas = 4 * math.pi * r ** 2
    print(f'Luas Tabung {4} * {math.pi} * {r} ** {2}  = {luas}')