text = input()

while not text == "end":
    new_str = text[::-1]
    print(f'{text} = {new_str}')

    text = input()