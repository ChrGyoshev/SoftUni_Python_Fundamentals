command = input()
register = {}
while not command == "end":
    course_name, student_name = command.split(" : ")

    if course_name not in register:
        register[course_name] = []
    register[course_name].append(student_name)

    command = input()

for key, value in register.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")
