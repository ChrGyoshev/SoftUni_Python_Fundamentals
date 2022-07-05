def shooting(i,tar):
    if i in range(len(tar)):
        divider = tar[i]
        tar[i] = -1
        for obj in range(len(tar)):
            if tar[obj] == -1:
                continue
            else:
                if tar[obj] <= divider:
                    tar[obj] += divider
                else:
                    tar[obj] -= divider
    return tar


targets = list(map(int, input().split()))
command = input()

while not command == "End":
    index = int(command)
    targets = shooting(index,targets)
    command = input()
shot_targets= list(filter(lambda x: x==-1, targets))
print(f'Shot targets: {len(shot_targets)} -> {" ".join([str(el) for el in targets])}')

