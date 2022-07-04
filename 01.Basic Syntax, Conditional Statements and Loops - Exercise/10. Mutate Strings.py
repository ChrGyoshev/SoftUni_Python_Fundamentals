string_a = input()
string_b = input()

for i in range (len(string_a)):
    f_str = string_a[i+1:]
    new_word = string_b[:i+1] + f_str
    if string_a[i] != string_b[i]:
        print(new_word)
