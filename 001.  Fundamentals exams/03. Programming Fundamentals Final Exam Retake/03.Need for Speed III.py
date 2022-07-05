def drive(dict,car,dist,fuel):
    if dict[car]["fuel"] - fuel >= 0:
        dict[car]['fuel'] -= fuel
        dict[car]['milage'] += dist
        print(f"{car} driven for {dist} kilometers. {fuel} liters of fuel consumed.")
        if dict[car]['milage'] >= 100000:
            print(f"Time to sell the {car}!")
            del dict[car]
    else:
        print("Not enough fuel to make that ride")
    return dict

    a=123

def refuel(dict,car,fuel):
    if dict[car]["fuel"] + fuel > 75:
        print(f"{car} refueled with {75 - dict[car]['fuel']} liters")
        dict[car]['fuel'] = 75

    else:
        dict[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")
    return dict

def revert(dict,car, kilometers):
    dict[car]['milage'] -= kilometers
    if dict[car]['milage'] < 10000:
        dict[car]['milage']= 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return dict


num_of_cars = int(input())
garage = {}
for cars in range (0, num_of_cars):
    command = input().split("|")
    if command[0] not in garage.keys():
        garage[command[0]] = {"milage": None, "fuel": None}
    garage[command[0]]["milage"], garage[command[0]]["fuel"] = int(command[1]), int(command[2])
curr_command = input()

while not curr_command == "Stop":
    curr_command= curr_command.split(" : ")
    if curr_command[0] == "Drive":
        garage = drive(garage,curr_command[1], int(curr_command[2]), int(curr_command[3]))
    elif curr_command[0]== "Refuel":
        garage = refuel(garage,curr_command[1],int(curr_command[2]))
    elif curr_command[0] == "Revert":
        garage = revert(garage,curr_command[1], int(curr_command[2]))

    curr_command = input()

for key,value in garage.items():
    print(f"{key} -> Mileage: {value['milage']} kms, Fuel in the tank: {value['fuel']} lt.")