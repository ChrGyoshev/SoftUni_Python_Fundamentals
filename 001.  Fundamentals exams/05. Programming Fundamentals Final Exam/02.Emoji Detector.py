import re


def multiplyList(xList):
    product = 1
    for x in xList:
        product = product * x
    return product

text = input()
cool_threshold_pattern = r"\d"
pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1"

cool_threshhold_sum =[int(el) for el in re.findall(cool_threshold_pattern, text)]
cool_threshhold_sum = multiplyList(cool_threshhold_sum)

validator = [obj.group() for obj in re.finditer(pattern, text)]
print(f"Cool threshold: {cool_threshhold_sum}")
final_list = []
for element in validator:
    sum_regex = 0
    for lett in element:
        if lett.isalpha():
            sum_regex += ord(lett)
    if sum_regex > cool_threshhold_sum:
        final_list.append(element)

print(f"{len(validator)} emojis found in the text. The cool ones are:")

print(*final_list, sep= "\n")