# buat file dengan nama multi_if2_nim.py
# buat program untuk kondisional if
# nama variabel ditambah 4 digit nim terakhir contoh: ipk_2032
# program ini menggunakan fungsi input()
# program menghitung diskon belanja

# input dari user
total_belanja_2032 = float(input("masukkan total belanja (Rp): "))

# input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2032 = input("apakah anda member? (y/t): ").strip().lower()
is_member_2032 = input_member_2032 in ["y", "ya"]

# input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2032 = input("apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2032 = input_promo_2032 in ["y", "ya"]

total_diskon_persen_2032 = 0

# multi-if terpisah: setiap kondisi diperiksa secara independen
# diskon bisa ditumpuk (akumulasi) hika memenuhi beberapa syarat sekaligus

if total_belanja_2032 > 1000000:
    total_diskon_persen_2032 += 10 # diskon belanja besar

if is_member_2032:
    total_diskon_persen_2032 += 5 # diskon member

if kode_promo_valid_2032:
    total_diskon_persen_2032 += 15 # diskon voucher

# menghitung nominal diskon dan total bayar
nominal_diskon_2032 = total_belanja_2032 * (total_diskon_persen_2032 / 100)
total_bayar_2032 = total_belanja_2032 - nominal_diskon_2032

# output hasil
print("\n--- rincian pembayaran ---")
print(f"total diskon : {total_diskon_persen_2032}% (Rp {nominal_diskon_2032:,.0f})")
print(f"total bayar  : Rp {total_bayar_2032:,.0f}")

print(f"total diskon yang anda dapatkan: {total_diskon_persen_2032}%")
# output: total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid