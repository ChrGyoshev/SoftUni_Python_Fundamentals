first_num = int(input())
second_num = int(input())
third_num = int(input())


def smallest_num(a,b,c):
    if a < b and a < c:
        return a
    elif b < c and b < a:
        return b
    else:
        return c

result = smallest_num(first_num,second_num,third_num)
print(result)
