import math

def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print('jadi luas persegi yang sisinya', sisi, 'adalah', luas)
    print('jadi keliling persegi yang sisinya', sisi, 'adalah', keliling)

def persegipanjang(panjang,lebar):
    luas = panjang * lebar
    keliling = panjang + lebar * 2
    print('jadi luas persegi panjang yang panjang dan lebarnya', panjang, 'dan', lebar,'adalah', luas)
    print('jadi keliling persegi panjang yang panjang dan lebarnya', panjang, 'dan',lebar , 'adalah', keliling)

def lingkaran(jari):
    luas = 22/7 * jari * jari
    keliling = 2 * 22/7 * jari
    print('jadi luas lingkaran yang jari-jarinya', jari, 'adalah', luas)
    print('jadi keliling lingkaran yang jari-jarinya', jari, 'adalah', keliling)

def segitiga_samasisi(sisi,alas,tinggi):
    luas = 1/2 * alas * tinggi
    keliling = sisi * 3
    print('jadi luas segitiga sama sisi yang alas dan tinggi nya', alas,'dan', tinggi, 'adalah', luas)
    print('jadi keliling segitiga sama sisi yang sisinya', sisi, 'adalah', keliling)

def trapesiumsamakaki(atas, bawah, miring, tinggi):
    luas = atas + bawah / 2 * tinggi
    keliling = miring * 2 + atas + bawah
    print('jadi luas trapesium sama sisi yang sisi dan tinggi nya', atas, bawah ,'dan', tinggi, 'adalah', luas)
    print('jadi keliling trapesium sama sisi yang sisinya', atas, miring, bawah, miring, 'adalah', keliling)

def belahketupat(sisi, di1, di2):
    luas = 1/2 * di1 * di2
    keliling = sisi * 4
    print('jadi luas belah ketupat yang diagonalnya', di1, 'dan', di2, 'adalah', luas)
    print('jadi keliling belah ketupat sama sisi yang sisinya', sisi, 'adalah', keliling)

def jajargenjang(atasbawah, kirikanan, tinggi):
    luas = 1/2 * atasbawah * tinggi
    keliling = atasbawah + kirikanan * 2
    print('jadi luas jajargenjang adalah', atasbawah,'dan', tinggi, 'adalah', luas)
    print('jadi keliling jajargenjang adalah', atasbawah,  kirikanan, atasbawah,  kirikanan, 'adalah', keliling)