counter = int(input())
dict = {}


for _ in range (counter):
    word = input()
    syn = input()
    if word not in dict:
        dict[word] = []
    dict[word].append(syn)

for key, value in dict.items():
    print(f'{key} - {", ".join(value)}')
