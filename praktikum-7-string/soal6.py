full_name = "  Muhammad Abdurrauf  "
nim = "2611532032"

clean_name = full_name.strip()
space_idx = clean_name.find(" ")

if space_idx == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space_idx]

username = first_name.lower() + nim[-3:]
print(username)