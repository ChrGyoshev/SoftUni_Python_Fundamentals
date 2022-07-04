def changeall(msg,subst, replacement):
    msg=msg.replace(subst,replacement)
    return msg

def insert(msg,index,value):

    msg = msg[:index] + value + msg[index:]

    return msg

def move(msg,num):
    msg = msg[num:] + msg[:num]
    return msg


encrypted_msg = input()
command = input()

while command != "Decode":
    command = command.split("|")
    if command[0] == "ChangeAll":
        encrypted_msg = changeall(encrypted_msg,command[1], command[2])
    elif command[0] == "Insert":
        encrypted_msg = insert(encrypted_msg,int(command[1]), command[2])
    elif command[0] == "Move":
        encrypted_msg = move(encrypted_msg,int(command[1]))
    command = input()
print(f"The decrypted message is: {encrypted_msg}")