def swap(dict,i_one,i_two):
    dict[i_one],dict[i_two] = dict[i_two], dict[i_one]
    return dict

def multiply(dict,i_one,i_two):
    dict[i_one] *= dict[i_two]
    return dict

def decrease(dict):
    dict=[el-1for el in dict]
    return dict

array = list(map(int, input().split()))
command = input()

while command != "end":
    command = command.split()
    if command[0] == "swap":
        array= swap(array,int(command[1]),int(command[2]))
    elif command[0] == "multiply":
        array = multiply(array,int(command[1]), int(command[2]))
    elif command[0] == "decrease":
        array = decrease(array)
    command = input()
print(*array,sep=", ")