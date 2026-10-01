# buat file dengan nama nested_for3_2032.py
# buat program untuk nested for dalam python
# nama variabel ditambah 4 digit terakhir nim contoh: ipk_2032
# program ini menggunakan fungsi input()

batas_2032 = int(input("masukkan nilai batas: "))
for i_2032 in range(batas_2032 + 1):
    for j_2032 in range(batas_2032 + 1):
        print(i_2032 + j_2032, end="")
    print() # pindah ke baris berikutnya