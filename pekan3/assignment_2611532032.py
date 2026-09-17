# buat file dengan nama assignmentt_2611532032.py
# nama variabel ditambah 4 digit terakhir NIM contoh: a_261153203
# program ini menggunakan fungsi input ()
# nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# program operator assignment dalam python

angka1_2032 = int(input("input angka-1: "))
angka2_2032 = int(input("input angka-2: "))

print("\nNilai awal angka1 =", angka1_2032)
print("Nilai angka2 =", angka2_2032)

# assignment biasa
hasil = angka1_2032
print("\nOperator assignment biasa")
print("hasil =", hasil)

# assignment penambahan
hasil = angka1_2032
hasil += angka2_2032
print("\nOperator assignment penambahan (+=)")
print("hasil =", hasil)

# assignment pengurangan
hasil = angka1_2032
hasil -= angka2_2032
print("\nOperator assignment pengurangan (-=)")
print("hasil =", hasil)

# assignment perkalian
hasil = angka1_2032
hasil *= angka2_2032
print("\nAssignment perkalian (*=)")
print("hasil =", hasil)

# assignment pembagian, pembagian bulat, pembagian sisa
if angka2_2032 != 0:
    hasil = angka1_2032
    hasil /= angka2_2032
    print("\nOperator assignment pembagian (/=)")
    print("hasil =", hasil) 
    # operator tambahan
    hasil = angka1_2032
    hasil //= angka2_2032
    print("\nOperator assignment pembagian bulat (//=)")
    print("hasil =", hasil)
    hasil = angka1_2032
    hasil %= angka2_2032
    print("\nOperator assignment pembagian sisa (%=)")
    print("hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("angka kedua tidak boleh bernilai 0.")

# operator tambahan: assignment perpangkatan
hasil = angka1_2032
hasil **= angka2_2032
print("\nAssignment perpangkatan (**=)")
print("hasil =", hasil)