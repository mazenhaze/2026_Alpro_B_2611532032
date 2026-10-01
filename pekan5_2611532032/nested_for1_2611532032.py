# buat file dengan nama nested_for1_2032.py
# buat program untuk nested for dalam python
# nama variabel ditambah 4 digit terakhir nim contoh: ipk_2032
# program ini menggunakan fungsi input()

batas_2032 = int(input("masukkan nilai batas: "))
for line_2032 in range(1, batas_2032 + 1 ):
    for j_2032 in range(1, (-1 * line_2032 + batas_2032) + 1):
        print(".", end=" ")
    print(line_2032)