def change_key(command, library):
    piece_to_work = command[1]
    new_key = command[2]
    if piece_to_work not in library:
        print(f"Invalid operation! {piece_to_work} does not exist in the collection.")
    else:
        library[piece_to_work]["key"] = new_key
        print(f"Changed the key of {piece_to_work} to {new_key}!")
    return library

def remove(command, library):
    piece_to_remove = command[1]
    if piece_to_remove not in library:
        print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")
    else:
        del library[piece_to_remove]
        print(f"Successfully removed {piece_to_remove}!")
    return library

def add(command, library):
    piece = command[1]
    composer = command[2]
    key = command[3]
    if piece not in library:
        library[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")
    return library

number_of_pieces = int(input())
library = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    library[piece] = {"composer": composer, "key": key}

commands = input()

while not commands == "Stop":
    commands = commands.split("|")
    if commands[0]== "Add":
        library = add(commands,library)
    elif commands[0]== "Remove":
        library = remove(commands, library)
    elif commands[0] == "ChangeKey":
        library = change_key(commands, library)

    commands = input()

for key,value in library.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")