# buat file dengan nama lainnya_2611532032.py
# nama variabel ditambah 4 digit terakhir NIM contoh: a_261153203
# program ini menggunakan fungsi input ()
# program operator keanggotan dan identitas dalam python

print("==================================")
print("Operator Keanggotan")
print("==================================")

# input beberapa data yang dipisahkan dengan koma
data_2032 = input("masukkan beberapa angka, pisahkan dengan koma: ")

# mengubah input menjadi list integer
data_2032 = [int(angka.strip()) for angka in data_2032.split(",")]

nilai_dicari_2032 = int(input("masukkan nilai yang dicari: "))

# operator in
hasil = nilai_dicari_2032 in data_2032
print("\nOperator keanggotan (in)")
print(nilai_dicari_2032, "in data =", hasil)

# operator not in
hasil = nilai_dicari_2032 not in data_2032
print("\nOperator keanggotan (not in)")
print(nilai_dicari_2032, "not in data =", hasil)


print("\n==================================")
print("2. Operator Identitas")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_2032 = data_2032

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2032 = objek1_2032

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2032 = data_2032.copy()

print("\nobjek1 =", objek1_2032)
print("objek2 =", objek2_2032)
print("objek3 =", objek3_2032)

# operator is
hasil = objek1_2032 is objek2_2032
print("\nOperator identitas (is)")
print("objek1 is objek2 =", hasil)

# operator is not
hasil = objek1_2032 is not objek3_2032
print("\nOperator identitas (is not)")
print("objek1 is not objek3 =", hasil)  

# membandingkan identitas dan nilai
print("\nMembandingkan Identitas dan Nilai")
print("objek1 is objek2 (identitas):", objek1_2032 is objek2_2032)
print("objek1 == objek2 (nilai):", objek1_2032 == objek2_2032)
print("objek1 is objek3 (identitas):", objek1_2032 is objek3_2032)
print("objek1 == objek3 (nilai):", objek1_2032 == objek3_2032)