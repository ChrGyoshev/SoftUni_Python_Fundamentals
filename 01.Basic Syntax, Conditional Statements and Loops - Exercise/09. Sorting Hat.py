command = input()

while not command =="Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        quit()
    else:
        name = len(command)
        if name < 5:
            print(f"{command} goes to Gryffindor.")
        elif name == 5:
            print(f"{command} goes to Slytherin.")
        elif name == 6:
            print(f"{command} goes to Ravenclaw.")
        elif name > 6:
            print(f"{command} goes to Hufflepuff.")


    command = input()
print("Welcome to Hogwarts.")
