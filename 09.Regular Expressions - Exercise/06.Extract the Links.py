import re
text = input()
pattern = r"w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+"
dict = []
while text:
    match = [object.group() for object in re.finditer(pattern,text)]
    if match:
        dict.extend(match)
    text = input()

print(*dict, sep="\n")
