def add_stop(spots, index, string):
    if index in range(len(spots)):
        spots = spots[:index] + string + spots[index:]
    print(spots)
    return spots

def remove(spots,start,end):
    if start in range(len(spots)) and end in range(len(spots)):
        spots = spots[:start] + spots[end+1:]
    print(spots)
    return spots

def switch(spots, old, new):
    if old in spots:
        spots = spots.replace(old, new)
    print(spots)
    return spots


travel_stops = input()
command = input()

while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        travel_stops = add_stop(travel_stops,int(command[1]),command[2])
    elif command[0] == "Remove Stop":
        travel_stops = remove(travel_stops, int(command[1]), int(command[2]))
    elif command[0] == "Switch":
        travel_stops = switch(travel_stops,command[1],command[2])
    command = input()
if command == "Travel":
    print(f"Ready for world tour! Planned stops: {travel_stops}")
