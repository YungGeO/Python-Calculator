import math


class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y


name = str = input("enter your name ")
print(f"hello {name} ")

action = str = input("you want to do add,sub,mul or exit?").lower()


while (action != "exit"):

    if action == "add":

        x = int(input("give me first number "))
        y = int(input("give me second number "))
        calc = Calculator(x, y)
        print("Result: ", calc.add())
    elif action == "sub":
        X = int(input("give me first number "))
        Y = int(input("give me second number "))
        calc = Calculator(x, y)
        print("Result: ", calc.sub())
    elif action == "mul":
        X = int(input("give me first number "))
        Y = int(input("give me second number "))
        calc = Calculator(x, y)
        print("Result: ", calc.mul())
    else:
        print("unknown command.Try again")
    action = input("you want to do add,sub,mul or exit?").lower()
