class Password_reset:
    result = ''
    def __init__(self,command):
        self.command = command


    def take_odd(self,command, text):
        result = ''
        for el in range(len(text)):
            if el % 2 != 0:
                result += text[el]
        print(result)
        Password_reset.result = result
        return result

    def cut(self,text,index,length):
        print(text[:index] + text[index+length:])
        Password_reset.result =text[:index] + text[index+length:]
        return text[:index] + text[index+length:]

    def substitute(self, text, substring, substitute):
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)

        else:
            print("Nothing to replace!")
        Password_reset.result = text

        return text
    def get_data(self):
        return f"Your password is: {Password_reset.result}"


text = input()
command = input()

while not command == "Done":
    command = command.split()
    checker = Password_reset(command[0])
    if command[0] == "TakeOdd":
        text=(checker.take_odd(command,text))

    elif command[0]=="Cut":
        text = (checker.cut(text,int(command[1]), int(command[2])))

    elif command[0] == "Substitute":
        text = checker.substitute(text,command[1],command[2])

    command = input()

print(checker.get_data())