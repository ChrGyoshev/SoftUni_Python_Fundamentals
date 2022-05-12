mapper = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junks = {}

while True:
    is_found = False
    materials = input().split()
    for i in range(0, len(materials),2):
        quantity = int(materials[i])
        item = materials[i+1].lower()
        if item in key_materials:
            key_materials[item] += quantity
        else:
            if item not in junks:
                junks[item] = quantity
            else:
                junks[item] += quantity
        for value in key_materials.values():
            if value >= 250:
                print(f"{mapper[item]} obtained!")
                key_materials[item] -= 250
                is_found = True
                break
        if is_found:
            break

    if is_found:
        break

for item,value in key_materials.items():
    print(f'{item}: {value}')

for item, value in junks.items():
    print(f'{item}: {value}')
