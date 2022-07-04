sequence_of_elements = input().split()
command = input()
moves = 0
while  command != "end":
    if len(sequence_of_elements)<=0:
        print(f"You have won in {moves} turns!")
        quit()
    moves +=1
    index_one,index_two = list(map(int, command.split()))
    if index_one == index_two or index_one not in range(len(sequence_of_elements)) or index_two not in range(len(sequence_of_elements)):
        print("Invalid input! Adding additional elements to the board")
        middle_part = len(sequence_of_elements) // 2
        element = f"-{moves}a"
        sequence_of_elements.insert(middle_part, element)
        sequence_of_elements.insert(middle_part, element)

    elif sequence_of_elements[index_one] == sequence_of_elements[index_two]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index_one]}!")
        sequence_of_elements = [el for el in sequence_of_elements if el!=sequence_of_elements[index_one]]


    elif sequence_of_elements[index_one] != sequence_of_elements[index_two]:
        print("Try again!")

    if len(sequence_of_elements)<=0:
        print(f"You have won in {moves} turns!")
        quit()
    command = input()


print("Sorry you lose :(")
print(f'{" ".join(sequence_of_elements)}')