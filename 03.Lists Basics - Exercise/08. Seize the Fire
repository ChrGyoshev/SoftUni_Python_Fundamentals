fire = input().split("#")
water = int(input())

RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)
effort = 0
total_fire = 0
final_fire = []
for f in fire:
    current_fire, value = f.split(" = ")
    value= int(value)
    if current_fire == "High" and value  not in RANGE_HIGH:
        continue
    elif current_fire == "Medium" and value  not in RANGE_MEDIUM:
        continue
    elif current_fire == "Low" and value  not in RANGE_LOW:
        continue
    if water >= value:
        water -= value
        effort += value * 0.25
        total_fire += value
        final_fire.append(value)

print("Cells:")
for i in final_fire:
    print(f" - {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
