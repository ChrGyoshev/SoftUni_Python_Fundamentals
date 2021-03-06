import re
pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+\.?\d+?)!(?P<quantity>\d+)"
command = input()
names = []
total_money = 0
while not command =="Purchase":
    match = re.match(pattern, command)
    if match:
        data = match.groupdict()
        names.append(data["name"])
        total_money += float(data["price"]) * int(data["quantity"])
    command = input()
print("Bought furniture:")
for el in names:
    print(el)
print(f'Total money spend: {total_money:.2f}')
