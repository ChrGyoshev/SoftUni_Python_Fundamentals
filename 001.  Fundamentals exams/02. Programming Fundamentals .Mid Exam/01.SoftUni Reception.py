efficency_1 = int(input())
efficency_2 = int(input())
efficency_3 = int(input())
students = int(input())
total_efficiency = efficency_2 + efficency_3 + efficency_1
hours = 0
while students >0:
    hours+=1
    if hours % 4 == 0:
        continue
    students -= total_efficiency
print(f"Time needed: {hours}h.")