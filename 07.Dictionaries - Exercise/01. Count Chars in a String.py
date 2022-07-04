word = input().split()

dict = {}


for el in word:
    for le in el:
        if le not in dict:
            dict[le] = 0
        dict[le] += 1

for el, v in dict.items():
    print (f"{el} -> {v}")
