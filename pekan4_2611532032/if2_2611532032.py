# buat file dengan nama if2_nim.py
# buat program untuk kondisional if
# nama variabel ditambah 4 digit nim terakhir contoh: ipk_2032
# program ini menggunakan input()

ipk_2032 = float(input("input ipk anda"))

if ipk_2032 > 2.75:
    print("anda lulus dengan sangat memuaskan dengan ipk " + str(ipk_2032))
else:
    print("anda tidak lulus")
print("program selesai")
