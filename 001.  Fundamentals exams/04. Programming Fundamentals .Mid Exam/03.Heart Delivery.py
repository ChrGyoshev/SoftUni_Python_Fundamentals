neighborhood = list(map(int, input().split("@")))
command = input()
current_jump = 0

while not command == "Love!":
    command = command.split()
    current_jump += int(command[1])
    if current_jump >= len(neighborhood):
        current_jump = 0
    if current_jump in range(len(neighborhood)):
        if neighborhood[current_jump]==0:
            print(f"Place {current_jump} already had Valentine's day.")
            command = input()
            continue
    neighborhood[current_jump] -= 2

    if neighborhood[current_jump]<=0:
        print(f"Place {current_jump} has Valentine's day.")

    command = input()
failed_places = [+1 for el in neighborhood if el>0]
print(f"Cupid's last position was {current_jump}.")
if sum(neighborhood)==0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(failed_places)} places.")

