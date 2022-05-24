def loading_bar(numb):
    final_print = ''
    result = ["."] * 10
    num = 0
    num_1 = 0
    for n in range(1,numb +1):
        if n % 10 ==0:
            num = n
    num_1 = num // 10
    for n in range(num_1):
        result[n] = "%"

    for r in result:
        final_print += r

    if num < 100:
        final_print = str(num) + "% " + "[" + final_print + "]"
        print(final_print)
        print('Still loading...')
    else:
        final_print = "[" + final_print + "]"
        print("100% Complete!")
        print(final_print)
        
number = int(input())

loading_bar(number)
