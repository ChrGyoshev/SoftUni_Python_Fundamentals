char_one = input()
char_two = input()

def asci(a,b):
    result = []
    a = (ord(char_one))
    b = (ord(char_two))
    for char in range(a +1, b):
        asci = chr(char)
        result.append(asci)

    return result

print(*asci(char_one,char_two))
