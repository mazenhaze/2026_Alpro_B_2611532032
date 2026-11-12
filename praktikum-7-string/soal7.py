name = "Muhammad Abdurrauf"
nim = "2611532032"

clean_name = name.strip()
space_idx = clean_name.find(" ")
first_name = clean_name if space_idx == -1 else clean_name[:space_idx]
username = first_name.lower() + nim[-3:]
intake_year = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake_year}")
print("=" * 30)