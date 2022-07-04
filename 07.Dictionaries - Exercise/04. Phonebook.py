command = input()
phonebook = {}
while len(command) >1:
    name, number = command.split("-")
    if name not in phonebook:
        phonebook[name] = number
    else:
        phonebook.pop(name)
        phonebook[name] = number





    command = input()


for i in range (int(command)):
    name = input()
    if name not in phonebook:
        print(f"Contact {name} does not exist.")
    else:
        for key, value in phonebook.items():
            if key == name:
                print(f"{key} -> {value}")
