import re
text = input()
pattern = r"\b(?P<day>\d{2})(?P<sep>.|/|-)(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})\b"
valid = [object.groupdict()for object in re.finditer(pattern, text)]
for match in valid:
    print(f'Day: {match["day"]}, Month: {match["month"]}, Year: {match["year"]}')
a=123
