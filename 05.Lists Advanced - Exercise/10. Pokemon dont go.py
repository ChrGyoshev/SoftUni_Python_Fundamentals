def in_range(numbers,popped):
    for el in range(len(numbers)):
        if numbers[el] <= popped:
            numbers[el] += popped
        else:
            numbers[el] -= popped
    return numbers


numbers = list(map(int, input().split()))
summing = 0
while len(numbers) >0:
    indexes = int(input())
    if 0 <= indexes < len(numbers):
        popped = numbers.pop(indexes)
        summing += popped
        numbers = in_range(numbers,popped)
    else:
        if indexes < 0:
            removed_item = numbers.pop(0)
            element = numbers[-1]
            numbers.insert(0, element)
            summing += removed_item
            numbers = in_range(numbers,removed_item)
        elif indexes >=len(numbers):
            removed_item = numbers.pop(-1)
            first_item = numbers[0]
            numbers.append(first_item)
            summing += removed_item
            numbers = in_range(numbers,removed_item)
print(summing)






