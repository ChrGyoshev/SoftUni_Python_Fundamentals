string = input().split("|")
coins = 100
energy = 100
REST_ENG = 50
MAX_ENG = 100
ORDER_ENG = 30
is_not_bankrupt = True
for i in string:
    single_event_list = i.split("-")
    event = single_event_list[0]
    number = int(single_event_list[1])
    if event == "rest":
        gained_energy = 0
        if energy + number > MAX_ENG:
            gained_energy = MAX_ENG - energy
            energy = MAX_ENG
        else:
            energy += number
            gained_energy = number
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= ORDER_ENG:
            energy -= ORDER_ENG
            coins += number
            print(f"You earned {number} coins.")

        else:
            energy += REST_ENG
            print("You had to rest!")
            continue
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            is_not_bankrupt = False
            break

if is_not_bankrupt:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
