import math
text = input().split()
command = input().split()


while not command[0] == "3:1":
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > (len(text)-1):
            end_index = (len(text)-1)
        merged = "".join(text[start_index:(end_index+1)])
        text[start_index:end_index+1] = [merged]



    if command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        element = text[index]
        partitions_l = []
        partition_length = math.floor(len(element)/partitions)
        for el in range(0,partitions):
            if el != (partitions -1):
                partitions_l.append(element[el*partition_length:(el+1)*partition_length])
            else:
                partitions_l.append(element[el*partition_length:])
        text[index:index+1] = partitions_l



    command = input().split()

print(" ".join(text))
