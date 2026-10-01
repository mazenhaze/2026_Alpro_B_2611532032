# buat file dengan nama perulangan_for2_2032.py
# buat program untuk perulangan for dalam python
# nama variabel ditambah 4 digit terakhir nim contoh: ipk_2032
# program ini menggunakan fungsi input()

ulang_2032 = int(input("masukkan jumlah perulangan: "))
print("perulangan ke-0 sampai ke-", ulang_2032-1)
for i_2032 in range(ulang_2032):
    print(i_2032, end=" ")
print()
print("perulangan ke-1 sampai ke-", ulang_2032)
for i_2032 in range(1, ulang_2032+1):
    print(i_2032, end=" ")