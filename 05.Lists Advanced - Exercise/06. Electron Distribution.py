num_of_electrons = int(input())
shell = 0
list = []
while num_of_electrons > 0:
    shell += 1
    factor = 2 * shell ** 2
    if num_of_electrons < factor:
        list.append(num_of_electrons)
    else:

        list.append(factor)
    num_of_electrons -= factor
print(list)
