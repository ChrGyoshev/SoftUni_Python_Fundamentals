command = input()

while not command == "End":
    new = ''
    if command == "SoftUni":
        command = input()
        continue
    else:
        for i in command:
            new += i + i
        print(new)
    command = input()
