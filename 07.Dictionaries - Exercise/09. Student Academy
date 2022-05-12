num = int(input())
students_database = {}

for _ in range (num):
    name = input()
    grade = float(input())
    if name not in students_database:
        students_database[name] = []
    students_database[name].append(grade)

filtered_grades = {}

for name, grades in students_database.items():
    avarage_grade = sum(grades) / len(grades)
    if avarage_grade >= 4.50:
        filtered_grades[name] = avarage_grade

for name, grade in filtered_grades.items():
    print(f"{name} -> {grade:.2f}")
