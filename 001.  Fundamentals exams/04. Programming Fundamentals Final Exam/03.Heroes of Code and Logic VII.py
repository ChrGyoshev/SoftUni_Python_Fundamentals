def heal(dict,name,points):
    if dict[name]['HP'] + points > MAX_HP:
        healed = MAX_HP - dict[name]['HP']
        dict[name]['HP'] = 100
    else:
        dict[name]['HP'] += points
        healed = points
    print(f"{name} healed for {healed} HP!")
    return dict

def recharge(dict,name,points):
    if dict[name]['MP'] + points > MAX_MP:
        healed = MAX_MP - dict[name]['MP']
        dict[name]['MP'] = 200
    else:
        dict[name]['MP'] += points
        healed = points
    print(f"{name} recharged for {healed} MP!")
    return dict


def take_dmg(dict,name,dmg,attacker):
    dict[name]["HP"] -= dmg
    if dict[name]['HP'] > 0:
        print(f"{name} was hit for {dmg} HP by {attacker} and now has {dict[name]['HP']} HP left!")
    else:
        print(f"{name} has been killed by {attacker}!")
        del dict[name]
    return dict

def cast_spell(dict,name,mp_needed,spell_name):
    if dict[name]["MP"] >= mp_needed:
        dict[name]["MP"] -= mp_needed
        print(f"{name} has successfully cast {spell_name} and now has {dict[name]['MP']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")
    return dict

heroes = int(input())
MAX_HP = 100
MAX_MP = 200
heroes_dict = {}
for heroes in range(heroes):
    hero_name, hp,  mp= input().split()
    hp = int(hp)
    mp = int(mp)
    heroes_dict[hero_name] = {"HP": hp, "MP": mp}

command = input()

while not command == "End":
    current_command = command.split(" - ")
    if current_command[0] == "CastSpell":
        heroes_dict = cast_spell(heroes_dict,current_command[1],int(current_command[2]),current_command[3])
    elif current_command[0] == "TakeDamage":
        heroes_dict = take_dmg(heroes_dict,current_command[1],int(current_command[2]),current_command[3])
    elif current_command[0] == "Recharge":
        heroes_dict = recharge(heroes_dict,current_command[1],int(current_command[2]))
    elif current_command[0] == "Heal":
        heroes_dict = heal(heroes_dict,current_command[1], int(current_command[2]))
    command = input()

if heroes_dict:
    for key,value in heroes_dict.items():
        print(f"{key}")
        print(f"HP: {value['HP']}")
        print(f"MP: {value['MP']}")