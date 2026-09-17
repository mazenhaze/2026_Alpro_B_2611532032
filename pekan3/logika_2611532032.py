# buat file dengan nama logika_2611532032.py
# nama variabel ditambah 4 digit terakhir NIM contoh: a_2611532032
# program ini menggunakan fungsi input ()
# program ini menggunakan operator logika dalam python

# memasukkan nilai boolean
# input tidak peka terhadap huruf besar dan kecil
a1_2032 = input("input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_2032 = input("input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1_2032)
print("A2 =", a2_2032)

# konjungsi: bernilai True jika kedua operand bernilai True
hasil = a1_2032 and a2_2032
print("\nOperator konjungsi (and)")
print("A1 and A2 =", hasil)

# disjungsi: bernilai True jika minimal satu operand bernilai True
hasil = a1_2032 or a2_2032
print("\nOperator disjungsi (or)")
print("A1 or A2 =", hasil)

# negasi A1: membalik nilai A1
hasil = not a1_2032
print("\nOperator negasi A1 (not)")
print("not A1 =", hasil)

# negasi A2: membalik nilai A2
hasil = not a2_2032
print("\nOperator negasi A2 (not)")
print("not A2 =", hasil)

# XOR: bernilai true jika kedua nilai berbeda
hasil = a1_2032 != a2_2032
print("\nDisjungsi eksklusif (XOR)")
print("A1 XOR A2 =", hasil)