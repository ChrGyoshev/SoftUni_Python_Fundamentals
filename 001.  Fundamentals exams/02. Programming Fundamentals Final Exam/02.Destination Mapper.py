num = int(input())
plants_dict = {}
plants_ratings = {}
for i in range(num):
    command = input().split("<->")
    plants_dict[command[0]] = int(command[1])
    if command[0] not in plants_ratings:
        plants_ratings[command[0]] = []
command = input()
while not command == "Exhibition":
    current_command = command.split(": ")
    if current_command[0] == "Rate":
        plant, rating = current_command[1].split(" - ")
        rating = int(rating)
        if plant not in plants_dict:
            print("error")
        else:
            if plant not in plants_ratings:
                plants_ratings[plant] = []
            plants_ratings[plant].append(rating)
    elif current_command[0] == "Update":
        plant, rarity = current_command[1].split(" - ")
        rarity = int(rarity)
        if plant not in plants_dict:
            print("error")

        else:
            plants_dict[plant] = rarity
    elif current_command[0] == "Reset":
        plant = current_command[1]
        if plant not in plants_dict:
            print("error")

        else:
            plants_ratings[plant] = []
    command = input()

if command == "Exhibition":
    print('Plants for the exhibition:')
    for k, v in plants_dict.items():
        if not plants_ratings[k]:
            avg = 0
        else:
            avg = sum(plants_ratings[k]) / len(plants_ratings[k])
        print(f'- {k}; Rarity: {v}; Rating: {avg:.2f}')


