def slice(key,si,ei):
    first_part = key[:si]
    second_part = key[ei:]
    new_pass = first_part + second_part
    print(new_pass)
    return new_pass


def flip(key,si,ei,dir):
    first_part = key[:si]
    second_part = key[ei:]
    if dir == "Upper":
        flipping = key[si:ei]
        flipping = flipping.upper()
    elif dir == "Lower":
        flipping = key[si:ei]
        flipping = flipping.lower()
    result = first_part + flipping + second_part
    print(result)
    return result


def substr(key,subst):
    if subst in key:
        print(f"{key} contains {subst}")
    else:
        print("Substring not found!")
    return key



raw_key = input()

command = input()

while not command == "Generate":
    command = command.split(">>>")

    if command[0] == "Contains":
        substring = command[1]
        raw_key = substr(raw_key, substring)
    elif command[0]== "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        direction = command[1]
        raw_key = flip(raw_key,start_index, end_index, direction)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_key = slice(raw_key, start_index, end_index)

    command = input()

print(f"Your activation key is: {raw_key}")