# buat file dengan nama jumlah_genap_2611532032.py
# buat program untuk menghitung jumlah bilangan genap dalam rentang tertentu
# nama variabel ditambah 4 digit terakhir nim contoh: jumlah_genap_2032
# program ini menggunakan fungsi input()

ulang = int(input("masukkan nilai batas: "))

jumlah_2032 = 0
for i_2032 in range(1, ulang + 1):
    if i_2032 % 2 == 0:
        print(i_2032, end=" ")
        jumlah_2032 = jumlah_2032 + i_2032

        if i_2032 < ulang:
            print("+", end=" ")
        else:
            print(" = ", jumlah_2032, end=" ")
print()
print("jumlah =", jumlah_2032)