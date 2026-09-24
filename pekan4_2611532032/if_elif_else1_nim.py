# buat file dengan nama if_elif_else1_nim.py
# buat program untuk kondisional if
# nama variabel ditambah 4 digit nim terakhir contoh: ipk_2032
# program ini menggunakan fungsi input()

umur_2032 = int(input("input umur anda: "))
sim_2032 = input("apakah anda sudah punya sim c: ")[0]

if umur_2032 >= 17 and sim_2032 == 'y':
    print("anda sudah dewasa dan boleh bawa motor")
elif umur_2032 >= 17 and sim_2032 != 'y':
    print("anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2032 < 17 and sim_2032 == 'y':
    print("anda belum cukup umur punya sim")
else:
    print("anda belum cukup umur bawa motor")
print("program selesai")
