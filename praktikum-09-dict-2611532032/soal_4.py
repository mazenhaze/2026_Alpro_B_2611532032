n = int(input("masukkan jumlah perulangan: "))
kas ={}

for i in range (n):
    nama, nominal = input().split()
    kas[nama] = kas.get(nama, 0) + int(nominal)

donatur = ""
terbesar = 0

for name, total in kas.items():
    print(f"{nama}: {total}")
    if total > terbesar:
        terbesar = total
        donatur = nama
print("total cash: ", total)
print("top contributor: ", donatur)
