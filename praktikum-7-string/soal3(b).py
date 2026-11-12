text = "Muhammad Abdurrauf"
count = 0
for char in text.lower():  # Ubah ke huruf kecil agar vokal kapital ikut terhitung
    if char in "aiueo":
        count += 1         # Perbaikan dari count = 1 menjadi akumulasi (+= 1)
print("Vowels:", count)