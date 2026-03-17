students = [
    {"name": "Alice",   "subject": "Math",    "scores": [88, 92, 95, 90]},
    {"name": "Bob",     "subject": "Science", "scores": [72, 68, 75, 80]},
    {"name": "Carol",   "subject": "Math",    "scores": [95, 98, 92, 97]},
    {"name": "David",   "subject": "History", "scores": [60, 65, 70, 58]},
    {"name": "Eva",     "subject": "Science", "scores": [83, 87, 80, 90]},
]


def calculate_average(scores):
    return sum(scores) / len(scores)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def class_topper(students):
    return max(students, key=lambda s: calculate_average(s["scores"]))


topper = class_topper(students)
sorted_students = sorted(students, key=lambda s: calculate_average(s["scores"]), reverse=True)

print(f"{'Name':<10} {'Subject':<10} {'Average':>7}  {'Grade':>5}")
print("-" * 40)
for student in sorted_students:
    avg = calculate_average(student["scores"])
    grade = get_grade(avg)
    tag = "  *** TOP ***" if student is topper else ""
    print(f"{student['name']:<10} {student['subject']:<10} {avg:>7.2f}  {grade:>5}{tag}")
