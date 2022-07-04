num_of_lines = int(input())
WATER_TANK_CAPACITY = 255
total_sum = 0
for i in range (num_of_lines):
    liters = int(input())
    if total_sum + liters <= WATER_TANK_CAPACITY:
        total_sum += liters
    else:
        print("Insufficient capacity!" )
print(total_sum)
