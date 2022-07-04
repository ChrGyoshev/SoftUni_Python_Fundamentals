import re
text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(.\d+)?($|(?=\s))"
validated = [obj.group()for obj in re.finditer(pattern,text)]
print(*validated)