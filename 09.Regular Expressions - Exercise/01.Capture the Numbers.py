import re
text = input()
pattern = r"\d+"
result_list = []
while text:
    validator = re.findall(pattern,text)
    if validator:
        result_list.extend(validator)
    text = input()
print(*result_list)
