numbers = (list(map(int, input().split(", "))))
group = 0
while len(numbers) >= 1:
    group += 10
    curr = [num for num in numbers if num <= group]
    print(f"Group of {group}'s: " + str(curr))
    numbers = list(filter(lambda x: x > group, numbers))
