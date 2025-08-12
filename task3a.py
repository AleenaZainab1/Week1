import json

# Student records as Python list of dicts
students = [
    {"name": "Ali", "age": 20, "grade": "A"},
    {"name": "Sara", "age": 19, "grade": "B"},
    {"name": "Ahmed", "age": 21, "grade": "A+"}
]

# 1) Save to JSON file
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)  # indent se file readable hoti hai

# 2) Reload from JSON file
with open("students.json", "r") as f:
    loaded_students = json.load(f)

# 3) Print to screen
print("Student Records:")
for student in loaded_students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
