# program untuk menampilkan segitiga

tinggi_2032 = int(input("masukkan tinggi segitiga: "))

for i_2032 in range(1, tinggi_2032 + 1):
    
    print(" " * (tinggi_2032 - i_2032), end="")

    for j_2032 in range(i_2032):
        print("♡", end=" ")

    print()  