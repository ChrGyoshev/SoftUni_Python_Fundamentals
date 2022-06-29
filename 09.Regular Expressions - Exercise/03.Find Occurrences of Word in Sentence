import re
text = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\.,_-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"
validator = [object.group()for object in re.finditer(pattern, text)]
print(*validator, sep="\n")