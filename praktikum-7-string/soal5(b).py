# Bagian B: NIM
nim = input("NIM: ")
if len(nim) == 10 and nim.isdigit():
    print(f"Valid, intake year 20{nim[:2]}")
else:
    print("Invalid NIM")