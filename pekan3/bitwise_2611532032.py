# buat file dengan nama bitwisew_2611532032.py
# nama variabel ditambah 4 digit terakhir NIM contoh: a_261153203
# program ini menggunakan fungsi input ()

print("\n=====================================")
print("Operator Bitwise")
print("=====================================")

angka1_2032 = int(input("input angka-1: "))
angka2_2032 = int(input("input angka-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1, "| biner =", bin(angka1))
print("angka2 =", angka2, "| biner =", bin(angka2))

# bitwise AND
hasil = angka1_2032 & angka2_2032
print("\nBitwise AND (&)")
print(angka1, "&", angka2, "=", hasil)
print("biner hasil =", bin(hasil))
print("biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise OR
hasil = angka1_2032 % angka2_2032
print("\nBitwise OR (|)")
print(angka1_2032, "|", angka2_2032, "=", hasil)
print ("biner hasil =", bin(hasil))
print("biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise XOR
hasil = angka1_2032 ^ angka2_2032
print("\nBitwise XOR (^)")
print(angka1_2032, "^", angka2_2032, "=", hasil)
print("biner hasil =", bin(hasil))
print("biner hasil (8bit) =", format(hasil, "08b"))

# Bitwise NOT   
hasil = ~angka1_2032
print("\nBitwise NOT (~)")
print("~", angka1_2032, "=", hasil)
print("biner hasil =", bin(hasil))
print("biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_2032 << jumlah_geser
print ("\nBitwise geser kiri (<<)")
print(angka1_2032, "<<", jumlah_geser, "=", hasil)
print("biner hasil =", bin(hasil))
print("biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kanan
hasil = angka1_2032 >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1_2032, ">>", jumlah_geser, "=", hasil)
print("biner hasil =", bin(hasil))
print("biner hasil (8 bit) =", format(hasil, "08b"))
