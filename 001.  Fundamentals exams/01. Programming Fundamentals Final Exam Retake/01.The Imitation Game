import re
text = input()
pattern = r"(#|\|)(?P<name>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1"
total_calories = 0
validated =[obj.groupdict()for obj in re.finditer(pattern, text)]
for match in validated:
    if 0< int(match["calories"]) <= 10000:
        total_calories +=int(match["calories"])
total_calories = total_calories//2000
print(f"You have food to last you for: {total_calories} days!")
for matches in validated:
    if 0 < int(matches["calories"]) <= 10000:
        print(f"Item: {matches['name']}, Best before: {matches['date']}, Nutrition: {matches['calories']}")


