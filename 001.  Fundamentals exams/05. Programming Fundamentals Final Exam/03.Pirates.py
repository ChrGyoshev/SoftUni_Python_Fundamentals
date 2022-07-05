#Functions
def prosper(database, town, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
        return database
    else:
        database[town]["goldy"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {database[town]['goldy']} gold.")
        return database

def plunder(database, town, people, gold):
    print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
    database[town]["goldy"] -= gold
    database[town]["pop"] -= people
    if database[town]['goldy'] == 0 or database[town]['pop'] == 0:
        del database[town]
        print(f"{town} has been wiped off the map!")
    return database







#Fill up the data:
command = input()
database = {}
while command != "Sail":
    city,population,gold = command.split("||")
    population = int(population)
    gold = int(gold)
    if city not in database:
        database[city] = {"goldy" : gold, "pop" : population}
    else:
        database[city]["goldy"] += gold
        database[city]["pop"] += population
    command = input()

# Process the data:

command_one = input()

while not command_one == "End":
    cur_command = command_one.split("=>")
    if cur_command[0] == "Plunder":
        town = cur_command[1]
        population = int(cur_command[2])
        gold = int(cur_command[3])
        database = plunder(database, town, population, gold)

    elif cur_command[0] == "Prosper":
        town = cur_command[1]
        gold = int(cur_command[2])
        database = prosper(database, town, gold)


    command_one = input()

if len(database) > 0:
    print(f"Ahoy, Captain! There are {len(database)} wealthy settlements to go to:")

    for key, value in database.items():
        print(f"{key} -> Population: {value['pop']} citizens, Gold: {value['goldy']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")