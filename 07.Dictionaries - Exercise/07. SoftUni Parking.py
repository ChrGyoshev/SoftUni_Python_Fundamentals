number_of_commands = int(input())

parking_lot = {}
for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "register":
        name, plate = command[1:]
        if name not in parking_lot:
            parking_lot[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    else:
        name = command[1]
        if name not in parking_lot:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking_lot.pop(name)

for name,plate in parking_lot.items():
    print(f"{name} => {plate}")
