import math

num_of_students = int(input())
num_of_lectures = int(input())
additional_bonus = int(input())
max_student = {"bonus": 0, "attendance": 0}
for students in range (num_of_students):
    student_attendance = int(input())
    total_bonus = (student_attendance) / (num_of_lectures) * (5 +(additional_bonus))
    total_bonus = math.ceil(total_bonus)
    if total_bonus >= max_student["bonus"]:
        max_student["bonus"], max_student["attendance"] = total_bonus, student_attendance
print(f"Max Bonus: {max_student['bonus']}.")
print(f"The student has attended {max_student['attendance']} lectures.")