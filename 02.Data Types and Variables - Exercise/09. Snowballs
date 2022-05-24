num_snowballs = int(input())
value = 0

for i in range (num_snowballs):
    snowball_weight = int(input())
    time_to_target = int(input())
    quality = int(input())

    formula = (snowball_weight // time_to_target) ** quality

    if formula > value:
        value = formula
        result = f"{snowball_weight} : {time_to_target} = {formula} ({quality})"
print(result)
