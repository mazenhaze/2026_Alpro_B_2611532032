n = int(input())

data = {}
urutan = []

for _ in range(n):
    nama, nominal = input().split()
    nominal = int(nominal)

    if nama not in data:
        data[nama] = 0
        urutan.append(nama)

    data[nama] += nominal

for nama in urutan:
    print(f"{nama}: {data[nama]}")

total_cash = sum(data.values())
print(f"Total cash: {total_cash}")

top_nama = urutan[0]
for nama in urutan:
    if data[nama] > data[top_nama]:
        top_nama = nama

print(f"Top contributor: {top_nama} ({data[top_nama]})")