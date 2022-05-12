import re

password = input()


def pass_validator(current):
    counter = 0
    pass_valid = True
    if len(current) >= 6 and len(current) <= 10:
        pass
    else:
        pass_valid = False
        print('Password must be between 6 and 10 characters')
    if re.match("^[A-Za-z0-9_-]*$", current):
        pass
    else:
        pass_valid = False
        print("Password must consist only of letters and digits")
    for char in password:
        if char.isdigit():
            counter += 1
    if counter >= 2:
        pass
    else:
        pass_valid = False
        print("Password must have at least 2 digits")
    if pass_valid:
        print("Password is valid")


pass_validator(password)
