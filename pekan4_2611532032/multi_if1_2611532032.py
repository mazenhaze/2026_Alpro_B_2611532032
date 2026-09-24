# buat file dengan nama multi_if1_nim.py
# buat program untuk kondisional if
# nama variabel ditambah 4 digit nim terakhir contoh: ipk_2032
# program ini menggunakan fungsi input ()

umur_2032 = int(input("input umur anda: "))
sim_2032 = input("apakah anda sudah punya sim c (y/t): ")[0]

if umur_2032 >= 17 and sim_2032 == 'y':
    print("anda sudah dewasa dan boleh bawa motor")

if umur_2032 >= 17 and sim_2032 != 'y':
    print("anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_2032 < 17 and sim_2032 == 'y':
    print("anda belum cukup umur punya sim")

if umur_2032 < 17 and sim_2032 != 'y':
    print("anda belum cukup umur bawa motor")
