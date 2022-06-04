command = input()
force = {}

while not command == "Lumpawaroo":
    user_is_found = False
    test_line = command.split(" | ")
    if len(test_line) > 1:
        side_to_join, user_to_join = test_line[0],test_line[1]
        for side, users in force.items():
            if user_to_join in users:
                user_is_found = True
                break
        if user_is_found:
            command = input()
            continue
        if side_to_join not in force:
            force[side_to_join]= []
        force[side_to_join].append(user_to_join)
    else:
        command = command.split(" -> ")
        user_to_join, side_to_join =command[0],command[1]
        if side_to_join not in force:
            force[side_to_join]=[]
            force[side_to_join].append(user_to_join)
        for side, jedi in force.items():
            if user_to_join in jedi:
                user_is_found = True
                force[side].pop(jedi.index(user_to_join))
        print(f'{user_to_join} joins the {side_to_join} side!')
        force[side_to_join].append(user_to_join)
    command = input()
for key, value in force.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        for name in value:
            print(f'! {name}')
