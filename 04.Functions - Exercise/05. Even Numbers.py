numbers = input().split()


def even_num(digit):
    list= []
    new_list = [list.append((int(num))) for num in digit if int(num) % 2 == 0]
    print(list)
    return list
    
    
even_num(numbers)
