quantity = int(input())
days = int(input())
total_cost = 0
spirit = 0

for days_left in range (1, days + 1):
    if days_left % 11 == 0:
        quantity += 2
    if days_left % 2 == 0:
        total_cost += 2 * quantity
        spirit+= 5
    if days_left % 3 == 0:
        total_cost +=(5 * quantity) + (3 * quantity)
        spirit+= 13
    if days_left % 5 == 0:
        total_cost += quantity * 15
        spirit += 17
        if days_left % 3 == 0:
            spirit += 30
    if days_left % 10 == 0:
        spirit -= 20
        total_cost += 23

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
