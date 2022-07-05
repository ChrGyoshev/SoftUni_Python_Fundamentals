def fire(ship, index, damage):
    if index in range(len(ship)):
        ship[index] -= damage
        if ship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            quit()

    return ship



def defend(ship, start, end, damage):
    if start in range(len(ship)) and end in range(len(ship)):
        for el in range(start,end+1):
            ship[el] -= damage
            if ship[el]<=0:
                print("You lost! The pirate ship has sunken.")
                quit()
    return ship



def repair(ship, index, health):
    if index in range(len(ship)):
        if ship[index] + health >= max_health:
            ship[index] = max_health
        else:
            ship[index] += health

    return ship

def status(ship,max_health):
    repair_soon = max_health * 0.2
    damn = 0
    for el in ship:
        if el < repair_soon:
            damn+=1

    if damn >0:
        print(f"{damn} sections need repair.")
    return ship




pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
max_health = int(input())
command = input()

while not command == "Retire":
    command = command.split()
    if command[0] == "Fire":
        war_ship = fire(war_ship, int(command[1]), int(command[2]))
    elif command[0] == "Defend":
        pirate_ship = defend(pirate_ship, int(command[1]), int(command[2]), int(command[3]))
    elif command[0] == "Repair":
        pirate_ship = repair(pirate_ship, int(command[1]), int(command[2]))
    elif command[0] == "Status":
        pirate_ship = status(pirate_ship,max_health)

    command = input()
print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(war_ship)}")