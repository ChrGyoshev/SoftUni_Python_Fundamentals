gifts = input().split()
command = input()
new_gift = []
while command != "No Money":
   current_command = command.split()

   if current_command[0]  == "OutOfStock" and current_command[1] in gifts:
        for index, value in enumerate(gifts):
            if current_command[1] == value:
                gifts.pop(index)
                gifts.insert(index, "None")

   elif current_command[0] == "Required":
       gift_is = current_command[1]
       index_is = int(current_command[2])
       gifts_len = len(gifts)
       if int(gifts_len) > index_is >= 0:
           gifts[index_is] = gift_is
           # gifts.pop(index_is)
           # gifts.insert(index_is, gift_is)


   elif current_command[0] =='JustInCase':
       gift_is = current_command[1]
       gifts.pop(-1)
       gifts.append(gift_is)
   command = input()
for index in gifts:
    if index == "None":
        pass
    else:
        print(index, end=" ")
