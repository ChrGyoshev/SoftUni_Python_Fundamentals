import re
text = input()
pattern = r"(?<=(=|/))[A-Z]([a-zA-Z]){2,}(?=\1)"
travel_points = 0
validator = [object.group()for object in re.finditer(pattern,text)]

for elements in validator:
    travel_points += len(elements)
if validator:
    print(f"Destinations: {', '.join(validator)}")
else:
    print("Destinations:")
print(f"Travel Points: {travel_points}")
