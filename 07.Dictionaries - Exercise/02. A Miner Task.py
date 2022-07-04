command = input()
dictonary = {}
while not command =="stop":
    product = command
    value = int(input())
    if product not in dictonary:
        dictonary[product]= value
    else:
        dictonary[product] += value
    command = input()

for key,value in dictonary.items():
    print(f'{key} -> {value}')
