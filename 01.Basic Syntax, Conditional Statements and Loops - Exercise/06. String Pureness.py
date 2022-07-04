n_count = int(input())

for i in range(n_count):
    curr_command = input()
    is_pure = True
    if "," in curr_command:
        is_pure = False
    elif "." in curr_command:
        is_pure = False
    elif "_" in curr_command:
        is_pure = False
    if is_pure:
        print(f"{curr_command} is pure.")
    else:
        print(f"{curr_command} is not pure!")
