command = input()
submission = {}
users = {}
while not command == "exam finished":
    command = command.split("-")
    if command[1] == "banned":
        del users[command[0]]
        command =input()
        continue
    user = command[0]
    lang = command[1]
    points = int(command[2])
    if not lang in submission:
        submission[lang] = 0
    submission[lang]+=1
    if not user in users:
        users[user] = points
    if users[user] < points:
        users[user] = points


    command = input()
print("Results:")
for user, points in users.items():
    print(f'{user} | {points}')
print("Submissions:")
for s,v in submission.items():
    print(f"{s} - {v}")