import re

text = input()
pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

valid = re.findall(pattern,text)

print(*valid,sep=" ")
