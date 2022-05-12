line = input().split()

looking_for = input().split()

dict = {}
for index in range(0, len(line), 2):
    key = line[index]
    value = int(line[index+1])
    dict[key]= value

for product in looking_for:
    if product in dict:
        print(f"We have {dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
