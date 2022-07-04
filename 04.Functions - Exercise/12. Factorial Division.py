#fact_num
def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

num_1 = int(input())
num_2 = int(input())
fact_num_one = fact(num_1)
fact_num_two = fact(num_2)
result = fact_num_one / fact_num_two

print(f'{result:.2f}')
