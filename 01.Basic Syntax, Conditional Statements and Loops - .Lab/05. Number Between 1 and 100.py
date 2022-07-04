num = float(input())
num_true = False

while not num_true:
    if num >= 1 and num <= 100:
        num_true = True
        print(f'The number {num} is between 1 and 100')
        break

    num = float(input())

