cards = input().split()
set_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
set_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

team_a_counter = 11
team_b_counter = 11

for card in cards:
    if team_a_counter < 7 or team_b_counter < 7:
        break
    tokens = card.split('-')
    team = tokens[0]
    number = int(tokens[1])

    if team == "A":
        if number in set_a:
            set_a.remove(number)
            team_a_counter -= 1
    elif team =="B":
        if number in set_b:
            set_b.remove(number)
            team_b_counter -=1

print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")
if team_b_counter < 7 or team_a_counter < 7:
    print(f"Game was terminated")
