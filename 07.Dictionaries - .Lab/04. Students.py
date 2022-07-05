word = input().split(":")
dict = {}
while not len(word) < 2:
    name,id,course = word[0],word[1],word[2]
    if course not in dict:
        dict[course] = {"name": [name], "id":[id]}
    else:
        dict[course]["name"].append(name)
        dict[course]["id"].append(id)

    word = input().split(":")
word= word[0].split("_")
word = str(" ".join(word))
names = []
ids = []
for key in dict:
    if key == word:
        names.append(dict[key]["name"])
        ids.append(dict[key]["id"])

for i in names:
    for j in ids:
        for q in range(len(i)):
            print(f"{i[q]} - {j[q]}")




