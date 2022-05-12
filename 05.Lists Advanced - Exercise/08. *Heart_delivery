neibourhood_size = list(map(int, input().split("@")))
command = input()
length = 0


def result(command):
    result = [el for el in command if el != 0]
    result = len(result)
    if result > 0:
        print(f"Cupid has failed {result} places.")
    else:
        print("Mission was successful.")
    return result


while not command == "Love!":
    command = command.split()
    length += int(command[1])
    if length >= len(neibourhood_size):
        length = 0
    if 0 <= length <= len(neibourhood_size):
        if neibourhood_size[length] == 0:
            print(f"Place {length} already had Valentine's day.")
            command = input()
            continue
    neibourhood_size[length] -= 2

    if neibourhood_size[length] <= 0:
        print(f"Place {length} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {length}.")
result(neibourhood_size)
