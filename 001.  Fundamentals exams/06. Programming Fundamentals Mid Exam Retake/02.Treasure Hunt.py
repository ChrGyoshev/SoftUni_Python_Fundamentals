def loot(dict,curr_comm):
    [dict.insert(0,el) for el in curr_comm if el not in dict]
    return dict


def drop(dict,index):
    if index in range(len(dict)):
        element = dict.pop(index)
        dict.append(element)
    return dict

def steal(dict, index):
    if index >= len(dict):
        print(", ".join([str(el) for el in dict]))
        dict.clear()
    else:

        elements = dict[len(dict)-index:]
        print(", ".join([str(el)for el in elements]))
        dict = dict[:-index]


    return dict




treasure_chest = input().split("|")
command = input()

while not command == "Yohoho!":
    command = command.split()
    if command[0] == "Loot":
        treasure_chest = loot(treasure_chest, command[1:])
    elif command[0] == "Drop":
        treasure_chest = drop(treasure_chest,int(command[1]))
    elif command[0] == "Steal":
        treasure_chest = steal(treasure_chest, int(command[1]))
    command = input()
if treasure_chest:
    len_of_elements = len(treasure_chest)
    sum_of_elements = [len(el)for el in treasure_chest]
    sum_of_elements = sum(sum_of_elements) /len_of_elements
    print(f"Average treasure gain: {sum_of_elements:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")