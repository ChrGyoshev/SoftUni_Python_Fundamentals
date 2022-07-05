

def exist(dict, item, found):
    if item in dict:
        found = True
    return found


journal = input().split(", ")
command = input()

while not command == "Craft!":
    item_found = False
    command = command.split(" - ")
    if command[0] == "Collect":
        item = command[1]
        item_found = exist(journal, item, item_found)
        if not item_found:
            journal.append(item)
    elif command[0] == "Drop":
        item = command[1]
        item_found = exist(journal, item, item_found)
        if item_found:
            journal.remove(item)
    elif command[0] == "Combine Items":
        old_item, new_item = command[1].split(":")
        item_found = exist(journal,old_item, item_found)
        if item_found:
            old_item_index = journal.index(old_item) + 1
            journal.insert(old_item_index, new_item)

    elif command[0] == "Renew":
        item = command[1]
        item_found = exist(journal,item,item_found)
        if item_found:
            journal.remove(item)
            journal.append(item)
    command = input()
print(", ".join(journal))