notes = input()
list = [0] * 10
while not notes == "End":
    notes = notes.split("-")
    importance, note = int(notes[0])-1, notes[1]
    list.pop(importance)
    list.insert(importance, note)


    notes = input()

list = [n for n in list if n !=0]

print(list)
