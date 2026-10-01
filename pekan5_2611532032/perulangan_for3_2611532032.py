# buat file dengan nama perulangan_for3_2032.py
# buat program untuk perulangan for dalam python
# nama variabel ditambah 4 digit terakhir nim contoh: ipk_2032
# program ini menggunakan fungsi input()

ulang = int(input("masukkan jumlah perulangan: "))

jumlah_2032 = 0
for i_2032 in range(1, ulang + 1):  
    print(i_2032, end=" ")
    jumlah_2032 = jumlah_2032 + i_2032

    if i_2032 < ulang:
        print("+", end=" ")
    else:
        print("=", end=" ")
print()
print("jumlah =", jumlah_2032)