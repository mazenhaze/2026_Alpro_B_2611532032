# buat file dengan nama nilai_nim.py
# buat program untuk nested if
# nama variabel ditambah 4 digit terakhir nim contoh: ipk_2032
# program ini menggunakan fungsi input()
# program konversi nilai angka menjadi huruf

nilai = int(input("inputkan nilai angka= "))

if nilai >= 81:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 60:
    print("C")
elif nilai >= 50:
    print("D")
else:
    print("E")