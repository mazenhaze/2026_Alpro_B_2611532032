phone = "081234567890"

# Algoritma dinamis untuk berbagai panjang nomor:
num_hidden = len(phone) - 7  # 4 digit depan + 3 digit belakang = 7 digit yang terlihat
masked = phone[:4] + "*" * num_hidden + phone[-3:]
print(masked)