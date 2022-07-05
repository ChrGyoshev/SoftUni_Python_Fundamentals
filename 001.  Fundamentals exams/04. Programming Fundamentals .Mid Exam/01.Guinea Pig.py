def unnecessary(groc, item):
    if item in groc:
        groc.remove(item)
    return groc


def urgent(groc, item):
    if item not in groc:
        groc.insert(0, item)
    return groc


def correct(groc, old_item, new_item):
    if old_item in groc:
        groc = (list(map(lambda item: item.replace(old_item, new_item), groc)))
    return groc

def rearrange(groc,item):
    if item in groc:
        groc.remove(item)
        groc.append(item)
    return groc



groceries = input().split("!")
command = input()

while not command == "Go Shopping!":
    command = command.split()
    if command[0] == "Unnecessary":
        groceries = unnecessary(groceries, command[1])
    elif command[0] == "Urgent":
        groceries = urgent(groceries, command[1])
    elif command[0] == "Correct":
        groceries = correct(groceries, command[1], command[2])
    elif command[0] == "Rearrange":
        groceries = rearrange(groceries,command[1])

    command = input()
print(", ".join(groceries))