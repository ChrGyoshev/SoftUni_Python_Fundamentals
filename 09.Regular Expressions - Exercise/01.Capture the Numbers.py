import re
text = input()
pattern = r"(^_|(?<=\s_))[A-Za-z0-9]+\b"

validator = [obj.group()for obj in re.finditer(pattern, text)]
print(*validator, sep= ",")