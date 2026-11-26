schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

# 6a. Hari dengan mata kuliah terbanyak dan jumlahnya
busiest_day = max(schedule, key=lambda day: len(schedule[day]))
max_courses = len(schedule[busiest_day])
print(f"Busiest day: {busiest_day} ({max_courses} courses)")

# 6b. Input nama mata kuliah dan hitung jumlah hari munculnya
course = input("Masukkan nama mata kuliah: ").strip()
day_count = sum(1 for courses in schedule.values() if course in courses)
print(f"{course}: {day_count} days")