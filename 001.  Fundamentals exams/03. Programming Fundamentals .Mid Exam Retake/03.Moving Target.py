def shoot(i, power, tar):
    i = int(i)
    power = int(power)
    if i in range(len(tar)):
        tar[i] -= power
        if tar[i] <= 0:
            tar.pop(i)

    return tar


def add(i, v, tar):
    i = int(i)
    v = int(v)
    if i in range(len(tar)):
        tar.insert(i, v)
    else:
        print("Invalid placement!")

    return tar


def strike(i, radius, tar):
    failed = True
    i = int(i)
    radius = int(radius)
    if i in range(len(tar)):
        if i - radius >= 0 and i + radius <= len(tar):
            failed = False
            left_part = tar[:i - radius]
            right_part = tar[i + radius + 1:]
            tar = left_part + right_part
    if failed:
        print("Strike missed!")
    return tar


targets = list(map(int, input().split()))
command = input()
while not command == "End":
    command = command.split()
    if command[0] == "Shoot":
        targets = shoot(command[1], command[2], targets)
    elif command[0] == "Add":
        targets = add(command[1], command[2], targets)
    elif command[0] == "Strike":
        targets = strike(command[1], command[2], targets)
    command = input()
print(f'{"|".join([str(el) for el in targets])}')