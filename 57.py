courses = {
    "riazi1": 14,
    "zaban": 20,
    "mabani computer": 20,
    "madar manteghi": 16,
    "andishe eslami": 7,
    "assembly": 10
}

for k, v in courses.items():
    if v >= 10:
        print(k, "Passed")
    else:
        print(k, "Failed")

avg = sum(courses.values()) / len(courses)
print(avg)
