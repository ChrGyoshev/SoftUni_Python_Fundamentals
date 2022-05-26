schedule = input().split(", ")
command = input()

while not command == "course start":
    command = command.split(":")
    if command[0] == "Add":
        lesson_title = command[1]
        if lesson_title not in schedule:
            schedule.append(lesson_title)
    elif command[0] == "Insert":
        lesson_title,index = command[1], command[2]
        index = int(index)
        if lesson_title not in schedule:
            schedule.insert(index, lesson_title)

    elif command[0] == "Remove":
        lesson_title = command[1]
        lesson_title_exercise = lesson_title + "-Exercise"
        for i in range(len(schedule)):
            if schedule[i] == lesson_title or schedule[i] == lesson_title_exercise:
                schedule.pop(i)
                break

    elif command[0] == "Swap":
        lesson_title = command[1]
        lesson_title_two = command[2]
        lesson_title_exercise = lesson_title + "-Exercise"
        lesson_title_two_exercise = lesson_title_two + "-Exercise"
        if lesson_title in schedule:
            if lesson_title_two in schedule:
                lesson_title_index, lesson_title_two_index = schedule.index(lesson_title), schedule.index(lesson_title_two)
                schedule[lesson_title_index] = lesson_title_two
                schedule[lesson_title_two_index] = lesson_title
            if lesson_title_exercise in schedule:
                for el in range(len(schedule)):
                    if schedule[el] + "-Exercise" == lesson_title_exercise:
                        to_be_moved = lesson_title_exercise
                        schedule.remove(lesson_title_exercise)
                        schedule.insert(el+1, to_be_moved)
            elif lesson_title_two_exercise in schedule:
                for el in range(len(schedule)):
                    if schedule[el] + "-Exercise" == lesson_title_two_exercise:
                        to_be_moved = lesson_title_two_exercise
                        schedule.remove(lesson_title_two_exercise)
                        schedule.insert(el+1, to_be_moved)





    elif command[0] == "Exercise":
        lesson_title = command[1]
        to_be_added = lesson_title + "-Exercise"
        if lesson_title not in schedule:
            schedule.append(lesson_title)
            schedule.append(to_be_added)
        else:
            if to_be_added not in schedule:
                indexer = schedule.index(lesson_title)
                schedule.insert(indexer+1, to_be_added)


    command = input()

for el in range(len(schedule)):
    print(f"{el+1}.{schedule[el]}")