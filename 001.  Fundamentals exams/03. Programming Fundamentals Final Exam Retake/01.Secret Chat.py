import re


def slicing(validator, mirror_words):
    for word in validator:
        if word.startswith("#"):
            word = word.split('#')
            word_two_reverse = word[3][::-1]
            if word[1] == word_two_reverse:
                mirror_words[word[1]] = word[3]
        elif word.startswith("@"):
            word = word.split('@')
            word_two_reverse = word[3][::-1]
            if word[1] == word_two_reverse:
                mirror_words[word[1]] = word[3]
    return validator, mirror_words



mirror_words = {}
text = input()
pattern = r"(@|#)[A-Za-z]{3,}\1\1[A-Za-z]{3,}\1"

validator = [obj.group() for obj in re.finditer(pattern, text)]

if not validator:
    print("No word pairs found!")

if validator:
    print(f'{len(validator)} word pairs found!')

validator, mirror_check = slicing(validator,mirror_words)

if mirror_check:
    result = [f"{key} <=> {value}"for key,value in mirror_check.items()]
    print("The mirror words are:")
    print(*result, sep=", ")
else:
    print("No mirror words!")