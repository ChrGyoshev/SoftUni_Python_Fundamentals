def potion(health, number):
    if number + health > 100:
        healed = 100 - health
        health = 100
    else:
        healed = number
        health += number
    print(f"You healed for {healed} hp.")
    print(f'Current health: {health} hp.')
    return health



dungeon_rooms = input().split("|")
health = 100
bitcoins = 0
room = 0
is_dead = False
for dungeon in dungeon_rooms:
    room +=1
    current_command, num = dungeon.split()
    num = int(num)
    if current_command == "potion":
        health = potion(health, num)
    elif current_command == "chest":
        bitcoins += num
        print(f"You found {num} bitcoins.")
    else:
        health -= num
        if health >0:
            print(f"You slayed {current_command}.")
        else:
            print(f"You died! Killed by {current_command}.")
            print(f"Best room: {room}")
            is_dead = True
            break
if is_dead==False:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}\n"
      f"Health: {health}")