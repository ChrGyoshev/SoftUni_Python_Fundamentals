word = input().split()

dict = {}

for wor in word:
    wor_low = wor.lower()
    if wor_low not in dict:
        dict[wor_low]=0
    dict[wor_low] +=1


for key,value in dict.items():
    if value % 2 != 0:

        print(key, end=" ")
