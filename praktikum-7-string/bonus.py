sentence = "ibu ratna antar ubi"

# Menghilangkan spasi dan mengubah ke huruf kecil
processed = sentence.replace(" ", "").lower()

# Memeriksa apakah sama dengan kebalikannya
if processed == processed[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")