# buat file dengan nama konstanta_2611532032.py
# program ini menggunakan konstanta untuk menghitung luas lingkarasn
# nama vvariabel ditambah 4 digit terakhir NIM

from typing import Final, final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2032 = float(input('Masukkan nilai jari-jari: '))
luas_2032 = PI * jari_2032 * jari_2032
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2032, luas_2032))