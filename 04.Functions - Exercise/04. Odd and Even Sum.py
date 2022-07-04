def even_odd(number):
    even =0
    odd=0
    for num in number:
        if int(num) % 2 == 0:
            even+= int(num)
        else:
            odd += int(num)
    result = (f"Odd sum = {odd}, Even sum = {even}")
    return result


num = input()

print(even_odd(num))
