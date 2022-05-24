targets = list(map(int, input().split()))

command = input()


def shoot(nums, i, v):
    if 0 <= i < len(nums):
        nums[i] -= v
        if nums[i] <=0:
            nums.pop(i)
    return nums

def strike(nums, i, v):
    left_part = i - v
    right_part = i + v
    if left_part >= 0 and right_part < len(nums):
        left_part = nums [:left_part]
        right_part = nums[right_part + 1:]
        nums = left_part + right_part
    else:
        print("Strike missed!")
    return nums

def add (nums, i, v):
    if 0 <= i < len(nums):
        nums.insert(i, v)
    else:
        print("Invalid placement!")
    return nums



while not command == "End":
    command, index, value = command.split()
    value= int(value)
    index = int(index)
    if command == "Shoot":
        targets = shoot(targets, index, value)
    elif command == "Strike":
        targets = strike(targets, index, value)
    elif command == "Add":
        targets = add(targets, index, value)

    command = input()

result = "|".join(str(el) for el in targets)
print(result)
