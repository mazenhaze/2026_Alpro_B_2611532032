# buat file dengan nama aritmatika_2611532032.py
# buat program untuk operator aritmatika dalam python
# nama variabel ditambah 4 digit terakhir NIM contoh: a_2611532032
# program ini menggunakan fungsi input ()
# nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2032 = int(input("input angka-1: "))
angka2_2032 = int(input("input angka-2: "))

# penjumlahan
hasil = angka1_2032 + angka2_2032
print("\nOperator penjumlahan")
print("hasil =", hasil)

# pengurangan
hasil = angka1_2032 - angka2_2032
print("\nOperator pengurangan")
print("hasil =", hasil)

# perkalian
hasil = angka1_2032 * angka2_2032
print("\nOperator perkalian")
print("hasil =", hasil)

# pembagian, pembagian bulat, pembagian sisa
if angka2_2032 != 0:
    hasil = angka1_2032 / angka2_2032
    print("\nOperator pembagian")
    print("hasil =", hasil)

    hasil = angka1_2032 // angka2_2032
    print("\nOperator pembagian bulat")
    print("hasil =", hasil)

    hasil = angka1_2032 % angka2_2032
    print("\nOperator pembagian sisa")
    print("hasil =", hasil)
else:
    print("angka kedua tidak boleh bernilai 0.")

    # pangkat
hasil = angka1_2032 ** angka2_2032
print("\nOperator pangkat")
print("hasil =", hasil)
