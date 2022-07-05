import re

text = input()
pattern = r"\+359(\s|-)2\1\d{3}\1\d{4}\b"
valid = [obj.group() for obj in re.finditer(pattern,text)]
print(*valid,sep = ", ")
